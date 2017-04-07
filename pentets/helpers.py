def clean_url(url):
    # remove trailing slash
    if url[-1:] == '/':
        url = url[:-1]
    return url

def bold(str):
    return "\033[1m{}\033[0m".format(str)

def red(str):
    return  "\x1b[31m{}\033[0m".format(str)

def cyan(str):
    return  "\x1b[36m{}\033[0m".format(str)
