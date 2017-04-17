#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *
from TSF_Trans import *

TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Trans_Initcards]
TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcallrun)

TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
    "Hello world","#TSF_echo"]),"T")

TSF_Forth_run()
