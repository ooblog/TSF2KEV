#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import random
import re
from TSFpy_Io import *

def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945"

def TSF_Forth_Initcards(TSF_cards):    #TSF_doc:ワードを初期化する(TSFAPI)。
#    TSF_cards["#TSF_fin."]=TSF_Forth_fin; TSF_cards["#TSFを終了。"]=TSF_Forth_fin
#    TSF_cards["#TSF_viewthey"]=TSF_Forth_viewthey; TSF_cards["#スタック一覧を表示"]=TSF_Forth_viewthey
#    TSF_cards["#TSF_RPN"]=TSF_Forth_RPN; TSF_cards["#逆ポーランド電卓で計算"]=TSF_Forth_RPN
    return TSF_cards


TSF_Initcalls=[]
TSF_stacks,TSF_styles,TSF_callptrs,TSF_cards=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
def TSF_Forth_init(TSF_argvs=[],TSF_addcalls=[]):    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
    global TSF_stacks,TSF_styles,TSF_callptrs,TSF_cards,TSF_Initcalls,TSF_stackthat,TSF_stackthis,TSF_stackcount,TSF_stackargvs
    TSF_stacks,TSF_styles,TSF_callptrs,TSF_words=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
    TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
    TSF_stacks[TSF_stackthis]=["0","#TSF_fin."]; #TSF_Forth_addfin(TSF_argvs)
    TSF_stackargvs=deque(TSF_argvs); TSF_stackargvs.popleft()
    TSF_Initcalls=[TSF_Forth_Initcards]+TSF_addcalls
    for TSF_Initcall in TSF_Initcalls:
        TSF_words=TSF_Initcall(TSF_words)



def TSF_Io_debug(TSF_argvs):    #TSFdoc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyForth.log";
    print("--- {0} ---".format(__file__))
    TSF_Forth_init([TSF_Forth_Initcards])
 #   TSF_Forth_init(TSF_argvs,[TSF_Forth_Initwords])
 #   TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","0","#TSF_fin."]))
#    TSF_Forth_setTSF("TSF_Forth.py:","\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout]))
#    TSF_Forth_setTSF("TSF_words:","\t".join(TSF_words.keys()))
#    TSF_Forth_addfin(TSF_argvs)
#    TSF_Forth_run()
#    for TSF_thename in TSF_Forth_stackskeys():
#        TSF_debug_log=TSF_Forth_view(TSF_thename,True,TSF_debug_log)
    print("--- fin. > {0} ---".format(TSF_debug_savefilename))
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log


if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(sys.argv))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
