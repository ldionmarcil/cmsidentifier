import unittest
import pdb
from pentets.document import *

class DocumentTest(unittest.TestCase):
    def test_load_info(self):
        doc = yaml.load("""\
--- !Document
name: perdu
website: https://perdu.com/
resources: https://perdu.org/
passive_rules:
  - /yolo/
  - /patate/i
active_rules:
  - path: /readme.html
    desc: patatepress Version
    regex: <br /> Version ([0-9.]+)
""")

        self.assertEqual("perdu", doc.name)
        self.assertEqual("https://perdu.com/", doc.website)
        self.assertEqual("https://perdu.org/", doc.resources)
        self.assertEqual(1, len(doc.active_rules))
        self.assertEqual(2, len(doc.passive_rules))
        self.assertEqual(len(doc.active_rules), doc.active_rules_count())
        self.assertEqual(len(doc.passive_rules), doc.passive_rules_count())

    def test_load_document(self):
        document = load_document("./tests/fixtures/fake.yml")
        self.assertEqual("Testpress", document.name)

    def test_load_documents(self):
        documents = list(load_documents("./tests/*/fake.yml"))
        self.assertEqual(1, len(documents))
        self.assertEqual("Testpress", documents[0].name)
