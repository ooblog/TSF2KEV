#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import locale
import codecs
import os
import subprocess
import ctypes
import zipfile
import base64
import datetime
import math
#import decimal
import struct
#from collections import OrderedDict
#from collections import deque


TSF_Io_name2codepoint,TSF_Io_urlliburlretrieve=None,None
if sys.version_info.major == 2:
    import htmlentitydefs
    TSF_Io_name2codepoint=htmlentitydefs.name2codepoint
    import HTMLParser
    TSF_Io_htmlparser=HTMLParser
    import urllib
    TSF_Io_urlliburlretrieve=urllib.urlretrieve
if sys.version_info.major == 3:
    import html.entities
    TSF_Io_name2codepoint=html.entities.name2codepoint
    import html.parser
    TSF_Io_htmlparser=html.parser
    import urllib.request
    TSF_Io_urlliburlretrieve=urllib.request.urlretrieve

TSF_maxint=2**(struct.Struct('i').size*8-1)-1;  TSF_minint=-TSF_maxint-1
TSF_longint=long if sys.version_info.major == 2 else int

TSF_libc=None
if sys.platform.startswith("win"):
    TSF_libc=ctypes.cdll.msvcrt
if sys.platform.startswith("linux"):
    TSF_libc=ctypes.CDLL("libc.so.6")

TSF_Io_stdout=sys.stdout.encoding if sys.stdout.encoding != None else locale.getpreferredencoding()
def TSF_Io_printlog(TSF_text,TSF_log=None):    #TSFdoc:テキストをstdoutに表示。ログに追記もできる。(TSFAPI)<br>
    TSF_text=TSF_text.rstrip('\n')
    if TSF_log != None:
        if len(TSF_log) > 0:
            TSF_log=TSF_log if TSF_log.endswith('\n') else "".join([TSF_log,'\n'])
        TSF_log="".join([TSF_log,TSF_text,'\n'])
    else:
        TSF_log=""
    TSF_Io_printf=TSF_text.encode(TSF_Io_stdout,"xmlcharrefreplace")
    TSF_libc.printf(b"%s\n",TSF_Io_printf)
    return TSF_log

def TSF_Io_argvs(TSF_argvdup=None):    #TSFdoc:TSF起動コマンド引数の文字コード対策。(TSFAPI)
    TSF_argvs=[]
    if sys.version_info.major == 2:
        for TSF_argv in TSF_argvdup:
            TSF_argvs.append(TSF_argv.decode(TSF_Io_stdout))
    if sys.version_info.major == 3:
        for TSF_argv in TSF_argvdup:
            TSF_argvs.append(TSF_argv)
    return TSF_argvs

def TSF_Io_loadtext(TSF_path,TSF_encoding="utf-8"):    #TSFdoc:ファイルからテキストを読み込む。通常「UTF-8」を扱う。(TSFAPI)
    TSF_text=""
    TSF_encoding=TSF_encoding.lower()
    if TSF_encoding in ["utf-8","utf_8","u8","utf","utf8"]: TSF_encoding="utf-8"
    if TSF_encoding in ["cp932","932","mskanji","ms-kanji","sjis","shiftjis","shift-jis","shift_jis"]: TSF_encoding="cp932"
    if os.path.isfile(TSF_path):
        if sys.version_info.major == 2:
            with open(TSF_path,"r") as TSF_Io_fileobj:
                TSF_byte=TSF_Io_fileobj.read()
            TSF_text=unicode(TSF_byte,TSF_encoding,errors="xmlcharrefreplace")
        if sys.version_info.major == 3:
            with open(TSF_path,mode="r",encoding=TSF_encoding,errors="xmlcharrefreplace") as TSF_Io_fileobj:
                TSF_text=TSF_Io_fileobj.read()
    return TSF_text

def TSF_Io_ESCencode(TSF_text):    #TSFdoc:「\t」を「&tab;」に置換。(TSFAPI)
    TSF_text=TSF_text.replace("&","&amp;").replace("\t","&tab;")
    return TSF_text

def TSF_Io_ESCdecode(TSF_text):    #TSFdoc:「&tab;」を「\t」に戻す。(TSFAPI)
    TSF_text=TSF_text.replace("&tab;","\t").replace("&amp;","&")
    return TSF_text

