import logging
import os
import pdb
import argparse

from .scan import *
from .helpers import *
from .version import __version__

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        metavar="URL", required=True,
                        help="Root URL to scan")
    parser.add_argument('-f', '--cms-family',
                        metavar="FAMILY",
                        help="The family of the CMS to scan for")
    parser.add_argument('-o', '--output',
                        nargs=1, type=str, metavar="URL",
                        help="The path to the report to produce, if desired")
    parser.add_argument('-a', '--active',
                        action="store_true",
                        help="Trigger active rules if passive rules are a match")
    parser.add_argument('-r', '--rules',
                        nargs=1, type=str, metavar="DIRECTORY",
                        default=os.path.dirname(os.path.realpath(__file__)) + "/../rules",
                        help="The path to the directory where rules reside")
    parser.add_argument('-U', '--user-agent',
                        type=str, metavar="USER AGENT",
                        default="Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
                        help="Network requests will be made with this User-Agent")
    parser.add_argument('-v', '--version',
                        action="version",
                        version='PentETS {version}'.format(version=__version__))
    parser.add_argument('-p', '--proxy',
                        type=str, metavar="PROXY", default="",
                        help="Proxy in the format of proto://host:port")
    parser.add_argument('-V', '--verbose',
                        action="store_true",
                        help="Enable debugging output")

    arguments = parser.parse_args()

    logging.basicConfig(format="[%(asctime)s %(levelname)-5s] %(message)s",
                        level=logging.DEBUG if arguments.verbose else logging.INFO)

    scan = Scan(target=arguments.url,
                rules=load_rules(arguments.rules),
                user_agent=arguments.user_agent,
                proxy=arguments.proxy,
                active=arguments.active)

    scan.generate_report()

if __name__ == '__main__':
    run()
