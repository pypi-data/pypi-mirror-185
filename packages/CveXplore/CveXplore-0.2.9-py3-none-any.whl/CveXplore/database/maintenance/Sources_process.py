"""
Source processing classes
=========================
"""
import datetime
import hashlib
import json
import logging
import os
import shutil
from collections import namedtuple
from xml.sax import make_parser

import pymongo
from dateutil.parser import parse as parse_datetime
from pymongo import TEXT, ASCENDING

from .Config import Configuration
from .Toolkit import generate_title
from .content_handlers import CapecHandler, CWEHandler
from .db_action import DatabaseAction
from CveXplore.database.connection.mongo_db import MongoDBConnection
from .file_handlers import XMLFileHandler, JSONFileHandler

file_prefix = "nvdcve-1.1-"
file_suffix = ".json.gz"
file_mod = "modified"
file_rec = "recent"

date = datetime.datetime.now()
year = date.year + 1

# default config
defaultvalue = {"cwe": "Unknown"}

cveStartYear = Configuration.getCVEStartYear()


class CPEDownloads(JSONFileHandler):
    """
    Class processing CPE source files
    """

    def __init__(self):
        self.feed_type = "CPE"
        self.prefix = "matches.item"
        super().__init__(self.feed_type, self.prefix)

        self.feed_url = Configuration.getFeedURL(self.feed_type.lower())

        self.logger = logging.getLogger("CPEDownloads")

    @staticmethod
    def process_cpe_item(item=None):
        if item is None:
            return None
        if "cpe23Uri" not in item:
            return None

        cpe = {
            "title": generate_title(item["cpe23Uri"]),
            "cpe_2_2": item["cpe23Uri"],
            "cpe_name": item["cpe_name"],
            "vendor": item["cpe23Uri"].split(":")[3],
            "product": item["cpe23Uri"].split(":")[4],
        }

        version_info = ""
        if "versionStartExcluding" in item:
            cpe["versionStartExcluding"] = item["versionStartExcluding"]
            version_info += cpe["versionStartExcluding"] + "_VSE"
        if "versionStartIncluding" in item:
            cpe["versionStartIncluding"] = item["versionStartIncluding"]
            version_info += cpe["versionStartIncluding"] + "_VSI"
        if "versionEndExcluding" in item:
            cpe["versionEndExcluding"] = item["versionEndExcluding"]
            version_info += cpe["versionEndExcluding"] + "_VEE"
        if "versionEndIncluding" in item:
            cpe["versionEndIncluding"] = item["versionEndIncluding"]
            version_info += cpe["versionEndIncluding"] + "_VEI"

        sha1_hash = hashlib.sha1(
            cpe["cpe_2_2"].encode("utf-8") + version_info.encode("utf-8")
        ).hexdigest()

        cpe["id"] = sha1_hash

        return cpe

    def process_item(self, item):
        cpe = self.process_cpe_item(item)

        if cpe is not None:
            if self.is_update:
                self.queue.put(
                    DatabaseAction(
                        action=DatabaseAction.actions.UpdateOne,
                        collection=self.feed_type.lower(),
                        doc=cpe,
                    )
                )
            else:
                self.queue.put(
                    DatabaseAction(
                        action=DatabaseAction.actions.InsertOne,
                        collection=self.feed_type.lower(),
                        doc=cpe,
                    )
                )

    def update(self, **kwargs):
        self.logger.info("CPE database update started")

        # if collection is non-existent; assume it's not an update
        if self.feed_type.lower() not in self.getTableNames():
            self.is_update = False

        self.process_downloads([self.feed_url])

        self.logger.info("Finished CPE database update")

        return self.last_modified

    def populate(self, **kwargs):
        self.logger.info("CPE Database population started")

        self.queue.clear()

        self.delColInfo(self.feed_type.lower())

        self.dropCollection(self.feed_type.lower())

        DatabaseIndexer().create_indexes(collection=self.feed_type.lower())

        self.is_update = False

        self.process_downloads([self.feed_url])

        self.logger.info("Finished CPE database population")

        return self.last_modified


