import logging
import pdb
from pathlib import Path

from .document import load_documents
from .report import Report
from .ruleset import Ruleset
from .helpers import clean_url, red, bold, cyan

class Scan():
    def __init__(self, targets, rules_dir, curl_client, active=False, jobs=1):
        if not isinstance(targets, list):
            self.targets = [targets]
        else:
            self.targets = targets
        self.rules_dir = rules_dir
        self.curl_client = curl_client
        self.active = active
        self.jobs = jobs
        self.succeded_rulesets = []

    def scan(self):
        documents = list(load_documents(self.rules_dir))
        for target in self.targets:

            self.scan_target(clean_url(target), documents)

    def scan_target(self, target, documents):
        logging.info("Scanning {}".format(cyan(target)))
        if not documents:
            documents = []

        plaintext = str(self.curl_client.request(target))
        found = False

        rulesets = [Ruleset(target, document) for document in documents]

        for ruleset in rulesets:
            if ruleset.launch_passive(plaintext):
                found = True
                self.succeded_rulesets.append((target, ruleset))
                if self.active:
                    ruleset.launch_active(self.curl_client)

                # bail on first passive rule
                break
        else:
            logging.info(red("  𝙭 -- no rule matched"))

    def generate_report(self, layout, destination):
        if not Path(layout).is_file():
            logging.error("{} is not a valid layout file".format(layout))
            return

        if not destination:
            logging.info("Use the `-o PATH` option to generate a report")
            return

        report = Report.from_file(layout, self)
        report.dump(destination)
