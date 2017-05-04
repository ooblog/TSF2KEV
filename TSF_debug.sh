#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir

./TSF.d --hello > debug/debug_d-hello.log 
./TSF.py --hello > debug/debug_py-hello.log

./TSF.d --py sample/sample_helloworld.tsf debug/trans_d-hello.py
./TSF.py --py sample/sample_helloworld.tsf debug/trans_py-hello.py
./TSF.d --d sample/sample_helloworld.tsf debug/trans_d-hello.d
./TSF.py --d sample/sample_helloworld.tsf debug/trans_py-hello.d

./TSF.py --help > debug/debug_py-help.log
./TSF.d --help > debug/debug_d-help.log 
./TSF.d --d sample/sample_help.tsf debug/trans_help.d
./TSF.d --py sample/sample_help.tsf debug/trans_help.py

./TSF.py --about > debug/debug_py-about.log
./TSF.d --about > debug/debug_d-about.log 
./TSF.d --d sample/sample_aboutTSF.tsf debug/trans_about.d
./TSF.d --py sample/sample_aboutTSF.tsf debug/trans_about.py

./TSF.py --RPN > debug/debug_py-RPN.log
./TSF.d --RPN > debug/debug_d-RPN.log 

./TSF.py --calc > debug/debug_py-calcrpn.log
./TSF.d --calc > debug/debug_d-calcrpn.log 

