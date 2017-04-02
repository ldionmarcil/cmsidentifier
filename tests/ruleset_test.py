import unittest
from testfixtures import LogCapture
from pentets.ruleset import *
from pentets.document import load_document

class RulesetTest(unittest.TestCase):
    def setUp(self):
        self.document = load_document("./tests/fixtures/fake.yml")
        self.ruleset = Ruleset("https://google.ca", self.document)

    def test_passive_match(self):
        self.ruleset.passive_matches.append("patate")
        self.assertEqual(True, self.ruleset.passive_match())

    def test_has_no_passive_match(self):
        self.assertEqual(False, self.ruleset.passive_match())

    def test_active_match(self):
        self.ruleset.active_matches.append("patate")
        self.assertEqual(True, self.ruleset.active_match())

    def test_has_no_active_match(self):
        self.assertEqual(False, self.ruleset.active_match())

    def test_launch_passive(self):
        # TODO
        pass

    def test_launch_passive_without_match(self):
        # TODO
        pass

    def test_launch_active(self):
        # TODO
        pass

    def test_launch_active_without_match(self):
        # TODO
        pass
