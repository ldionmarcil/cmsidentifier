import re
import logging
from documents import Passive, Active, Info

class Ruleset():
    def __init__(self, scan, ruleset):
        self.scan=scan
        self.unpack_documents(ruleset)

    def execute(self):
        for heuristic in self.passive_rules:
            match = re.search(heuristic, self.scan.plaintext)
            if match:
                logging.info("Match found for %s (%s)!" % (self.info.name, self.info.website))

        
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
