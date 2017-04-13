#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Trans_Initcards(TSF_cardsD,TSF_cardsO):    #TSF_doc:関数カードにDやPythonに翻訳する命令を追加する。(TSFAPI)
    TSF_Forth_cards={
        "#TSF_Python":TSF_Trans_python, "#デッキのpython化":TSF_Trans_python,
        "#TSF_D-lang":TSF_Trans_dlang, "#デッキのD言語化":TSF_Trans_dlang,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Trans_python():    #TSFdoc:TSFデッキのPython化。1枚[path]ドロー。
    TSF_Trans_python(TSF_Forth_drawthe())
    return ""

def TSF_Trans_dlang():    #TSFdoc:TSFデッキのD言語化。1枚[path]ドロー。
    return ""


def TSF_Trans_python(TSF_tsfpath=None,TSF_pyhonpath=None):    #TSFdoc:TSFデッキのPython化。(TSFAPI)
    TSF_mainandargvs=TSF_Forth_mainandargvs()
    print("TSF_tsfpath",TSF_tsfpath,TSF_pyhonpath)
    TSF_text=""

#def TSF_Forth_writesamplepy(TSF_tsfpath=None,TSF_pyhonpath=None):   #TSF_doc:[filename,stack]スタック全体をpythonとみなして.pyに保存する(TSFAPI)。
#    TSF_text=""
#    if os.path.isfile(TSF_tsfpath if TSF_tsfpath != None else ""):
#        if len(TSF_Forth_loadtext(TSF_tsfpath,TSF_tsfpath)):
#            TSF_Forth_merge(TSF_tsfpath,[],TSF_mergedel=True)
#            TSF_appendtext=TSF_txt_ESCdecode("\t{0}\t".format("\t".join(TSF_stacks[TSF_Forth_1ststack()])))
#            TSF_appendtags=re.findall(re.compile("\\t[:a-zA-Z0-9_\/\\\\]*?\\t#TSF_viewpythonappend\\t",re.MULTILINE),TSF_appendtext)
#            if len(TSF_appendtags):
#                TSF_Forth_writesamplepyappend(TSF_appendtags[0].replace("\t#TSF_viewpythonappend","").strip('\t'))
#    TSF_text+="#! /usr/bin/env python\n"
#    TSF_text+="# -*- coding: UTF-8 -*-\n"
#    TSF_text+="from __future__ import division,print_function,absolute_import,unicode_literals\n\n"
#    TSF_text+="import sys\nimport os\nos.chdir(sys.path[0])\nsys.path.append('{0}')\n".format(TSF_Forth_writesamplepyappend())
#    TSF_text+="from TSF_io import *\n"
#    TSF_text+="#from TSF_Forth import *\n"
#    TSF_importlist=["TSF_shuffle","TSF_match","TSF_uri","TSF_calc","TSF_time"]
#    for TSF_import in TSF_importlist:
#        TSF_text+="from {0} import *\n".format(TSF_import)
#    TSF_text+="\n"
#    TSF_text+="TSF_Forth_init(TSF_io_argvs(),[TSF_shuffle_Initwords,TSF_match_Initwords,TSF_uri_Initwords,TSF_calc_Initwords,TSF_time_Initwords])\n\n"
#    for TSF_thename in TSF_stacks.keys():
#        TSF_text=TSF_Forth_samplingpy(TSF_thename,False,TSF_text)
#    TSF_text+="\nTSF_Forth_addfin(TSF_io_argvs())\nTSF_Forth_argvsleftcut(TSF_io_argvs(),1)\nTSF_Forth_mainfile(TSF_io_argvs()[0])\nTSF_Forth_run()"
#    if TSF_pyhonpath != None:
#        TSF_io_savetext(TSF_pyhonpath,TSF_text=TSF_text)
#    else:
#        for TSF_textline in TSF_text.split('\n'):
#            TSF_io_printlog(TSF_textline)




TSF_Initcalldebug=[TSF_Forth_Initcards]
def TSF_Trans_debug(TSF_sysargvs):    #TSFdoc:「TSF_Trans」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Trans.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Trans_debug(TSF_Io_argvs(["python","TSF_Trans.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
