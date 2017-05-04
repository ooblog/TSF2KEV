#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *
from TSF_Shuffle import *
from TSF_Calc import *
from TSF_Match import *
from TSF_Trans import *

TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Shuffle_Initcards,TSF_Calc_Initcards,TSF_Match_Initcards,TSF_Trans_Initcards]
TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcallrun)

TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
    "help:","#TSF_argvsthe","#TSF_echoN","#TSF_fin."]),"T")
TSF_Forth_setTSF("help:","\t".join([
    "usage: ./TSF.py [command|file.tsf] [argvs] ...",
    "commands & samples:",
    "  --help        this commands view",
    "  --python      TSF to Python",
    "  --dlang       TSF to D",
    "  --about       about TSF mini guide",
    "  --helloworld  \"Hello world  #TSF_echo\" sample",
    "  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... ",
    "  --calc        fraction calculator \"1/3-m1|2\"-> p5|6",
    "  --fizzbuzz    Fizz(#3) Buzz(#5) Fizz&Buzz(#15) sample"]),"N")

TSF_Forth_run()
