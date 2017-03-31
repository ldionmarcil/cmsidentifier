import logging
import pdb

from .network import *
from .documents import Passive, Active, Info
from .ruleset import *
from .helpers import *

class Scan():
    matches = []

    def __init__(self, target, rules, user_agent, active, proxy):
        logging.info("Scanning {}".format(target))
        # Extract scan options to self
        self.target = clean_url(target)
        self.user_agent = user_agent
        self.active = active
        self.proxy = proxy
        self.rules = load_rules(rules)
        self.plaintext = str(request(self.target, self.user_agent, self.proxy))

    def process_rules(self):
        for ruledata in self.rules:
            ruleset = Ruleset(self, ruledata)
            ruleset.launch_passive()

            # Passive rules are a match
            if ruleset.passive_match():

                logging.info("Passive match for {} ({})".format(red(ruleset.info.name), ruleset.info.website))
                logging.info("Resources: {}\n".format(ruleset.info.resources))
                # If active rules are needed
                if self.active:
                    ruleset.launch_active()

                # Passive rule match, don't bother with other rules
                break


    def generate_report(self):
        pass
