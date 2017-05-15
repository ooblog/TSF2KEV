#! /usr/bin/env rdmd

import std.string;
import std.path;

import TSF_Io;
import TSF_Forth;
import TSF_Shuffle;
import TSF_Calc;
import TSF_Time;
import TSF_Urlpath;
import TSF_Match;
import TSF_Trans;

void main(string[] sys_argvs){
    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);
    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=[&TSF_Forth_Initcards,&TSF_Shuffle_Initcards,&TSF_Calc_Initcards,&TSF_Time_Initcards,&TSF_Urlpath_Initcards,&TSF_Match_Initcards,&TSF_Trans_Initcards];
TSF_Forth_initTSF(TSF_sysargvs[1..$],TSF_Initcallrun);
TSF_Forth_mainfilepath(absolutePath(TSF_sysargvs[0]));

    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "Hello world","#TSF_echo"],"\t"),"T");

    TSF_Forth_run();
}
