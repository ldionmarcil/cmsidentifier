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

    def __init__(self, target, rules, user_agent, active, proxy):
        logging.info("Scanning {}".format(target))
        # Extract scan options to self
        self.target = clean_url(target)
        self.user_agent = user_agent

        self.plaintext = str(network.request(target,
                                             self.user_agent,
                                             proxy))

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

    def generate_report(self):
        pass
