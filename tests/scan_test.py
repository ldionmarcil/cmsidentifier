import unittest
from pentets.scan import Scan
from pentets.document import load_document

class MockedCurlClient():
    def __init__(self, response):
        self.response = response

    def request(self, *args):
        return self.response

class ScanTest(unittest.TestCase):
    def setUp(self):
        self.target = "http://phoenix.etsmtl.ca/"
        self.rules_dir = "./tests/fixtures/fake.yml"
        self.fake_document = load_document("./tests/fixtures/fake.yml")

    def test_scan_passive_match(self):
        pass

    def test_scan_active_match(self):
        pass

    def test_scan_multiple_passive_match(self):
        pass

    def test_scan_mutliple_active_match(self):
        pass

    def test_scan_target_no_document(self):
        scan = Scan([self.target], self.rules_dir, MockedCurlClient(""))
        scan.scan_target(self.target, None)

    def test_scan_target_no_target(self):
        scan = Scan([self.target], self.rules_dir, MockedCurlClient(""))
        scan.scan_target(None, [self.fake_document])

    def test_scan_target_no_match(self):
        scan = Scan([self.target], self.rules_dir, MockedCurlClient(""))
        scan.scan_target(self.target, [self.fake_document])

    def test_scan_target_match_passive(self):
        pass

    def test_scan_target_match_active(self):
        pass

    def test_generate_report(self):
        pass

    def test_generate_report_invalid_destination(self):
        pass
