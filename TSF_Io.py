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
from collections import OrderedDict
from collections import deque


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

TSF_libc=None
if sys.platform.startswith("win"):
    TSF_libc=ctypes.cdll.msvcrt
if sys.platform.startswith("linux"):
    TSF_libc=ctypes.CDLL("libc.so.6")

TSF_Io_stdout=sys.stdout.encoding if sys.stdout.encoding != None else locale.getpreferredencoding()
def TSF_Io_printlog(TSF_text,TSF_log=None):    ##TSFdoc:テキストをstdoutに表示。ログに追記もできる。(TSFAPI)
    TSF_log="" if TSF_log == None else TSF_log if TSF_log.endswith('\n') else "".join([TSF_log,'\n']) if len(TSF_log) else ""
    TSF_Io_printf=TSF_text.encode(TSF_Io_stdout,"xmlcharrefreplace")
    if TSF_text.endswith('\n'):
        TSF_libc.printf(b"%s",TSF_Io_printf)
        TSF_log="".join([TSF_log,TSF_text]) if TSF_log != None else ""
    else:
        TSF_libc.printf(b"%s\n",TSF_Io_printf)
        TSF_log="".join([TSF_log,TSF_text,'\n']) if TSF_log != None else ""
    return TSF_log

def TSF_Io_argvs(TSF_argvobj=None):    #TSFdoc:TSF起動コマンド引数の文字コード対策。(TSFAPI)
    TSF_argvs=[]
    if sys.version_info.major == 2:
        for TSF_argv in sys.argv:
            TSF_argvs.append(TSF_argv.decode(TSF_Io_stdout))
    if sys.version_info.major == 3:
        for TSF_argv in sys.argv:
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
    TSF_text=TSF_text.replace('&',"&amp;").replace('\t',"&tab;")
    return TSF_text

def TSF_Io_ESCdecode(TSF_text):    #TSFdoc:「&tab;」を「\t」に戻す。(TSFAPI)
    TSF_text=TSF_text.replace("&tab;",'\t').replace("&amp;",'&')
    return TSF_text

def TSF_Io_splitlen(TSF_text,TSF_split):    #TSFdoc:テキストの行数などを取得。(TSFAPI)
    TSF_splitlen=TSF_Io_separatelen(TSF_text.split(TSF_split))
    return TSF_splitlen
def TSF_Io_separatelen(TSF_separate):    #TSFdoc:リストの数を取得。(TSFAPI)
    TSF_separatelen=len(TSF_separate)
    return TSF_separatelen

def TSF_Io_splitpeekN(TSF_tsv,TSF_split,TSF_peek):    #TSFdoc:TSVなどから数値指定で読込。(TSFAPI)
    TSF_pull=TSF_Io_separatepeekN(TSF_tsv.split(TSF_split),TSF_peek)
    return TSF_pull
def TSF_Io_separatepeekN(TSF_separate,TSF_peek):    #TSFdoc:リストから数値指定で読込。(TSFAPI)
    TSF_pull=""
    if 0 <= TSF_peek < len(TSF_separate):
        TSF_pull=TSF_separate[TSF_peek]
    return TSF_pull
def TSF_Io_splitpeekL(TSF_ltsv,TSF_split,TSF_label):    #TSFdoc:LTSVからラベル指定で読込。(TSFAPI)
    TSF_pull=TSF_Io_separatepeekL(TSF_ltsv.split(TSF_split),TSF_label)
    return TSF_pull
def TSF_Io_separatepeekL(TSF_separate,TSF_label):    #TSFdoc:リストからラベル指定で読込。(TSFAPI)
    TSF_pull=""
    if len(TSF_label) > 0:
        for TSF_separated in TSF_separate:
            if TSF_separated.find(TSF_label) == 0:
                TSF_pull=TSF_separated[len(TSF_label):]
    return TSF_pull

def TSF_Io_splitpokeN(TSF_tsv,TSF_split,TSF_peek,TSF_poke):    #TSFdoc:TSVなどから数値指定で書込。(TSFAPI)
    TSF_splitpoked=TSF_Io_separatepokeN(TSF_tsv.split(TSF_split),TSF_peek,TSF_poke)
    return TSF_split.join(TSF_splitpoked)
