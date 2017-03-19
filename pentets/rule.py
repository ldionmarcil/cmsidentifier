import yaml
import glob
import pdb

class Info(yaml.YAMLObject):
    yaml_tag = u'!Info'

    def __init__(self, name):
        self.name = name
        
class Passive(yaml.YAMLObject):
    yaml_tag = u'!Passive'

    def __init__(self, test):
        self.test = test

class Active(yaml.YAMLObject):
    yaml_tag = u'!Active'

    def __init__(self, test):
        self.test = test

    def execute(self):
        pass


def load_rule(file):
    return yaml.load_all(open(file,'r'))

def load_rules(search_glob):
    return map(load_rule, glob.glob(search_glob))