class CVEDownloads(JSONFileHandler):
    """
    Class processing CVE source files
    """

    def __init__(self):
        self.feed_type = "CVES"
        self.prefix = "CVE_Items.item"
        super().__init__(self.feed_type, self.prefix)

        self.feed_url = Configuration.getFeedURL("cve")
        self.modfile = file_prefix + file_mod + file_suffix
        self.recfile = file_prefix + file_rec + file_suffix

        self.logger = logging.getLogger("CVEDownloads")

    @staticmethod
    def get_cve_year_range():
        """
        Method to fetch the years where we need cve's for
        """
        for a_year in range(cveStartYear, year):
            yield a_year

    @staticmethod
    def get_cpe_info(cpeuri):
        query = {}
        version_info = ""
        if "versionStartExcluding" in cpeuri:
            query["versionStartExcluding"] = cpeuri["versionStartExcluding"]
            version_info += query["versionStartExcluding"] + "_VSE"
        if "versionStartIncluding" in cpeuri:
            query["versionStartIncluding"] = cpeuri["versionStartIncluding"]
            version_info += query["versionStartIncluding"] + "_VSI"
        if "versionEndExcluding" in cpeuri:
            query["versionEndExcluding"] = cpeuri["versionEndExcluding"]
            version_info += query["versionEndExcluding"] + "_VEE"
        if "versionEndIncluding" in cpeuri:
            query["versionEndIncluding"] = cpeuri["versionEndIncluding"]
            version_info += query["versionEndIncluding"] + "_VEI"

        return query, version_info

    @staticmethod
    def add_if_missing(cve, key, value):
        if value not in cve[key]:
            cve[key].append(value)
        return cve

    @staticmethod
    def get_vendor_product(cpeUri):
        vendor = cpeUri.split(":")[3]
        product = cpeUri.split(":")[4]
        return vendor, product

    @staticmethod
    def stem(cpeUri):
        cpeArr = cpeUri.split(":")
        return ":".join(cpeArr[:5])

    def process_cve_item(self, item=None):
        if item is None:
            return None
        if "ASSIGNER" not in item["cve"]["CVE_data_meta"]:
            item["cve"]["CVE_data_meta"]["ASSIGNER"] = None

        cve = {
            "id": item["cve"]["CVE_data_meta"]["ID"],
            "assigner": item["cve"]["CVE_data_meta"]["ASSIGNER"],
            "Published": parse_datetime(item["publishedDate"], ignoretz=True),
            "Modified": parse_datetime(item["lastModifiedDate"], ignoretz=True),
            "last-modified": parse_datetime(item["lastModifiedDate"], ignoretz=True),
        }

        for description in item["cve"]["description"]["description_data"]:
            if description["lang"] == "en":
                if "summary" in cve:
                    cve["summary"] += " {}".format(description["value"])
                else:
                    cve["summary"] = description["value"]
        if "impact" in item:
            cve["access"] = {}
            cve["impact"] = {}
            if "baseMetricV3" in item["impact"]:
                cve["impact3"] = {}
                cve["exploitability3"] = {}
                cve["impact3"]["availability"] = item["impact"]["baseMetricV3"][
                    "cvssV3"
                ]["availabilityImpact"]
                cve["impact3"]["confidentiality"] = item["impact"]["baseMetricV3"][
                    "cvssV3"
                ]["confidentialityImpact"]
                cve["impact3"]["integrity"] = item["impact"]["baseMetricV3"]["cvssV3"][
                    "integrityImpact"
                ]
                cve["exploitability3"]["attackvector"] = item["impact"]["baseMetricV3"][
                    "cvssV3"
                ]["attackVector"]
                cve["exploitability3"]["attackcomplexity"] = item["impact"][
                    "baseMetricV3"
                ]["cvssV3"]["attackComplexity"]
                cve["exploitability3"]["privilegesrequired"] = item["impact"][
                    "baseMetricV3"
                ]["cvssV3"]["privilegesRequired"]
                cve["exploitability3"]["userinteraction"] = item["impact"][
                    "baseMetricV3"
                ]["cvssV3"]["userInteraction"]
                cve["exploitability3"]["scope"] = item["impact"]["baseMetricV3"][
                    "cvssV3"
                ]["scope"]
                cve["cvss3"] = float(
                    item["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]
                )
                cve["cvss3-vector"] = item["impact"]["baseMetricV3"]["cvssV3"][
                    "vectorString"
                ]
                cve["impactScore3"] = float(
                    item["impact"]["baseMetricV3"]["impactScore"]
                )
                cve["exploitabilityScore3"] = float(
                    item["impact"]["baseMetricV3"]["exploitabilityScore"]
                )
            else:
                cve["cvss3"] = None
            if "baseMetricV2" in item["impact"]:
                cve["access"]["authentication"] = item["impact"]["baseMetricV2"][
                    "cvssV2"
                ]["authentication"]
                cve["access"]["complexity"] = item["impact"]["baseMetricV2"]["cvssV2"][
                    "accessComplexity"
                ]
                cve["access"]["vector"] = item["impact"]["baseMetricV2"]["cvssV2"][
                    "accessVector"
                ]
                cve["impact"]["availability"] = item["impact"]["baseMetricV2"][
                    "cvssV2"
                ]["availabilityImpact"]
                cve["impact"]["confidentiality"] = item["impact"]["baseMetricV2"][
                    "cvssV2"
                ]["confidentialityImpact"]
                cve["impact"]["integrity"] = item["impact"]["baseMetricV2"]["cvssV2"][
                    "integrityImpact"
                ]
                cve["cvss"] = float(
                    item["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
                )
                cve["exploitabilityScore"] = float(
                    item["impact"]["baseMetricV2"]["exploitabilityScore"]
                )
                cve["impactScore"] = float(
                    item["impact"]["baseMetricV2"]["impactScore"]
                )
                cve["cvss-time"] = parse_datetime(
                    item["lastModifiedDate"], ignoretz=True
                )  # NVD JSON lacks the CVSS time which was present in the original XML format
                cve["cvss-vector"] = item["impact"]["baseMetricV2"]["cvssV2"][
                    "vectorString"
                ]
            else:
                cve["cvss"] = None
        if "references" in item["cve"]:
            cve["references"] = []
            for ref in item["cve"]["references"]["reference_data"]:
                cve["references"].append(ref["url"])
        if "configurations" in item:
            cve["vulnerable_configuration"] = []
            cve["vulnerable_product"] = []
            cve["vendors"] = []
            cve["products"] = []
            cve["vulnerable_product_stems"] = []
            cve["vulnerable_configuration_stems"] = []
            for cpe in item["configurations"]["nodes"]:
                if "cpe_match" in cpe:
                    for cpeuri in cpe["cpe_match"]:
                        if "cpe23Uri" not in cpeuri:
                            continue
                        if cpeuri["vulnerable"]:
                            query, version_info = self.get_cpe_info(cpeuri)
                            if query != {}:
                                query["id"] = hashlib.sha1(
                                    cpeuri["cpe23Uri"].encode("utf-8")
                                    + version_info.encode("utf-8")
                                ).hexdigest()
                                cpe_info = self.getCPEVersionInformation(query)
                                if cpe_info:
                                    if cpe_info["cpe_name"]:
                                        for vulnerable_version in cpe_info["cpe_name"]:
                                            cve = self.add_if_missing(
                                                cve,
                                                "vulnerable_product",
                                                vulnerable_version["cpe23Uri"],
                                            )
                                            cve = self.add_if_missing(
                                                cve,
                                                "vulnerable_configuration",
                                                vulnerable_version["cpe23Uri"],
                                            )
                                            cve = self.add_if_missing(
                                                cve,
                                                "vulnerable_configuration_stems",
                                                self.stem(
                                                    vulnerable_version["cpe23Uri"]
                                                ),
                                            )
                                            vendor, product = self.get_vendor_product(
                                                vulnerable_version["cpe23Uri"]
                                            )
                                            cve = self.add_if_missing(
                                                cve, "vendors", vendor
                                            )
                                            cve = self.add_if_missing(
                                                cve, "products", product
                                            )
                                            cve = self.add_if_missing(
                                                cve,
                                                "vulnerable_product_stems",
                                                self.stem(
                                                    vulnerable_version["cpe23Uri"]
                                                ),
                                            )
                                    else:
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_product",
                                            cpeuri["cpe23Uri"],
                                        )
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_configuration",
                                            cpeuri["cpe23Uri"],
                                        )
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_configuration_stems",
                                            self.stem(cpeuri["cpe23Uri"]),
                                        )
                                        vendor, product = self.get_vendor_product(
                                            cpeuri["cpe23Uri"]
                                        )
                                        cve = self.add_if_missing(
                                            cve, "vendors", vendor
                                        )
                                        cve = self.add_if_missing(
                                            cve, "products", product
                                        )
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_product_stems",
                                            self.stem(cpeuri["cpe23Uri"]),
                                        )
                            else:
                                # If the cpe_match did not have any of the version start/end modifiers,
                                # add the CPE string as it is.
                                cve = self.add_if_missing(
                                    cve, "vulnerable_product", cpeuri["cpe23Uri"]
                                )
                                cve = self.add_if_missing(
                                    cve, "vulnerable_configuration", cpeuri["cpe23Uri"]
                                )
                                cve = self.add_if_missing(
                                    cve,
                                    "vulnerable_configuration_stems",
                                    self.stem(cpeuri["cpe23Uri"]),
                                )
                                vendor, product = self.get_vendor_product(
                                    cpeuri["cpe23Uri"]
                                )
                                cve = self.add_if_missing(cve, "vendors", vendor)
                                cve = self.add_if_missing(cve, "products", product)
                                cve = self.add_if_missing(
                                    cve,
                                    "vulnerable_product_stems",
                                    self.stem(cpeuri["cpe23Uri"]),
                                )
                        else:
                            cve = self.add_if_missing(
                                cve, "vulnerable_configuration", cpeuri["cpe23Uri"]
                            )
                            cve = self.add_if_missing(
                                cve,
                                "vulnerable_configuration_stems",
                                self.stem(cpeuri["cpe23Uri"]),
                            )
                if "children" in cpe:
                    for child in cpe["children"]:
                        if "cpe_match" in child:
                            for cpeuri in child["cpe_match"]:
                                if "cpe23Uri" not in cpeuri:
                                    continue
                                if cpeuri["vulnerable"]:
                                    query, version_info = self.get_cpe_info(cpeuri)
                                    if query != {}:
                                        query["id"] = hashlib.sha1(
                                            cpeuri["cpe23Uri"].encode("utf-8")
                                            + version_info.encode("utf-8")
                                        ).hexdigest()
                                        cpe_info = self.getCPEVersionInformation(query)
                                        if cpe_info:
                                            if cpe_info["cpe_name"]:
                                                for vulnerable_version in cpe_info[
                                                    "cpe_name"
                                                ]:
                                                    cve = self.add_if_missing(
                                                        cve,
                                                        "vulnerable_product",
                                                        vulnerable_version["cpe23Uri"],
                                                    )
                                                    cve = self.add_if_missing(
                                                        cve,
                                                        "vulnerable_configuration",
                                                        vulnerable_version["cpe23Uri"],
                                                    )
                                                    cve = self.add_if_missing(
                                                        cve,
                                                        "vulnerable_configuration_stems",
                                                        self.stem(
                                                            vulnerable_version[
                                                                "cpe23Uri"
                                                            ]
                                                        ),
                                                    )
                                                    (
                                                        vendor,
                                                        product,
                                                    ) = self.get_vendor_product(
                                                        vulnerable_version["cpe23Uri"]
                                                    )
                                                    cve = self.add_if_missing(
                                                        cve, "vendors", vendor
                                                    )
                                                    cve = self.add_if_missing(
                                                        cve, "products", product
                                                    )
                                                    cve = self.add_if_missing(
                                                        cve,
                                                        "vulnerable_product_stems",
                                                        self.stem(
                                                            vulnerable_version[
                                                                "cpe23Uri"
                                                            ]
                                                        ),
                                                    )
                                            else:
                                                cve = self.add_if_missing(
                                                    cve,
                                                    "vulnerable_product",
                                                    cpeuri["cpe23Uri"],
                                                )
                                                cve = self.add_if_missing(
                                                    cve,
                                                    "vulnerable_configuration",
                                                    cpeuri["cpe23Uri"],
                                                )
                                                cve = self.add_if_missing(
                                                    cve,
                                                    "vulnerable_configuration_stems",
                                                    self.stem(cpeuri["cpe23Uri"]),
                                                )
                                                (
                                                    vendor,
                                                    product,
                                                ) = self.get_vendor_product(
                                                    cpeuri["cpe23Uri"]
                                                )
                                                cve = self.add_if_missing(
                                                    cve, "vendors", vendor
                                                )
                                                cve = self.add_if_missing(
                                                    cve, "products", product
                                                )
                                                cve = self.add_if_missing(
                                                    cve,
                                                    "vulnerable_product_stems",
                                                    self.stem(cpeuri["cpe23Uri"]),
                                                )
                                    else:
                                        # If the cpe_match did not have any of the version start/end modifiers,
                                        # add the CPE string as it is.
                                        if "cpe23Uri" not in cpeuri:
                                            continue
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_product",
                                            cpeuri["cpe23Uri"],
                                        )
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_configuration",
                                            cpeuri["cpe23Uri"],
                                        )
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_configuration_stems",
                                            self.stem(cpeuri["cpe23Uri"]),
                                        )
                                        vendor, product = self.get_vendor_product(
                                            cpeuri["cpe23Uri"]
                                        )
                                        cve = self.add_if_missing(
                                            cve, "vendors", vendor
                                        )
                                        cve = self.add_if_missing(
                                            cve, "products", product
                                        )
                                        cve = self.add_if_missing(
                                            cve,
                                            "vulnerable_product_stems",
                                            self.stem(cpeuri["cpe23Uri"]),
                                        )
                                else:
                                    if "cpe23Uri" not in cpeuri:
                                        continue
                                    cve = self.add_if_missing(
                                        cve,
                                        "vulnerable_configuration",
                                        cpeuri["cpe23Uri"],
                                    )
                                    cve = self.add_if_missing(
                                        cve,
                                        "vulnerable_configuration_stems",
                                        self.stem(cpeuri["cpe23Uri"]),
                                    )
        if "problemtype" in item["cve"]:
            for problem in item["cve"]["problemtype"]["problemtype_data"]:
                for cwe in problem[
                    "description"
                ]:  # NVD JSON not clear if we can get more than one CWE per CVE (until we take the last one) -
                    # NVD-CWE-Other??? list?
                    if cwe["lang"] == "en":
                        cve["cwe"] = cwe["value"]
            if not ("cwe" in cve):
                cve["cwe"] = defaultvalue["cwe"]
        else:
            cve["cwe"] = defaultvalue["cwe"]
        cve["vulnerable_configuration_cpe_2_2"] = []
        return cve

    def process_item(self, item):
        cve = self.process_cve_item(item)

        if cve is not None:
            if self.is_update:
                self.queue.put(
                    DatabaseAction(
                        action=DatabaseAction.actions.UpdateOne,
                        collection=self.feed_type.lower(),
                        doc=cve,
                    )
                )
            else:
                self.queue.put(
                    DatabaseAction(
                        action=DatabaseAction.actions.InsertOne,
                        collection=self.feed_type.lower(),
                        doc=cve,
                    )
                )

    def update(self):
        self.logger.info("CVE database update started")

        # if collection is non-existent; assume it's not an update
        if "cves" not in self.getTableNames():
            self.is_update = False

        self.process_downloads(
            [self.feed_url + self.modfile, self.feed_url + self.recfile]
        )

        self.logger.info("Finished CVE database update")

        return self.last_modified

    def populate(self):
        urls = []

        self.logger.info("CVE database population started")

        self.logger.info(
            "Starting CVE database population starting from year: {}".format(
                cveStartYear
            )
        )

        self.is_update = False

        self.queue.clear()

        self.delColInfo(self.feed_type.lower())

        self.dropCollection(self.feed_type.lower())

        DatabaseIndexer().create_indexes(collection=self.feed_type.lower())

        for x in self.get_cve_year_range():
            getfile = file_prefix + str(x) + file_suffix

            urls.append(self.feed_url + getfile)

        self.process_downloads(urls)

        self.logger.info("Finished CVE database population")

        return self.last_modified


