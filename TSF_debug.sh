#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir

./TSF.d --hello > debug/debug_d-hello.log 
./TSF.py --hello > debug/debug_py-hello.log
./TSF.d --py sample/sample_helloworld.tsf debug/debug_d-hello.py
./TSF.py --py sample/sample_helloworld.tsf debug/debug_py-hello.py
./TSF.d --d sample/sample_helloworld.tsf debug/debug_d-hello.d
./TSF.py --d sample/sample_helloworld.tsf debug/debug_py-hello.d

./TSF.py --help > debug/debug_py-help.log
./TSF.d --help > debug/debug_d-help.log 

./TSF.py --about > debug/debug_py-about.log
./TSF.d --about > debug/debug_d-about.log 

./TSF.py --RPN > debug/debug_py-RPN.log
./TSF.d --RPN > debug/debug_d-RPN.log 
