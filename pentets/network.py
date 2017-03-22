import logging
import pycurl
from io import BytesIO


def request(url):
    logging.debug("Network: %s" %url)
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()
