#! /usr/bin/env rdmd

import std.string;

import TSF_Io;
import TSF_Forth;
import TSF_Trans;

void main(string[] sys_argvs){
    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);
    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=[&TSF_Forth_Initcards,&TSF_Trans_Initcards];
TSF_Forth_initTSF(TSF_sysargvs[1..$],TSF_Initcallrun);

    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "Hello world","#TSF_echo"],"\t"),"T");

    TSF_Forth_run();
}