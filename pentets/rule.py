import yaml
import glob
import pdb

class Rule(yaml.YAMLObject):
    yaml_tag = u'!Rule'

    def __init__(self, name):
        self.name = name
        
    def execute(self):
        pass

class Passive(yaml.YAMLObject):
    yaml_tag = u'!Passive'

    def __init__(self, test):
        self.test = test

class Active(yaml.YAMLObject):
    yaml_tag = u'!Active'

    def __init__(self, test):
        self.test = test
            
    
def load_rule(file):
    return yaml.load_all(open(file,'r'))

def load_rules(search_glob):
    return map(load_rule, glob.glob(search_glob))
