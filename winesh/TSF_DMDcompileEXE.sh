#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir
cd ..

/mnt/home/Tahrpup605/wine-portable-1.7.18-1-p4/wine-portable "dmd TSF.d TSF_Io.d TSF_Forth.d TSF_Shuffle.d TSF_Calc.d TSF_Time.d TSF_Urlpath.d TSF_Match.d TSF_Trans.d"
