import yaml
import glob

class Rule(yaml.YAMLObject):
    yaml_tag = u'!Rule'

    def __init__(self, name):
        self.name = name

    def execute(self):
        pass

def load_rule(file):
    return Rule(yaml.load(file))

def load_rules(search_glob):
    return map(load_rules, glob.glob(search_glob))
