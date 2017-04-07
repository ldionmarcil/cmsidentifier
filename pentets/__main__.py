import logging
import fileinput
import os
import pdb
import argparse

from .scan import Scan
from .network import CurlClient
from .version import __version__

def run():
    root_path = os.path.dirname(os.path.realpath(__file__)) + "/.."
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        metavar="URL",
                        help="Root URL to scan")
    parser.add_argument('-i', '--inplace',
                        action='store_true',
                        help="Specifies a list of targets from a file")
    parser.add_argument('-o', '--output',
                        type=argparse.FileType('w'),
                        help="The path to the report to produce, if desired")
    parser.add_argument('-a', '--active',
                        action="store_true",
                        help="Trigger active rules if passive rules are a match")
    parser.add_argument('-r', '--rules',
                        nargs=1, type=str, metavar="DIRECTORY",
                        default=(root_path + "/rules/*.yml"),
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
    parser.add_argument('-j', '--jobs',
                        type=int, metavar="JOBS",
                        default=1,
                        help="Maximum number of parallel scan jobs. The default is 1.")
    parser.add_argument('-l', '--layout',
                        nargs=1, type=str, metavar="URL",
                        help="The path of the layout used to generate the reports",
                        default=(root_path + "/layouts/default.html"))

    arguments = parser.parse_args()


    logging.basicConfig(format="[%(asctime)s %(levelname)-5s] %(message)s",
                        level=logging.DEBUG if arguments.verbose else logging.INFO)


    curl_client = CurlClient(user_agent=arguments.user_agent, proxy=arguments.proxy)

    # multiple_urls = None
    multiple_urls = [line.rstrip() for line in fileinput.input(arguments.inplace)]
    targets = arguments.url or multiple_urls

    if not targets:
        parser.print_help();
        return

    scan = Scan(targets=targets,
                rules_dir=arguments.rules,
                curl_client=curl_client,
                active=arguments.active,
                jobs=arguments.jobs)

    scan.scan()
    scan.generate_report(arguments.layout, arguments.output)

if __name__ == '__main__':
    run()
