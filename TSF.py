#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import sys
import os
os.chdir(sys.path[0])
sys.path.append('.')
from TSF_Io import *
from TSF_Forth import *


def TSF_sample_Helloworld():    #TSF_doc:Helloworldサンプル(「Hello world」を表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["Hello world","#TSF_echo"]),TSF_style="T")
    TSF_sample_run("TSF_sample_Helloworld")

def TSF_sample_run(TSF_sample_sepalete=None):    #TSF_doc:TSFサンプルプログラム実行。
    if TSF_sample_sepalete != None:
        TSF_Io_printlog("-- {0} source --".format(TSF_sample_sepalete))
        TSF_Forth_viewthey()
        TSF_Io_printlog("-- {0} run --".format(TSF_sample_sepalete))
    TSF_Forth_run()


TSF_argvs=TSF_Io_argvs(sys.argv)
TSF_bootcommand="" if len(TSF_argvs) < 2 else TSF_argvs[1]
TSF_Forth_initTSF(TSF_argvs,[])
if os.path.isfile(TSF_bootcommand):
    pass
#    if len(TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand)):
#        TSF_Forth_merge(TSF_bootcommand,[])
#        TSF_Forth_mainfile(TSF_mergefile)
#        TSF_sample_run()
elif TSF_bootcommand in ["--hello","--helloworld","--Helloworld"]:
    TSF_sample_Helloworld()
#elif TSF_mergefile in ["--about"]:
#    TSF_sample_about()
else:  #TSF_mergefile in ["--help"]:
#    TSF_sample_help()
    TSF_sample_Helloworld()
sys.exit(0)


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
