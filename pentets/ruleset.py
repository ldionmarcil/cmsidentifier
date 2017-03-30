import re
import logging

from .network import *
from .helpers import *
from .documents import Passive, Active, Info

class Ruleset():
    # By default nothing matches
    passive_matches = []

    def __init__(self, scan, ruleset):
        self.scan=scan
        self.unpack_documents(ruleset)

    # Returns true if matches one or more passive rules
    def passive_match(self):
        return (len(self.passive_matches) > 0)

    def launch_passive(self):
        logging.debug("Launching passive rules for {}".format(self.info.name))
        for heuristic in self.passive_rules:
            if re.search(heuristic, self.scan.plaintext):
                logging.debug("Match on {}".format(heuristic))
                self.passive_matches.append(heuristic)

    def launch_active(self):
        logging.debug("Launching active rules for {}".format(self.info.name))
        for rule in self.active_rules:
            plaintext = str(request(self.scan.target + rule['path'],
                                    self.scan.user_agent,
                                    self.scan.proxy))

            matches = re.search(rule['regex'], plaintext)

            # Pattern matched
            if matches:
                logging.info("Active {} match".format(rule['path']))
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


    def unpack_documents(self, ruleset):
        logging.debug('Unpacking YAML documents')
        for document in ruleset:
            # Extract rule information
            if type(document) is Info:
                self.info = document

            # Extract passive rules
            if type(document) is Passive:
                self.passive_rules = document

            # Extract active rules
            if type(document) is Active:
                self.active_rules = document
