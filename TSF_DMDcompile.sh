#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir

dmd -o- TSF.d TSF_Io.d TSF_Forth.d TSF_Shuffle.d TSF_Calc.d TSF_Match.d TSF_Trans.d
echo $PATH
