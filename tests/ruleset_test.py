import unittest
from testfixtures import LogCapture
from pentets.ruleset import *

class MockedScan():
    pass

class RulesetTest(unittest.TestCase):
    def setUp(self):
        self.documents = load_documents("./tests/fixtures/fake.yml")
        self.ruleset = Ruleset(MockedScan(), self.documents)

    def test_passive_match(self):
        self.ruleset.passive_matches.append("patate")
        self.assertEqual(True, self.ruleset.passive_match())

    def test_has_no_passive_match(self):
        self.assertEqual(False, self.ruleset.passive_match())

    def test_launch_passive(self):
        pass

    def test_launch_active(self):
        pass
