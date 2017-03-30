import unittest
import pdb
from pentets.documents import *

class DocumentsTest(unittest.TestCase):
    def test_load_info(self):
        info = yaml.load("""\
--- !Info
name: perdu
website: https://perdu.com/
resources: https://perdu.org/
""")

        self.assertEqual("perdu", info.name)
        self.assertEqual("https://perdu.com/", info.website)
        self.assertEqual("https://perdu.org/", info.resources)

    def test_load_passive(self):
        passive = yaml.load("""\
--- !Passive
regexes:
- /yolo/
- /patate/i
""")

        self.assertEqual(2, passive.count())
        self.assertEqual(["/yolo/", "/patate/i"], list(passive))

    def test_passive_defaults(self):
        self.assertEqual([], Passive.regexes)

    def test_load_active(self):
        active = yaml.load("""\
--- !Active
entries:
  - path: /readme.html
    desc: patatepress Version
    regex: <br /> Version ([0-9.]+)
""")

        self.assertEqual(1, active.count())
        self.assertEqual([{
            "path": "/readme.html",
            "desc": "patatepress Version",
            "regex": "<br /> Version ([0-9.]+)"
        }], list(active))

    def test_active_defaults(self):
        self.assertEqual([], Active.entries)

    def test_load_document(self):
        document = load_document("./tests/fixtures/fake.yml")
        self.assertEqual(3, len(list(document)))

    def test_load_documents(self):
        documents = load_documents("./tests/*/fake.yml")
        self.assertEqual(1, len(list(documents)))
