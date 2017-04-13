#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import sys
import os
os.chdir(sys.path[0])
sys.path.append('.')
from TSF_Io import *
from TSF_Forth import *


def TSF_sample_help():    #TSF_doc:「sample_help.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["help:","#TSF_argvsthe","#TSF_reverseN","help:","#TSF_lenthe","#TSF_echoN","#TSF_fin."]),"T")
    TSF_Forth_setTSF("help:",
        "\t".join([
        "usage: ./TSF.py [command|file.tsf] [argv] ...",
        "commands & samples:",
        "  --help        this commands view",
        "  --helloworld  \"Hello world  #TSF_echo\" sample",
        "  --RPN         decimal calculator \"1,3/m1|2-\"-> 0.8333... sample",
        ]),"N")
    TSF_sample_run("TSF_sample_help")

def TSF_sample_run(TSF_sample_sepalete=None,TSF_sample_viewthey=None):    #TSF_doc:TSF実行。コマンド実行の場合はソースも表示。
    if TSF_sample_sepalete != None:
        TSF_Io_printlog("-- {0} source --".format(TSF_sample_sepalete))
        TSF_Forth_viewthey()
        TSF_Io_printlog("-- {0} run --".format(TSF_sample_sepalete))
    TSF_Forth_run()
    if TSF_sample_viewthey != None:
        TSF_Io_printlog("-- {0} viewthey --".format(TSF_sample_sepalete))
        TSF_Forth_viewthey()

def TSF_sample_Helloworld():    #TSF_doc:「sample_helloworld.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["Hello world","#TSF_echo"]),"T")
    TSF_sample_run("TSF_sample_Helloworld")

def TSF_sample_RPN():    #TSF_doc:「sample_RPN.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["RPNsetup:","#TSF_this","#TSF_fin."]),"T")
    TSF_Forth_setTSF("RPNsetup:",
        "\t".join(["RPNargvs:","#TSF_that","#TSF_argvs",",","#TSF_sandwichN","RPNjump:","RPNargvs:","#TSF_lenthe","#TSF_peekNthe","#TSF_this"]),"T")
    TSF_Forth_setTSF("RPNjump:",
        "\t".join(["-","RPNdefault:","RPN:"]),"T")
    TSF_Forth_setTSF("RPNdefault:",
        "\t".join(["1,3/m1|2-","RPN:","#TSF_this"]),"T")
    TSF_Forth_setTSF("RPN:",
        "\t".join(["#TSF_RPN","#TSF_echo"]),"T")
    TSF_sample_run("TSF_sample_RPN")


TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Forth_initTSF(TSF_sysargvs[1:],[])
TSF_bootcommand="" if len(TSF_sysargvs) < 2 else TSF_sysargvs[1]
if os.path.isfile(TSF_bootcommand) and len(TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand)):
    TSF_Forth_merge(TSF_bootcommand,[],True)
    TSF_sample_run()
elif TSF_bootcommand in ["--help","--commands"]:
    TSF_sample_help()
elif TSF_bootcommand in ["--hello","--helloworld","--Helloworld"]:
    TSF_sample_Helloworld()
elif TSF_bootcommand in ["--RPN","--rpn"]:
    TSF_sample_RPN()
else:
    TSF_sample_help()
sys.exit(0)


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
