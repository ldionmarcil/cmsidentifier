import unittest

class PentetsTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

# -u https://herby.tv/
# [2017-03-20 13:45:56,647 DEBUG] Loading rule data
# [2017-03-20 13:45:58,788 DEBUG] Unpacking YAML documents
# [2017-03-20 13:45:58,793 DEBUG] Launching passive rules for Wordpress
# [2017-03-20 13:45:58,794 INFO] Match for Wordpress (https://wordpress.com/)

# -u http://phoenix.etsmtl.ca/ -a
# [2017-03-21 21:42:35,729 INFO] Match for Wordpress (https://wordpress.com/)
# [2017-03-21 21:42:36,114 INFO] Active /readme.html match
# [2017-03-21 21:42:36,114 INFO] Exracted: 4.3.9
# [2017-03-21 21:42:36,567 INFO] Active /license.txt match
# [2017-03-21 21:42:36,567 INFO] Exracted: Copyright 2017 by the contributors
