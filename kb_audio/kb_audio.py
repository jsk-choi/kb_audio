import sys
import dbsetup
import dbaccess as dal

import _config as cf
import _functions as fn

import requests as req
import urllib

all_audio = fn.get_audio_href(fn.get_html(''))

# EMPTY DB, RUN FOR FIRST TIME
if len(dal.audiofiles_select('1 = 1')) == 0:
    
    for audio in all_audio:
        dal.audiofiles_insert(audio[0], audio[1])
        
    for audio in dal.audiofiles_select('1 = 1'):
        print("{0} :: {1}".format(audio[0], audio[2]))

    print("Enter number to download:")
    audio_no = int(input())

    audio_dl = dal.audiofiles_select("Id = {0}".format(audio_no))[0]

    audio_html = fn.get_html(audio_dl[1])
    audio_ahref = fn.get_audio_href(audio_html)

    for mp3 in audio_ahref:
        
        mp3_url = cf.url + mp3[0]
        r = req.get(mp3_url, allow_redirects=True)
        print(r.content)
        
        urllib.request.urlretrieve(mp3_url, mp3[0])

        #mp3_url = cf.url + mp3[0].replace(' ', '%20')

        #print(mp3_url)
        #print('')
        #print('')

        ## http://www.kevinandbeanarchive.com/audio.php?dir=audio/------August%2030%20Friday------&file=12b%20What`s%20Happening-2019-08-30-9%20am.mp3

        #mp3_url_real = url.urlopen(mp3_url)
        
        #for mp3_path in mp3_url_real:
        #    print(mp3_path)

        #    response = urllib2.urlopen('http://www.example.com/')
        #    html = response.read()

        #print('')
        #print('')
        #print('')
        