#"0123456789abcdef.pm$|":
#M,P,Atan2,atan,SinCosTan,RootE,Log,Pi,^,Gg
def TSF_Io_RPN(TSF_RPN):    #TSFdoc:逆ポーランド電卓。分数は簡易的に小数で処理するので不正確。ゼロ除算も「n|0」とテキストで返す。(TSFAPI)
    TSF_RPNanswer=""
    TSF_RPNnum,TSF_RPNminus="",0
    TSF_RPNstack=[]
    TSF_RPNseq="".join([TSF_RPN.lstrip(","),"  "])
    if TSF_RPNseq[0]=="-":  TSF_RPNseq="".join(["m",TSF_RPNseq[1:]])
    elif TSF_RPNseq[0]=="/":  TSF_RPNseq="".join(["1|",TSF_RPNseq[1:]])
    elif TSF_RPNseq[0]=="*":  TSF_RPNseq=TSF_RPNseq[1:]
    if TSF_RPNseq[0:2] in ["U+","0x"]:  TSF_RPNseq="".join(["$",TSF_RPNseq[2:]])
    for TSF_RPNope in TSF_RPNseq:
        if TSF_RPNope in "0123456789abcdef.pm$|":
            TSF_RPNnum+=TSF_RPNope
        else:
            if len(TSF_RPNnum) > 0:
                TSF_RPNminus=TSF_RPNnum.count('m');  TSF_RPNnum=TSF_RPNnum.replace("p","").replace("m","").replace(" ","")
                if "|" in TSF_RPNnum:
                    try:
                        TSF_RPNcalcND=TSF_RPNnum.split("|")
                        TSF_RPNcalcN=float(int(TSF_RPNcalcND[0].replace("$",""),16)) if "$" in TSF_RPNcalcND[0] else float(TSF_RPNcalcND[0])
                        TSF_RPNcalcD=float(int(TSF_RPNcalcND[-1].replace("$",""),16)) if "$" in TSF_RPNcalcND[1] else float(TSF_RPNcalcND[1])
                    except ValueError:
                        TSF_RPNanswer="n|0"
                        break;
                else:
                    try:
                        TSF_RPNcalcN,TSF_RPNcalcD=float(int(TSF_RPNnum.replace("$",""),16)) if "$" in TSF_RPNnum else float(TSF_RPNnum),1.0
                    except ValueError:
                        TSF_RPNanswer="n|0"
                        break;
                if TSF_RPNminus%2:
                    TSF_RPNcalcN=-TSF_RPNcalcN
                try:
                    TSF_RPNstack.append(TSF_RPNcalcN/TSF_RPNcalcD)
                except ZeroDivisionError:
                    TSF_RPNanswer="n|0"
                    break;
                TSF_RPNnum=""
            if TSF_RPNope in "!SCTsctRELl":
                TSF_RPNstackL=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
                if TSF_RPNope == "!":
                    TSF_RPNstack.append(abs(TSF_RPNstackL))
                elif TSF_RPNope == "S":
                    TSF_RPNstack.append(math.sin(TSF_RPNstackL))
                elif TSF_RPNope == "C":
                    TSF_RPNstack.append(math.cos(TSF_RPNstackL))
                elif TSF_RPNope == "T":
                    TSF_RPNstack.append(math.tan(TSF_RPNstackL))
                elif TSF_RPNope == "s":
                    TSF_RPNstack.append(math.asin(TSF_RPNstackL))
                elif TSF_RPNope == "c":
                    TSF_RPNstack.append(math.acos(TSF_RPNstackL))
                elif TSF_RPNope == "t":
                    TSF_RPNstack.append(math.atan(TSF_RPNstackL))
                elif TSF_RPNope == "R":
                    TSF_RPNstack.append(math.sqrt(TSF_RPNstackL))
                elif TSF_RPNope == "E":
                    TSF_RPNstack.append(math.log1p(TSF_RPNstackL))
                elif TSF_RPNope == "L":
                    TSF_RPNstack.append(math.log10(TSF_RPNstackL))
                elif TSF_RPNope == "l":
                    TSF_RPNstack.append(math.log(TSF_RPNstackL,2))
            elif TSF_RPNope in "+-*/\\#%<>AH^":
                TSF_RPNstackR=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
                TSF_RPNstackL=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
                if TSF_RPNope == "+":
                    TSF_RPNstack.append(TSF_RPNstackL+TSF_RPNstackR)
                elif TSF_RPNope == "-":
                    TSF_RPNstack.append(TSF_RPNstackL-TSF_RPNstackR)
                elif TSF_RPNope == "*":
                    TSF_RPNstack.append(TSF_RPNstackL*TSF_RPNstackR)
                elif TSF_RPNope == "/":
                    try:
                        TSF_RPNstack.append(TSF_RPNstackL/TSF_RPNstackR)
                    except ZeroDivisionError:
                        TSF_RPNanswer="n|0";  break;
                elif TSF_RPNope == "\\":
                    try:
                        TSF_RPNstack.append(float(TSF_RPNstackL//TSF_RPNstackR))
                    except ZeroDivisionError:
                        TSF_RPNanswer="n|0";  break;
                elif TSF_RPNope == "#":
                    try:
                        if TSF_RPNstackR > 0:
                            TSF_RPNstack.append(TSF_RPNstackL%TSF_RPNstackR)
                        else:
                            if TSF_RPNstackL%abs(TSF_RPNstackR) != 0:
                                TSF_RPNstack.append(abs(TSF_RPNstackR)-TSF_RPNstackL%abs(TSF_RPNstackR))
                            else:
                                TSF_RPNstack.append(0.0)
                    except ZeroDivisionError:
                        TSF_RPNanswer="n|0";  break;
                elif TSF_RPNope == "%":
                    TSF_RPNstack.append(TSF_RPNstackL+TSF_RPNstackL*TSF_RPNstackR/100.0)
                elif TSF_RPNope == ">":
                    TSF_RPNstack.append(min(TSF_RPNstackL,TSF_RPNstackR))
                elif TSF_RPNope == "<":
                    TSF_RPNstack.append(max(TSF_RPNstackL,TSF_RPNstackR))
                elif TSF_RPNope == "A":
                    TSF_RPNstack.append(math.atan2(TSF_RPNstackL,TSF_RPNstackR))
                elif TSF_RPNope == "H":
                    TSF_RPNstack.append(math.hypot(TSF_RPNstackL,TSF_RPNstackR))
                elif TSF_RPNope == "^":
                    if TSF_RPNstackL == 0.0 and TSF_RPNstackR <= 0.0:
                        TSF_RPNanswer="n|0";  break;
                    else:
                        TSF_RPNstack.append(pow(TSF_RPNstackL,TSF_RPNstackR))
            elif TSF_RPNope in "ZzOoUu":
                TSF_RPNstackF=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
                TSF_RPNstackR=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
                TSF_RPNstackL=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
                if TSF_RPNope == "Z":
                    TSF_RPNstack.append(TSF_RPNstackL if TSF_RPNstackF==0 else TSF_RPNstackR)
                elif TSF_RPNope == "z":
                    TSF_RPNstack.append(TSF_RPNstackL if TSF_RPNstackF!=0 else TSF_RPNstackR)
                elif TSF_RPNope == "O":
                    TSF_RPNstack.append(TSF_RPNstackL if TSF_RPNstackF>=0 else TSF_RPNstackR)
                elif TSF_RPNope == "o":
                    TSF_RPNstack.append(TSF_RPNstackL if TSF_RPNstackF>0 else TSF_RPNstackR)
                elif TSF_RPNope == "U":
                    TSF_RPNstack.append(TSF_RPNstackL if TSF_RPNstackF<=0 else TSF_RPNstackR)
                elif TSF_RPNope == "u":
                    TSF_RPNstack.append(TSF_RPNstackL if TSF_RPNstackF<0 else TSF_RPNstackR)
    TSF_RPNstackL=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
    if TSF_RPNanswer != "n|0":
        TSF_RPNanswer=str(TSF_RPNstackL)
        if "e+" in TSF_RPNanswer:
            TSF_RPNloge=TSF_RPNanswer.split("e+"); TSF_RPNloge[0]=TSF_RPNloge[0].replace(".","").replace("-","")
            TSF_RPNlogeN=int(TSF_RPNloge[-1])-len(TSF_RPNloge[0])+1
            TSF_RPNlogeZ='0'*TSF_RPNlogeN
            TSF_RPNanswer="".join(["" if TSF_RPNstackL >= 0 else "-",TSF_RPNloge[0],TSF_RPNlogeZ])
        elif "e-" in TSF_RPNanswer:
            TSF_RPNloge=TSF_RPNanswer.split("e-"); TSF_RPNloge[0]=TSF_RPNloge[0].replace(".","").replace("-","")
            TSF_RPNlogeN=int(TSF_RPNloge[-1])-len(TSF_RPNloge[0])
            TSF_RPNlogeZ='0'*TSF_RPNlogeN
            TSF_RPNanswer="".join(["0." if TSF_RPNstackL >= 0 else "-0.",TSF_RPNlogeZ,TSF_RPNloge[0]])
        elif TSF_RPNstackL == int(TSF_RPNstackL):
            TSF_RPNanswer=str(int(TSF_RPNstackL))
        if TSF_RPNanswer != "0":
            TSF_RPNanswer=TSF_RPNanswer.replace('-','m') if TSF_RPNanswer.startswith('-') else "".join(["p",TSF_RPNanswer])
    return TSF_RPNanswer
# 0.0000123	p1.23e-05

def TSF_Io_RPNzero(TSF_RPN):    #TSFdoc:逆ポーランド電卓。分数は簡易的に小数で処理するので不正確。ゼロ除算を「0」と数値で返す。(TSFAPI)
    TSF_RPNtext=TSF_Io_RPN(TSF_RPN)
    TSF_RPNtext=TSF_RPNtext.replace("p","").replace("m","-")
    TSF_RPNanswer=0
    try:
        TSF_RPNanswer=int(TSF_RPNtext)
    except ValueError:
        TSF_RPNanswer=0
    return TSF_RPNanswer

def TSF_Io_savedir(TSF_path):    #TSFdoc:「TSF_Io_savetext()」でファイル保存する時、1階層分のフォルダを作成する。(TSFAPI)
    TSF_Io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_Io_workdir) and not os.path.isdir(TSF_Io_workdir) and len(TSF_Io_workdir):
        os.mkdir(TSF_Io_workdir)

def TSF_Io_savedirs(TSF_path):    #TSFdoc:一気に深い階層のフォルダを複数作れてしまうので取扱い注意(扱わない)。(TSFAPI)
    TSF_Io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_Io_workdir) and not os.path.isdir(TSF_Io_workdir) and len(TSF_Io_workdir): os.makedirs(TSF_Io_workdir)

