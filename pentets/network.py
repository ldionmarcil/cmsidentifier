import logging
import pycurl
from io import BytesIO


def request(url, user_agent):
    logging.debug("Network: %s" %url)
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.FOLLOWLOCATION, True)
    c.setopt(c.USERAGENT, user_agent)
    c.perform()
    c.close()
    return buffer.getvalue()