class VIADownloads(JSONFileHandler):
    """
    Class processing VIA4 source files
    """

    def __init__(self):
        self.feed_type = "VIA4"
        self.prefix = "cves"
        super().__init__(self.feed_type, self.prefix)

        self.feed_url = Configuration.getFeedURL(self.feed_type.lower())

        self.logger = logging.getLogger("VIADownloads")

    def file_to_queue(self, file_tuple):

        working_dir, filename = file_tuple

        for cve in self.ijson_handler.fetch(filename=filename, prefix=self.prefix):
            x = 0
            for key, val in cve.items():
                entry_dict = {"id": key}
                entry_dict.update(val)
                self.process_item(item=entry_dict)
                x += 1

            self.logger.debug("Processed {} items from file: {}".format(x, filename))

        with open(filename, "rb") as input_file:
            data = json.loads(input_file.read().decode("utf-8"))

            self.setColInfo("via4", "sources", data["metadata"]["sources"])
            self.setColInfo("via4", "searchables", data["metadata"]["searchables"])

            self.logger.debug("Processed metadata from file: {}".format(filename))

        try:
            self.logger.debug("Removing working dir: {}".format(working_dir))
            shutil.rmtree(working_dir)
        except Exception as err:
            self.logger.error(
                "Failed to remove working dir; error produced: {}".format(err)
            )

    def process_item(self, item):

        if self.is_update:
            self.queue.put(
                DatabaseAction(
                    action=DatabaseAction.actions.UpdateOne,
                    collection=self.feed_type.lower(),
                    doc=item,
                )
            )
        else:
            self.queue.put(
                DatabaseAction(
                    action=DatabaseAction.actions.InsertOne,
                    collection=self.feed_type.lower(),
                    doc=item,
                )
            )

    def update(self, **kwargs):
        self.logger.info("VIA4 database update started")

        # if collection is non-existent; assume it's not an update
        if self.feed_type.lower() not in self.getTableNames():
            self.is_update = False

        self.process_downloads([self.feed_url])

        self.logger.info("Finished VIA4 database update")

        return self.last_modified

    def populate(self, **kwargs):
        self.is_update = False
        self.queue.clear()

        self.delColInfo(self.feed_type.lower())

        self.dropCollection(self.feed_type.lower())

        return self.update()