def TSF_Io_savetext(TSF_path,TSF_text=None):    #TSFdoc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。(TSFAPI)
    if TSF_text != None:
        TSF_Io_savedir(TSF_path)
        if not TSF_text.endswith('\n'):
            TSF_text+='\n'
        if sys.version_info.major == 2:
            with open(TSF_path,'wb') as TSF_Io_fileobj:
                TSF_Io_fileobj.write(TSF_text.encode("UTF-8"))
        if sys.version_info.major == 3:
            with open(TSF_path,mode="w",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_Io_fileobj:
                TSF_Io_fileobj.write(TSF_text)
    else:
        os.remove(TSF_text)

def TSF_Io_writetext(TSF_path,TSF_text):    #TSFdoc:TSF_pathにTSF_textを追記する。(TSFAPI)
    if TSF_text != None:
        TSF_Io_savedir(TSF_path)
        if not TSF_text.endswith('\n'):
            TSF_text+='\n'
        if sys.version_info.major == 2:
            with open(TSF_path,'ab') as TSF_Io_fileobj:
                TSF_Io_fileobj.write(TSF_text.encode("UTF-8"))
        if sys.version_info.major == 3:
            with open(TSF_path,mode="a",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_Io_fileobj:
                TSF_Io_fileobj.write(TSF_text)


def TSF_Io_debug(TSF_argvs):    #TSFdoc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Io.log";
    print("--- {0} ---".format(__file__))
    TSF_debug_log=TSF_Io_printlog("TSF_Tab-Separated-Forth:",TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("\t".join(["0",":TSF_fin."])),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_argvs:",TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_py:",TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("\t".join(["Python({0}){1.major}.{1.minor}.{1.micro}".format(sys.copyright.split('\n')[0],sys.version_info),sys.platform,TSF_Io_stdout])),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_debug_tsv:",TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("helloワールド\u5496\u55B1"),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_ESCencode("csv\ttsv\tLTSV\tL:Tsv\tTSF")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_ESCdecode("csv&tab;tsv&tab;LTSV&tab;L:Tsv&tab;TSF")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_debug_rpn:",TSF_log=TSF_debug_log)
    for debug_rpn in [
        "0","0.0","U+p128","$ffff","m1","-1","1.414|3","2,3+","2,m3+","2,3-","2,m3-","2,3*","2,3/","0|0","0,0/","5,3\\","5,3#","5,3<","5,3>",
        "5,7,p1Z","5,7,0Z","5,7,m1Z","5,7,p1z","5,7,0z","5,7,m1z","5,7,p1O","5,7,0O","5,7,m1O","5,7,p1o","5,7,0o","5,7,m1o","5,7,p1U","5,7,0U","5,7,m1U","5,7,p1u","5,7,0u","5,7,m1u",
        "456000000000000000000000000","-789000000000000000000000000",
        "0.0000000000456","-0.0000000000789",",/10000000000000000000000000|1",
        "0.0001","0.00001","0.000001",
        "0,p1^","0,0^","0,m1^",
    ]:
        TSF_debug_log=TSF_Io_printlog("\t{0}\t{1}".format(debug_rpn,TSF_Io_RPN(debug_rpn)),TSF_debug_log)
    print("--- fin. > {0} ---".format(TSF_debug_savefilename))
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log
#helloワールド\u5496\u55B1

if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(sys.argv))


#! -- Copyright (c) 2017 ooblog --
#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
