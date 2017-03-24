import logging
import pycurl
from io import BytesIO


def request(url, user_agent, proxy):
    logging.debug("Network: %s" %url)
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.FOLLOWLOCATION, True)
    c.setopt(c.USERAGENT, user_agent)
    c.setopt(c.PROXY, proxy)
    c.setopt(c.CONNECTTIMEOUT, 5)
    c.perform()
    c.close()
    return buffer.getvalue()
