import logging
import pdb

from .document import load_documents
from .ruleset import Ruleset
from .helpers import clean_url, red, bold

class Scan():
    def __init__(self, targets, rules_dir, curl_client, active=False, jobs=1):
        self.targets = targets
        self.rules_dir = rules_dir
        self.curl_client = curl_client
        self.active = active
        self.jobs = jobs

    def scan(self):
        documents = load_documents(self.rules_dir)
        # TODO: multi-targets
        self.scan_target(clean_url(self.targets), documents)

    def scan_target(self, target, documents):
        if not documents:
            documents = []

        plaintext = str(self.curl_client.request(target))

        for document in documents:
            ruleset = Ruleset(target, document)

            if ruleset.launch_passive(plaintext):
                if self.active:
                    ruleset.launch_active(self.curl_client)

                # bail on first passive rule
                break

    def generate_report(self):
        pass
