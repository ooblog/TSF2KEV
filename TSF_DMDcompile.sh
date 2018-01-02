#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir

if [ "$1" ]; then
  echo $1
  dmd $1 TSF_Io.d TSF_Forth.d TSF_Calc.d TSF_Time.d TSF_Urlpath.d TSF_Match.d TSF_Trans.d
else
  echo TSF.d
  dmd TSF2.d TSF_Io.d TSF_Forth.d TSF_Calc.d TSF_Time.d TSF_Urlpath.d TSF_Match.d TSF_Trans.d
fi
echo $PATH
