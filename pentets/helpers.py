from documents import *
import logging

def clean_url(url):
    # remove trailing slash
    if url[-1:] == '/':
        url = url[:-1]
    return url

def load_rules(path):

    logging.debug("Loading rule data")

    rule_files = load_documents(path + "/*.yml")

    return rule_files
    
    
def bold(str):
    return "\033[1m{}\033[0m".format(str)