class CAPECDownloads(XMLFileHandler):
    """
    Class processing CAPEC source files
    """

    def __init__(self):
        self.feed_type = "CAPEC"
        super().__init__(self.feed_type)

        self.feed_url = Configuration.getFeedURL(self.feed_type.lower())

        self.logger = logging.getLogger("CAPECDownloads")

        # make parser
        self.parser = make_parser()
        self.ch = CapecHandler()
        self.parser.setContentHandler(self.ch)

    def file_to_queue(self, file_tuple):

        working_dir, filename = file_tuple

        self.parser.parse(filename)
        x = 0
        for attack in self.ch.capec:
            self.process_item(attack)
            x += 1

        self.logger.debug("Processed {} entries from file: {}".format(x, filename))

        try:
            self.logger.debug("Removing working dir: {}".format(working_dir))
            shutil.rmtree(working_dir)
        except Exception as err:
            self.logger.error(
                "Failed to remove working dir; error produced: {}".format(err)
            )

    def update(self, **kwargs):
        self.logger.info("CAPEC database update started")

        # if collection is non-existent; assume it's not an update
        if self.feed_type.lower() not in self.getTableNames():
            self.is_update = False

        self.process_downloads([self.feed_url])

        self.logger.info("Finished CAPEC database update")

        return self.last_modified

    def populate(self, **kwargs):
        self.is_update = False
        self.queue.clear()

        self.delColInfo(self.feed_type.lower())

        self.dropCollection(self.feed_type.lower())

        return self.update()


