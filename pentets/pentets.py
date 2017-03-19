import os
import pdb
import argparse
from scan import *
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

    rule_files = load_rules(RULE_FOLDER + "/*.yml")



    # Every rule file gets a scan
    for rules in rule_files:
        scan = Scan(rules=rules, target=arguments.url, report=arguments.output)

        # Rules returned a match
        if scan.match == True:

            #Generate report
            scan.generate_report()
            
    

if __name__ == '__main__':
    run()
