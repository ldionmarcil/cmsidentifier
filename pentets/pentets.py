import os
import pdb
import argparse
from rule import *

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', metavar="URL", help="Root URL to scan", required=True)
    parser.add_argument('-f', '--cms-family', metavar="FAMILY", help="The family of the CMS to scan for")
    parser.add_argument('-o', '--output', nargs=1, type=str, metavar="URL", help="The path to the report to produce, if desired")
    parser.add_argument('-r', '--rules', nargs=1, type=str, metavar="DIRECTORY", help="The path to the directory where rules reside")
    arguments = parser.parse_args()


    if arguments.rules is not None:
        RULE_FOLDER = arguments.rules[0]
    else:
        RULE_FOLDER = os.path.dirname(os.path.realpath(__file__)) + "/../rules"

    rules = load_rules(RULE_FOLDER + "/*.yml")

    for rule in rules:
        print("Executing rule %s" % (rule.name))
        rule.execute()

if __name__ == '__main__':
    run()