class CWEDownloads(XMLFileHandler):
    """
    Class processing CWE source files
    """

    def __init__(self):
        self.feed_type = "CWE"
        super().__init__(self.feed_type)

        self.feed_url = Configuration.getFeedURL(self.feed_type.lower())

        self.logger = logging.getLogger("CWEDownloads")

        # make parser
        self.parser = make_parser()
        self.ch = CWEHandler()
        self.parser.setContentHandler(self.ch)

    def file_to_queue(self, file_tuple):

        working_dir, filename = file_tuple

        self.parser.parse(filename)
        x = 0
        for cwe in self.ch.cwe:
            try:
                cwe["related_weaknesses"] = list(set(cwe["related_weaknesses"]))
            except KeyError:
                pass
            self.process_item(cwe)
            x += 1

        self.logger.debug("Processed {} entries from file: {}".format(x, filename))

        try:
            self.logger.debug("Removing working dir: {}".format(working_dir))
            shutil.rmtree(working_dir)
        except Exception as err:
            self.logger.error(
                "Failed to remove working dir; error produced: {}".format(err)
            )

    def update(self, **kwargs):
        self.logger.info("CWE database update started")

        # if collection is non-existent; assume it's not an update
        if self.feed_type.lower() not in self.getTableNames():
            self.is_update = False

        self.process_downloads([self.feed_url])

        self.logger.info("Finished CWE database update")

        return self.last_modified

    def populate(self, **kwargs):
        self.is_update = False
        self.queue.clear()

        self.delColInfo(self.feed_type.lower())

        self.dropCollection(self.feed_type.lower())

        return self.update()


