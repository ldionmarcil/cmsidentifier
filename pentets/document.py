import yaml
import glob

class Document(yaml.YAMLObject):
    yaml_tag = u'!Document'

    active_rules = []
    passive_rules = []

    def active_rules_count(self):
        return len(self.active_rules)

    def passive_rules_count(self):
        return len(self.passive_rules)

def load_document(file):
    with open(file, 'r') as stream:
        return yaml.load(stream.read())

def load_documents(search_glob):
    return map(load_document, glob.glob(search_glob))
