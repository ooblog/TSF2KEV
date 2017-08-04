#! /usr/bin/env rdmd

import std.string;
import std.path;

import TSF_Io;
import TSF_Forth;
import TSF_Calc;
import TSF_Time;
import TSF_Urlpath;
import TSF_Match;
import TSF_Trans;

void main(string[] sys_argvs){
    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);
    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=[&TSF_Forth_Initcards,&TSF_Calc_Initcards,&TSF_Time_Initcards,&TSF_Urlpath_Initcards,&TSF_Match_Initcards,&TSF_Trans_Initcards];
    TSF_Forth_initTSF(TSF_sysargvs[1..$],TSF_Initcallrun);
    TSF_Forth_mainfilepath(absolutePath(__FILE__));

    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "replace:","#!TSF_this","help:","#!TSF_argvsthe","#!TSF_echoN","#!TSF_fin."],"\t"),'T');
    TSF_Forth_setTSF("help:",join([
        "usage: ./TSF [command|file.tsf] [argvs] ...",
        "commands & samples:",
        "  --help        this commands view",
        "  --about       about TSF mini guide",
        "  --doc         TSF and more documentation tool",
        "  --python      TSF to Python",
        "  --dlang       TSF to D",
        "  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... ",
        "  --calc        fraction calculator \"1/3-m1|2\"-> p5|6",
        "  --calender    \"@4y@0m@0dm@wdec@0h@0n@0s\"-> {calender}",
        "  --helloworld  \"Hello world  #!TSF_echo\" sample",
        "  --fizzbuzz    Fizz(#3) Buzz(#5) Fizz&Buzz(#15) sample",
        "  --zundoko     Zun Zun Zun Zun Doko VeronCho sample",
        "  --99bear      99 Bottles of Beer 9 Bottles sample",
        "  --quine       quine (TSF,Python,D... selfsource) sample"],"\t"),'N');
    TSF_Forth_setTSF("replace:",join([
        "help:","{calender}","@4y@0m@0dm@wdec@0h@0n@0s","#!TSF_calender","#!TSF_replacesQON"],"\t"),'T');

    TSF_Forth_run();
}
