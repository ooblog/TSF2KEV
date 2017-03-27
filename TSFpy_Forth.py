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


def TSF_Io_debug(TSF_argvs):    #TSFdoc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyForth.log";
    print("--- {0} ---".format(__file__))
    print("--- fin. > {0} ---".format(TSF_debug_savefilename))
#    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log


if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(sys.argv))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
