import _config as cf
import urllib.request


def get_html():
    fp = urllib.request.urlopen(cf.url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    print(mystr)

    beautiful
