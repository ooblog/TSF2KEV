#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *
from TSF_Shuffle import *
from TSF_Calc import *
from TSF_Time import *
from TSF_Urlpath import *
from TSF_Match import *
from TSF_Trans import *

TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Shuffle_Initcards,TSF_Calc_Initcards,TSF_Time_Initcards,TSF_Urlpath_Initcards,TSF_Match_Initcards,TSF_Trans_Initcards]
TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcallrun)
TSF_Forth_mainfilepath(os.path.abspath(__file__))

TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
    "quine_echo:","#TSF_this","#TSF_fin.","sample_quine.tsf"]),"T")
TSF_Forth_setTSF("quine_echo:","\t".join([
    "#TSF_mainfile","#TSF_fileext","quine_ext:","quine_view:","#TSF_aliasQN","#TSF_this"]),"T")
TSF_Forth_setTSF("quine_ext:","\t".join([
    ".tsf",".py",".d"]),"T")
TSF_Forth_setTSF("quine_view:","\t".join([
    "quine_TSF:","quine_Python:","quine_D:"]),"T")
TSF_Forth_setTSF("quine_TSF:","\t".join([
    "#TSF_viewthey"]),"N")
TSF_Forth_setTSF("quine_Python:","\t".join([
    "#TSF_Python"]),"N")
TSF_Forth_setTSF("quine_D:","\t".join([
    "#TSF_D-lang"]),"N")

TSF_Forth_run()
