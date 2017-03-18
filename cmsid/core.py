import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', metavar="URL", help="Root URL to scan", required=True)
parser.add_argument('-f', '--cms-family', metavar="FAMILY", help="The family of the CMS to scan for")
parser.add_argument('-o', '--output', nargs=1, type=str, metavar="URL", help="The path to the report to produce, if desired")
parser.add_argument('-r', '--rules', nargs=1, type=str, metavar="DIRECTORY", help="The path to the directory where rules reside")
args = parser.parse_args()

print(args.url)
print(args.report)
