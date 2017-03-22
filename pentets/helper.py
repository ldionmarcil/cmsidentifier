def clean_url(url):
    # remove trailing slash
    if url[-1:] == '/':
        url = url[:-1]
    return url
