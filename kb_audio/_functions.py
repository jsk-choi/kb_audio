import _config as cf
import dbaccess as dal

import urllib.request
from bs4 import BeautifulSoup

def get_html(path):
    #path = urllib.parse.quote(path)
    fp = urllib.request.urlopen(cf.url + path.replace(' ', '%20'))
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def get_audio_href(html):
    soup = BeautifulSoup(html, features="html.parser")
    ret_arr = []

    for a in soup.find_all('a', href=True):
        if str(a['href']).startswith("?dir=audio/"):
            ret_arr.append((a['href'], a.decode_contents()))

    return ret_arr

def audio_href_exists(audio_url):
    return len(dal.audiofiles_select("AudioUrl = '{}'".format(audio_url))) > 0
