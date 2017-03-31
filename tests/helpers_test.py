import unittest
from testfixtures import LogCapture
from pentets.helpers import *

class HelpersTest(unittest.TestCase):
    def test_clean_url_with_trailling_slash(self):
        self.assertEqual("/hello", clean_url("/hello/"))

    def test_clean_url_without_trailing_slash(self):
        self.assertEqual("/hello", clean_url("/hello"))

    def test_clean_url_with_root(self):
        self.assertEqual("", clean_url("/"))

    def test_load_rules_logs(self):
        with LogCapture() as l:
            load_rules("")
            l.check(("root", "DEBUG", "Loading rule data"))

    def test_load_rules(self):
        # do something
        pass

    def test_red_empty_string(self):
        self.assertEqual("\x1b[31m\033[0m", red(""))

    def test_red_string(self):
        self.assertEqual("\x1b[31mpatate\033[0m", red("patate"))

    def test_bold_empty_string(self):
        self.assertEqual("\033[1m\033[0m", bold(""))

    def test_bold_string(self):
        self.assertEqual("\033[1mpatate\033[0m", bold("patate"))
