import unittest
from io import StringIO
from pentets.report import *

class MockedScan():
    def something(self):
        return "monsieur l'ordinateur"

class ReportTest(unittest.TestCase):
    def test_render_from_file(self):
        report = Report.from_file("./tests/fixtures/fake_layout.txt", MockedScan())
        self.assertEqual("allo: monsieur l'ordinateur", report.render())

    def test_render(self):
        report = Report("asdfg: {{ scan.something() }}", MockedScan())
        self.assertEqual("asdfg: monsieur l'ordinateur", report.render())

    def test_dump(self):
        with StringIO() as out:
            report = Report.from_file("./tests/fixtures/fake_layout.txt", MockedScan())
            report.dump(out)

            self.assertEqual("allo: monsieur l'ordinateur", out.getvalue())