def TSF_Io_separatepokeN(TSF_separate,TSF_peek,TSF_poke):    #TSFdoc:リストから数値指定で書込。(TSFAPI)
    if 0 <= TSF_peek < len(TSF_separate):
        TSF_separate[TSF_peek]=TSF_poke
    return TSF_separate
def TSF_Io_splitpokeL(TSF_ltsv,TSF_split,TSF_label,TSF_poke):    #TSFdoc:LTSVからラベル指定で書込。(TSFAPI)
    TSF_splitpoked=TSF_Io_separatepokeL(TSF_ltsv.split(TSF_split),TSF_label,TSF_poke)
    return TSF_split.join(TSF_splitpoked)
def TSF_Io_separatepokeL(TSF_separate,TSF_label,TSF_poke):    #TSFdoc:リストからラベル指定で書込。(TSFAPI)
    if len(TSF_label) > 0:
        for TSF_peek,TSF_separated in enumerate(TSF_separate):
            if TSF_separated.find(TSF_label) == 0:
                TSF_separate[TSF_peek]=TSF_label+TSF_poke
    return TSF_separate

def TSF_Io_splitpullN(TSF_tsv,TSF_split,TSF_peek):    #TSFdoc:TSVなどから数値指定で引抜。(TSFAPI)
    TSF_separated=TSF_Io_separatepullN(TSF_tsv.split(TSF_split),TSF_peek)
    return TSF_split.join(TSF_separated)
def TSF_Io_separatepullN(TSF_separate,TSF_peek):    #TSFdoc:リストから数値指定で引抜。(TSFAPI)
    TSF_joined="",TSF_separate
    if 0 <= TSF_peek < len(TSF_separate):
        TSF_joined=TSF_separate[:TSF_peek]+TSF_separate[TSF_peek+1:]
    return TSF_joined
def TSF_Io_splitpullL(TSF_ltsv,TSF_split,TSF_label):    #TSFdoc:LTSVからラベル指定で引抜。(TSFAPI)
    TSF_separated=TSF_Io_separatepullL(TSF_ltsv.split(TSF_split),TSF_label)
    return TSF_split.join(TSF_separated)
def TSF_Io_separatepullL(TSF_separate,TSF_label):    #TSFdoc:リストからラベル指定で引抜。(TSFAPI)
    TSF_joined="",TSF_separate
    if len(TSF_label) > 0:
        for TSF_peek,TSF_separated in enumerate(TSF_separate):
            if TSF_separated.find(TSF_label) == 0:
                TSF_joined=TSF_separate[:TSF_peek]+TSF_separate[TSF_peek+1:]
    return TSF_joined

def TSF_Io_splitpushN(TSF_tsv,TSF_split,TSF_peek,TSF_push):    #TSFdoc:TSVなどから数値指定で差込。(TSFAPI)
    TSF_separated=TSF_Io_separatepushN(TSF_tsv.split(TSF_split),TSF_peek,TSF_push)
    return TSF_split.join(TSF_separated)
def TSF_Io_separatepushN(TSF_separate,TSF_peek,TSF_push):    #TSFdoc:リストから数値指定で差込。(TSFAPI)
    TSF_joined=TSF_separate
    if 0 <= TSF_peek < len(TSF_separate):
        TSF_joined=TSF_separate[:TSF_peek]+[TSF_push]+TSF_separate[TSF_peek:]
    elif TSF_peek < 0:
        TSF_joined=[TSF_push]+TSF_separate
    elif len(TSF_separate) <= TSF_peek:
        TSF_joined=TSF_separate+[TSF_push]
    return TSF_joined
def TSF_Io_splitpushL(TSF_ltsv,TSF_split,TSF_label,TSF_push):    #TSFdoc:LTSVからラベル指定で差込。(TSFAPI)
    TSF_separated=TSF_Io_separatepushL(TSF_ltsv.split(TSF_split),TSF_label,TSF_push)
    return TSF_split.join(TSF_separated)
