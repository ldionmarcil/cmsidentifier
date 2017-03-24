import network
import logging
from documents import Passive, Active, Info
from ruleset import *
from helpers import *
import pdb


class Scan():
    passive_rules = Passive()
    active_rules = Active()

    matches = []
    
    def __init__(self, target, rules, active):
        logging.info("Scanning {}".format(target))
        # Extract scan options to self
        self.target = clean_url(target)

        self.plaintext = str(network.request(target))

        for ruledata in rules:
            ruleset = Ruleset(self, ruledata)
            ruleset.launch_passive()

            # Passive rules are a match
            if ruleset.passive_match():
                
                logging.info("Passive match for \x1b[31m{}\033[0m ({})".format(ruleset.info.name, ruleset.info.website))
                logging.info("Resources: {}\n".format(ruleset.info.resources))
                # If active rules are needed
                if active:
                    ruleset.launch_active()

                # Passive rule match, don't bother with other rules
                break
        
    def perform(self):
        pdb.set_trace()
        logging.info('Starting rule "{}"'.format(self.info.name))
        logging.info('Heuristics loaded')
        logging.info(' - {} passive rules'.format(self.passive_rules.count()))
        logging.info(' - {} active rules'.format(self.active_rules.count()))



    def generate_report(self):
        pass
