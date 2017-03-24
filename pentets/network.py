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
    c.setopt(c.USERAGENT, "Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1")
    c.perform()
    c.close()
    return buffer.getvalue()