def TSF_Io_separatepushL(TSF_separate,TSF_label,TSF_push):    #TSFdoc:リストからラベル指定で差込。(TSFAPI)
    TSF_joined=[]
    if len(TSF_label) > 0:
        for TSF_peek,TSF_separated in enumerate(TSF_separate):
            if TSF_separated.find(TSF_label) == 0:
                TSF_joined=TSF_separate; TSF_joined[TSF_peek]=TSF_label+TSF_push; 
        if len(TSF_joined) == 0:
            TSF_joined=TSF_separate+[TSF_label+TSF_push]
    else:
        TSF_joined=TSF_separate
    return TSF_joined

def TSF_Io_RPN(TSF_RPN):    #TSFdoc:逆ポーランド電卓。分数は簡易的に小数で処理するので不正確。一応ゼロ除算を「n|0」と返せる。(TSFAPI)
    TSF_RPNanswer=""
    TSF_RPNnum,TSF_RPNminus="",0
    TSF_RPNstack=deque([])
    TSF_RPNseq=TSF_RPN.replace("U+","$").replace("0x","$")+" "
    for TSF_RPNope in TSF_RPNseq:
        if TSF_RPNope in "0123456789.pm$|":
            TSF_RPNnum+=TSF_RPNope
        else:
            if len(TSF_RPNnum) > 0:
                TSF_RPNminus=TSF_RPNnum.count('m');  TSF_RPNnum=TSF_RPNnum.replace('p','').replace('m','')
                if "$" in TSF_RPNnum:
                    try:
                        TSF_RPNcalcN,TSF_RPNcalcD=int(TSF_RPNnum.replace("$",""),16),1.0
                    except ValueError:
                        TSF_RPNanswer="n|0"
                        break;
                elif "|" in TSF_RPNnum:
                    try:
                        TSF_RPNcalcND=TSF_RPNnum.split("|")
                        TSF_RPNcalcN,TSF_RPNcalcD=float(TSF_RPNcalcND[0]),float(TSF_RPNcalcND[-1])
                    except ValueError:
                        TSF_RPNanswer="n|0"
                        break;
                else:
                    try:
                        TSF_RPNcalcN,TSF_RPNcalcD=float(TSF_RPNnum),1.0
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
            if TSF_RPNope in "+-*/":
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
                        TSF_RPNanswer="n|0"
                        break;
    TSF_RPNstackL=TSF_RPNstack.pop() if len(TSF_RPNstack) > 0 else 0.0
    if TSF_RPNanswer != "n|0":
        TSF_RPNanswer=str(TSF_RPNstackL) if TSF_RPNstackL != int(TSF_RPNstackL) else str(int(TSF_RPNstackL))
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
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyIo.log";
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
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitlen(TSF_debug_log,'\n')),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitlen("csv\ttsv\tLTSV\tL:Tsv\tTSF",'\t')),TSF_debug_log)
    TSF_debug_PPPP="this:Peek\tthat:Poke\tthe:Pull\tthey:Push"
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpeekN(TSF_debug_PPPP,'\t',0)),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpeekL(TSF_debug_PPPP,'\t',"this:")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpokeN(TSF_debug_PPPP,'\t',1,"poked")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpokeL(TSF_debug_PPPP,'\t',"that:","poked")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpokeL(TSF_debug_PPPP,'\t',"cards:","poked")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpullN(TSF_debug_PPPP,'\t',2)),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpullL(TSF_debug_PPPP,'\t',"the:")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpushN(TSF_debug_PPPP,'\t',-1,"pushed")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpushN(TSF_debug_PPPP,'\t',3,"pushed")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpushN(TSF_debug_PPPP,'\t',10,"pushed")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpushL(TSF_debug_PPPP,'\t',"they:","pushed")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_splitpushL(TSF_debug_PPPP,'\t',"cards:","pushed")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_debug_rpn:",TSF_log=TSF_debug_log)
    for debug_rpn in ["U+p128","1.414|3","2,3+","2,m3+","2,3-","2,m3-","2,3*","2,3/","0|0","0,0/"]:
        TSF_debug_log=TSF_Io_printlog("\t{0}\t{1}".format(debug_rpn,TSF_Io_RPN(debug_rpn)),TSF_debug_log)
    print("--- fin. > {0} ---".format(TSF_debug_savefilename))
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log
#helloワールド\u5496\u55B1

if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(sys.argv))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
