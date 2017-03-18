import yaml
import glob
import pdb

class Rule(yaml.YAMLObject):
    yaml_tag = u'!Rule'

    def __init__(self, yaml_obj):
        self.yaml_obj = yaml_obj
        self.name = yaml_obj.name

    def execute(self):
        pass

def load_rule(file):
    return Rule(yaml.load(open(file,'r')))

def load_rules(search_glob):
    return map(load_rule, glob.glob(search_glob))
