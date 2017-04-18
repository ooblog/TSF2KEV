#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Trans_Initcards(TSF_cardsD,TSF_cardsO):    #TSF_doc:関数カードにDやPythonに翻訳する命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Trans")
    TSF_Forth_cards={
        "#TSF_Python":TSF_Trans_python, "#デッキのpython化":TSF_Trans_python,
        "#TSF_D-lang":TSF_Trans_dlang, "#デッキのD言語化":TSF_Trans_dlang,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Trans_python():    #TSFdoc:TSFデッキのPython化。1枚[path]ドロー。
    TSF_Trans_generator_python(TSF_Forth_drawthe())
    return ""

def TSF_Trans_dlang():    #TSFdoc:TSFデッキのD言語化。1枚[path]ドロー。
    TSF_Trans_generator_dlang(TSF_Forth_drawthe())
    return ""


def TSF_Trans_generator_python(TSF_tsfpath=None,TSF_pyhonpath=None):    #TSFdoc:TSFデッキのPython化。(TSFAPI)
    TSF_mainandargvs=TSF_Forth_mainandargvs()
    TSF_text,TSF_card="",""
    if os.path.isfile(TSF_tsfpath if TSF_tsfpath != None else ""):
        if len(TSF_Forth_loadtext(TSF_tsfpath,TSF_tsfpath)):
            TSF_Forth_merge(TSF_tsfpath,[],True)
        TSF_text+="#! /usr/bin/env python\n"
        TSF_text+="# -*- coding: UTF-8 -*-\n"
        TSF_text+="from __future__ import division,print_function,absolute_import,unicode_literals\n\n"
        TSF_text+="from TSF_Io import *\n"
        for TSF_import in TSF_Forth_importlist():
            TSF_text+="from {0} import *\n".format(TSF_import)
            TSF_card+="{0}_Initcards,".format(TSF_import)
        TSF_text+="\nTSF_sysargvs=TSF_Io_argvs(sys.argv)\n"
        TSF_text+="TSF_Initcallrun=["+TSF_card.rstrip(',')+"]\n"
        TSF_text+="TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcallrun)\n\n"
#        for TSF_the in TSF_Forth_stackD().keys():
        for TSF_the in TSF_Forth_stackO():
            TSF_text=TSF_Trans_view_python(TSF_the,False,TSF_text)
        TSF_text+="\nTSF_Forth_run()\n"
        if TSF_pyhonpath != None:
            TSF_Io_savetext(TSF_pyhonpath,TSF_text)
        else:
            for TSF_textline in TSF_text.split('\n'):
                TSF_Io_printlog(TSF_textline)

def TSF_Trans_view_python(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSFdoc:スタックの内容をPython風テキスト表示。(TSFAPI)
    if TSF_view_log == None: TSF_view_log=""
    if TSF_the in TSF_Forth_stackD():
        TSF_cards=[TSF_Io_ESCdecode(TSF_card).replace('\\','\\\\').replace('"','\\"').replace('\t','\\t').replace('\n','\\n') for TSF_card in TSF_Forth_stackD()[TSF_the]]
        TSF_style=TSF_Forth_style().get(TSF_the,"T")
        if TSF_style == "O":
            TSF_view_logline='TSF_Forth_setTSF("{0}","\\t".join(["{1}"]),"O")\n'.format(TSF_the,'","'.join(TSF_cards))
        elif TSF_style == "T":
            TSF_view_logline='TSF_Forth_setTSF("{0}","\\t".join([\n    "{1}"]),"T")\n'.format(TSF_the,'","'.join(TSF_cards))
        else:  # TSF_style == "N":
            TSF_view_logline='TSF_Forth_setTSF("{0}","\\t".join([\n    "{1}"]),"N")\n'.format(TSF_the,'",\n    "'.join(TSF_cards))
        TSF_view_log=TSF_Io_printlog(TSF_view_logline,TSF_log=TSF_view_log) if TSF_view_io == True else TSF_view_log+TSF_view_logline
    return TSF_view_log

def TSF_Trans_generator_dlang(TSF_tsfpath=None,TSF_dlangpath=None):    #TSFdoc:TSFデッキのD言語化。(TSFAPI)
    TSF_mainandargvs=TSF_Forth_mainandargvs()
    TSF_text,TSF_card="",""
    if os.path.isfile(TSF_tsfpath if TSF_tsfpath != None else ""):
        if len(TSF_Forth_loadtext(TSF_tsfpath,TSF_tsfpath)):
            TSF_Forth_merge(TSF_tsfpath,[],True)
        TSF_text+="#! /usr/bin/env rdmd\n\n"
        TSF_text+="import std.string;\n\n"
        TSF_text+="import TSF_Io;\n"
        for TSF_import in TSF_Forth_importlist():
            TSF_text+="import {0};\n".format(TSF_import)
            TSF_card+="&{0}_Initcards,".format(TSF_import)
        TSF_text+="\nvoid main(string[] sys_argvs){\n"
        TSF_text+="    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);\n"
        TSF_text+="    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=["+TSF_card.rstrip(',')+"];\n"
        TSF_text+="TSF_Forth_initTSF(TSF_sysargvs[1..$],TSF_Initcallrun);\n\n"
#        for TSF_the in TSF_Forth_stackD().keys():
        for TSF_the in TSF_Forth_stackO():
            TSF_text=TSF_Trans_view_dlang(TSF_the,False,TSF_text)
        TSF_text+="\n    TSF_Forth_run();\n}\n"
        if TSF_dlangpath != None:
            TSF_Io_savetext(TSF_dlangpath,TSF_text)
            pass
        else:
            for TSF_textline in TSF_text.split('\n'):
                TSF_Io_printlog(TSF_textline)

def TSF_Trans_view_dlang(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSFdoc:スタックの内容をD言語風テキスト表示。(TSFAPI)
    if TSF_view_log == None: TSF_view_log=""
    if TSF_the in TSF_Forth_stackD():
        TSF_cards=[TSF_Io_ESCdecode(TSF_card).replace('\\','\\\\').replace('"','\\"').replace('\t','\\t').replace('\n','\\n') for TSF_card in TSF_Forth_stackD()[TSF_the]]
        TSF_style=TSF_Forth_style().get(TSF_the,"T")
        if TSF_style == "O":
            TSF_view_logline='    TSF_Forth_setTSF("{0}",join(["{1}"],"\\t"),"O");\n'.format(TSF_the,'","'.join(TSF_cards))
        elif TSF_style == "T":
            TSF_view_logline='    TSF_Forth_setTSF("{0}",join([\n        "{1}"],"\\t"),"T");\n'.format(TSF_the,'","'.join(TSF_cards))
        else:  # TSF_style == "N":
            TSF_view_logline='    TSF_Forth_setTSF("{0}",join([\n        "{1}"],"\\t"),"N");\n'.format(TSF_the,'",\n        "'.join(TSF_cards))
        TSF_view_log=TSF_Io_printlog(TSF_view_logline,TSF_log=TSF_view_log) if TSF_view_io == True else TSF_view_log+TSF_view_logline
    return TSF_view_log


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
