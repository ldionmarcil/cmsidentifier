import re
import network
import logging
from documents import Passive, Active, Info

class Ruleset():
    # By default nothing matches
    match = False

    def __init__(self, scan, ruleset):
        self.scan=scan
        self.unpack_documents(ruleset)

    def launch_passive(self):
        logging.debug("Launching passive rules for %s" % self.info.name)
        for heuristic in self.passive_rules:
            if re.search(heuristic, self.scan.plaintext):
                self.match = True

    def launch_active(self):
        logging.debug("Launching active rules for %s" % self.info.name)
        for rule in self.active_rules:
            plaintext = str(network.request(self.scan.target + rule['path']))

            matches = re.search(rule['regex'], plaintext)

            # Pattern matched
            if matches:
                logging.info("Active %s match" % rule['path'])

                # if group matching: data extraction
                if len(matches.groups()) > 0:
                    logging.debug("Dumping extracted...:")

                    for match in matches.groups():
                        logging.info("Exracted: %s" % match)
            

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
