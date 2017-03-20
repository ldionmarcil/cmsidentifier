import network
import logging
import os
import pdb
import argparse
from scan import *
from documents import *

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

    logging.debug("Loading rule data")
    rule_files = load_documents(RULE_FOLDER + "/*.yml")

    
    scan = Scan(target=arguments.url, rules=rule_files)
    scan.generate_report()
            
    

if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(levelname)s] %(message)s",
                        level=logging.DEBUG)
    run()
