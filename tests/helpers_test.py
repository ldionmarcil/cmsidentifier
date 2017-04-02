import unittest
from pentets.helpers import *

class HelpersTest(unittest.TestCase):
    def test_clean_url_with_trailling_slash(self):
        self.assertEqual("/hello", clean_url("/hello/"))

    def test_clean_url_without_trailing_slash(self):
        self.assertEqual("/hello", clean_url("/hello"))

    def test_clean_url_with_root(self):
        self.assertEqual("", clean_url("/"))

    def test_red_empty_string(self):
        self.assertEqual("\x1b[31m\033[0m", red(""))

    def test_red_string(self):
        self.assertEqual("\x1b[31mpatate\033[0m", red("patate"))

    def test_bold_empty_string(self):
        self.assertEqual("\033[1m\033[0m", bold(""))

    def test_bold_string(self):
        self.assertEqual("\033[1mpatate\033[0m", bold("patate"))

    def test_cyan_empty_string(self):
        self.assertEqual("\x1b[36m\033[0m", cyan(""))

    def test_cyan_string(self):
        self.assertEqual("\x1b[36mpatate\033[0m", cyan("patate"))
