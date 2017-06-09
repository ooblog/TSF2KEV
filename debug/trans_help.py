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
    "replace:","#TSF_this","help:","#TSF_argvsthe","#TSF_echoN","#TSF_fin."]),'T')
TSF_Forth_setTSF("help:","\t".join([
    "usage: ./TSF [command|file.tsf] [argvs] ...","commands & samples:","  --help        this commands view","  --about       about TSF mini guide","  --doc         TSF and more documentation tool","  --python      TSF to Python","  --dlang       TSF to D","  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... ","  --calc        fraction calculator \"1/3-m1|2\"-> p5|6","  --calender    \"@4y@0m@0dm@wdec@0h@0n@0s\"-> {calender}","  --helloworld  \"Hello world  #TSF_echo\" sample","  --fizzbuzz    Fizz(#3) Buzz(#5) Fizz&Buzz(#15) sample","  --99bear      99 Bottles of Beer 9 Bottles sample","  --quine       quine (TSF,Python,D... selfsource) sample"]),'T')
TSF_Forth_setTSF("replace:","\t".join([
    "help:","{calender}","@4y@0m@0dm@wdec@0h@0n@0s","#TSF_calender","#TSF_replacesQON"]),'T')

TSF_Forth_run()
