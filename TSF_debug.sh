#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir

echo "--hello"
./TSF.d --hello > debug/debug_d-hello.log 
./TSF.py --hello > debug/debug_py-hello.log
./TSF.d --py sample/sample_helloworld.tsf debug/trans_d-hello.py
./TSF.py --py sample/sample_helloworld.tsf debug/trans_py-hello.py
./TSF.d --d sample/sample_helloworld.tsf debug/trans_d-hello.d
./TSF.py --d sample/sample_helloworld.tsf debug/trans_py-hello.d

echo "--help"
./TSF.py --help > debug/debug_py-help.log
./TSF.d --help > debug/debug_d-help.log 
./TSF.d --d sample/sample_help.tsf debug/trans_help.d
./TSF.d --py sample/sample_help.tsf debug/trans_help.py

echo "--about"
./TSF.py --about > debug/debug_py-about.log
./TSF.d --about > debug/debug_d-about.log 
./TSF.d --d sample/sample_aboutTSF.tsf debug/trans_about.d
./TSF.d --py sample/sample_aboutTSF.tsf debug/trans_about.py

echo "--RPN"
./TSF.py --RPN > debug/debug_py-RPN.log
./TSF.d --RPN > debug/debug_d-RPN.log 

echo "--calc"
./TSF.py --calc > debug/debug_py-calcrpn.log
./TSF.d --calc > debug/debug_d-calcrpn.log 

echo "--fizzbuzz"
./TSF.py --fizzbuzz > debug/debug_py-fizzbuzz.log
./TSF.d --fizzbuzz > debug/debug_d-fizzbuzz.log 

echo "--zundoko"
./TSF.py --zundoko > debug/debug_py-zundoko.log
./TSF.d --zundoko > debug/debug_d-zundoko.log 

echo "--99beer"
./TSF.py --99beer 99 > debug/debug_py-99beer.log
./TSF.d --99beer 99 > debug/debug_d-99beer.log 

echo "--quine"
./TSF.d --d sample/sample_quine.tsf trans_quine.d
./TSF.d --py sample/sample_quine.tsf trans_quine.py
./TSF.d sample/sample_quine.tsf > sample/sample_quine.tsf.txt
./trans_quine.py > trans_quine.py.txt
./trans_quine.d > trans_quine.d.txt
diff trans_quine.py trans_quine.py.txt
diff trans_quine.d trans_quine.d.txt
diff sample/sample_quine.tsf sample/sample_quine.tsf.txt
