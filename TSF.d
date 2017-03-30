#! /usr/bin/env rdmd

import TSF_Io;
import TSF_Forth;

void main(string[] sys_argvs){
    string[] TSF_argvs=TSF_Io_argvs(sys_argvs);
    TSF_Forth_initTSF(TSF_argvs,null);
}

// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
