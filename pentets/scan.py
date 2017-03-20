import network
import logging
from documents import Passive, Active, Info
from ruleset import *
import pdb


class Scan():
    passive_rules = Passive()
    active_rules = Active()

    matches = []
    
    def __init__(self, target, rules, active):
        # Extract scan options to self
        self.target = target

        self.plaintext = str(network.request(target))

        for ruledata in rules:
            ruleset = Ruleset(self, ruledata)
            ruleset.launch_passive()

            # Passive rules are a match
            if ruleset.match:
                logging.info("Match for %s (%s)" % (ruleset.info.name, ruleset.info.website))

                # If active rules are needed
                if active:
                    logging.debug("Passive rules matched and active rules flag present")
                    ruleset.launch_active()

                # Passive rule match, don't bother with other rules
                break
        
    def perform(self):
        pdb.set_trace()
        logging.info('Starting rule "%s"' %(self.info.name))
        logging.info('Heuristics loaded')
        logging.info(' - %d passive rules' % self.passive_rules.count())
        logging.info(' - %d active rules' % self.active_rules.count())



    def generate_report(self):
        pass
