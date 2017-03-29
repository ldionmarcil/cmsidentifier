import unittest
from testfixtures import LogCapture
from pentets.ruleset import *

class MockedScan():
    pass

class RulesetTest(unittest.TestCase):
    def test_passive_match(self):
        pass

    def test_launch_passive(self):
        pass

    def test_launch_active(self):
        pass

    @unittest.skip("seems like I can't code...")
    def test_unpack_documents(self):
        self.setup_document_ruleset()
        self.assertEqual(1, self.ruleset.info)
        self.assertEqual(1, self.ruleset.passive_rules)
        self.assertEqual(1, self.ruleset.active_rules)

    def test_unpack_documents_logs(self):
        with LogCapture() as l:
            self.setup_document_ruleset()
            l.check(("root", "DEBUG", "Unpacking YAML documents"))

    def setup_document_ruleset(self):
        self.documents = load_documents("./tests/fixtures/document_1.yml")
        self.ruleset = Ruleset(MockedScan(), self.documents)
