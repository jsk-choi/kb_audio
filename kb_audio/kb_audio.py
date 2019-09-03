import sys
import dbsetup
import dbaccess as dal

import _config as cf
import _functions as fn

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

    print(audio_ahref)