MongoUniqueIndex = namedtuple("MongoUniqueIndex", "index name unique")
MongoAddIndex = namedtuple("MongoAddIndex", "index name")


class DatabaseIndexer(object):
    """
    Class processing the Mongodb indexes
    """

    def __init__(self):

        database = MongoDBConnection(**json.loads(os.getenv("MONGODB_CON_DETAILS")))
        self.database = database._dbclient

        self.indexes = {
            "cpe": [
                MongoUniqueIndex(index=[("id", ASCENDING)], name="id", unique=True),
                MongoAddIndex(index=[("vendor", ASCENDING)], name="vendor"),
                MongoAddIndex(index=[("product", ASCENDING)], name="product"),
            ],
            "cpeother": [
                MongoUniqueIndex(index=[("id", ASCENDING)], name="id", unique=True)
            ],
            "cves": [
                MongoAddIndex(index=[("id", ASCENDING)], name="id"),
                MongoAddIndex(
                    index=[("vulnerable_configuration", ASCENDING)],
                    name="vulnerable_configuration",
                ),
                MongoAddIndex(
                    index=[("vulnerable_product", ASCENDING)], name="vulnerable_product"
                ),
                MongoAddIndex(index=[("Modified", ASCENDING)], name="Modified"),
                MongoAddIndex(index=[("Published", ASCENDING)], name="Published"),
                MongoAddIndex(
                    index=[("last-modified", ASCENDING)], name="last-modified"
                ),
                MongoAddIndex(index=[("cvss", ASCENDING)], name="cvss"),
                MongoAddIndex(index=[("cvss3", ASCENDING)], name="cvss3"),
                MongoAddIndex(index=[("summary", TEXT)], name="summary"),
                MongoAddIndex(index=[("vendors", ASCENDING)], name="vendors"),
                MongoAddIndex(index=[("products", ASCENDING)], name="products"),
                MongoAddIndex(
                    index=[("vulnerable_product_stems", ASCENDING)],
                    name="vulnerable_product_stems",
                ),
                MongoAddIndex(
                    index=[("vulnerable_configuration_stems", ASCENDING)],
                    name="vulnerable_configuration_stems",
                ),
            ],
            "via4": [MongoAddIndex(index=[("id", ASCENDING)], name="id")],
            "mgmt_whitelist": [MongoAddIndex(index=[("id", ASCENDING)], name="id")],
            "mgmt_blacklist": [MongoAddIndex(index=[("id", ASCENDING)], name="id")],
            "capec": [
                MongoAddIndex(
                    index=[("related_weakness", ASCENDING)], name="related_weakness"
                )
            ],
        }

        self.logger = logging.getLogger("DatabaseIndexer")

    def getInfo(self, collection):
        return self.sanitize(self.database["info"].find_one({"db": collection}))

    def sanitize(self, x):
        if type(x) == pymongo.cursor.Cursor:
            x = list(x)
        if type(x) == list:
            for y in x:
                self.sanitize(y)
        if x and "_id" in x:
            x.pop("_id")
        return x

    def create_indexes(self, collection=None):

        if collection is not None:
            try:
                for each in self.indexes[collection]:
                    if isinstance(each, MongoUniqueIndex):
                        self.setIndex(
                            collection, each.index, name=each.name, unique=each.unique
                        )
                    elif isinstance(each, MongoAddIndex):
                        self.setIndex(collection, each.index, name=each.name)
            except KeyError:
                # no specific index given, continue
                self.logger.warning(
                    "Could not find the requested collection: {}, skipping...".format(
                        collection
                    )
                )
                pass

        else:
            for index in self.iter_indexes():
                self.setIndex(index[0], index[1])

            for collection in self.indexes.keys():
                for each in self.indexes[collection]:
                    if isinstance(each, MongoUniqueIndex):
                        self.setIndex(
                            collection, each.index, name=each.name, unique=each.unique
                        )
                    elif isinstance(each, MongoAddIndex):
                        self.setIndex(collection, each.index, name=each.name)

    def iter_indexes(self):
        for each in self.get_via4_indexes():
            yield each

    def get_via4_indexes(self):
        via4 = self.getInfo("via4")
        result = []
        if via4:
            for index in via4.get("searchables", []):
                result.append(("via4", index))
        return result

    def setIndex(self, col, field, **kwargs):
        try:
            self.database[col].create_index(field, **kwargs)
            self.logger.info("Success to create index %s on %s" % (field, col))
        except Exception as e:
            self.logger.error("Failed to create index %s on %s: %s" % (col, field, e))
