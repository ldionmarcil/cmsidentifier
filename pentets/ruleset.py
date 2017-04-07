import re
import logging
import pdb

from .helpers import *

class Ruleset():
    def __init__(self, target, document):
        self.target = target
        self.document = document
        self.passive_matches = []
        self.active_matches = []

    def passive_match(self):
        return len(self.passive_matches) > 0

    def active_match(self):
        return len(self.active_matches) > 0

    def launch_passive(self, plaintext):
        logging.debug("Launching passive rules for {}".format(self.document.name))

        for heuristic in self.document.passive_rules:
            if re.search(heuristic, plaintext):
                self.passive_matches.append(heuristic)

        if self.passive_match():
            logging.info("{} match for {} ({})".format(bold("Passive"), red(self.document.name), self.document.website))
            logging.info("Resources: {}".format(self.document.resources))
            for m in self.passive_matches:
                logging.info(bold("  ✓ -- {}".format(m)))

        return self.passive_match()

    def launch_active(self, curl_client):
        logging.debug("Launching active rules for {}".format(self.document.name))
        for rule in self.document.active_rules:
            plaintext = str(curl_client.request(self.target + rule['path']))
            matches = re.search(rule['regex'], plaintext)

            # Pattern matched
            if matches:
                logging.info("{} match {}".format(bold("Active"), rule['path']))
                if 'info' in rule:
                    logging.info(" - {}".format(rule['info']))
                # if group matching: data extraction
                if len(matches.groups()) > 0:
                    logging.debug("Dumping extracted...:")

                    for match in matches.groups():
                        if 'desc' in rule:
                            logging.info("{} : {}".format(bold(rule['desc']), match))
                        else:
                            logging.info("Extracted data : {}".format(match))

        return self.active_match()
