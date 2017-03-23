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

def TSF_Io_intstr0x(TSF_Io_codestr):    #TSFdoc:テキストを整数に変換する。10進と16進数も扱う。(TSFAPI)
    TSF_Io_codestr="{0}".format(TSF_Io_codestr).replace('m','-').replace('p','')
    TSF_Io_codeint=int(TSF_Io_floatstrND(TSF_Io_codestr))
    for TSF_Io_hexstr in ["0x","U+","$"]:
        if TSF_Io_hexstr in TSF_Io_codestr:
            try:
                TSF_Io_codeint=int(TSF_Io_codestr.replace(TSF_Io_hexstr,""),16)
            except ValueError:
                pass
            break
    return TSF_Io_codeint

def TSF_Io_floatstrND(TSF_Io_codestr):    #TSFdoc:テキストを小数に変換する。分数も扱う。(TSFAPI)
    TSF_Io_codestr="{0}".format(TSF_Io_codestr).replace('m','-').replace('p','').replace('|','/')
    TSF_Io_codefloat=0.0
    if '/' in TSF_Io_codestr:
        TSF_Io_codesplit=TSF_Io_codestr.split('/')
        TSF_Io_calcN,TSF_Io_calcD=TSF_Io_codesplit[0],TSF_Io_codesplit[-1]
        try:
            TSF_Io_codefloat=float(TSF_Io_calcN)/float(TSF_Io_calcD)
        except ValueError:
            TSF_Io_codefloat=0.0
    else:
        try:
            TSF_Io_codefloat=float(TSF_Io_codestr)
        except ValueError:
            TSF_Io_codefloat=0.0
    return TSF_Io_codefloat

def TSF_Io_ESCencode(TSF_text):
    TSF_text=TSF_text.replace('&',"&amp;").replace('\t',"&tab;")
    return TSF_text

def TSF_Io_ESCdecode(TSF_text):
    TSF_text=TSF_text.replace("&tab;",'\t').replace("&amp;",'&')
    return TSF_text

def TSF_Io_readlinedeno(TSF_text):    #TSFdoc:TSF_textの行数を取得。
    if len(TSF_text) > 0:
        TSF_linedeno=TSF_text.count('\n') if TSF_text.endswith('\n') else TSF_text.count('\n')+1
    else:
        TSF_linedeno=0
    return TSF_linedeno

def TSF_Io_readlinenum(TSF_text,TSF_linenum):    #TSFdoc:TSF_textから1行取得。
    TSF_line=""
    TSF_splits=TSF_text.rstrip('\n').split('\n')
    if 0 <= LTsv_linenum < len(TSF_splits):
        TSF_line=TSF_splits[LTsv_linenum]
    return TSF_line

def TSF_Io_overlinenum(TSF_text,TSF_linenum,TSF_line=None):    #TSFdoc:TSF_textの1行上書。LTsv_line=Noneの時は1行削除。
    TSF_splits=TSF_text.rstrip('\n').split('\n')
    if LTsv_linenum < 0:
        if TSF_line != None:
            TSF_text = '\n'.join(TSF_line.rstrip('\n').split('\n')+TSF_splits)
    elif len(TSF_splits) <= LTsv_linenum:
        if TSF_line != None:
            TSF_text = '\n'.join(TSF_splits+TSF_line.rstrip('\n').split('\n'))
    else:
        if TSF_line != None:
            if TSF_linenum == int(TSF_linenum):
                LTsv_text = '\n'.join(TSF_splits[:TSF_linenum]+LTsv_line.rstrip('\n').split('\n')+TSF_splits[TSF_linenum+1:])
            else:
                LTsv_text = '\n'.join(TSF_splits[:math.floor(TSF_linenum)]+LTsv_line.rstrip('\n').split('\n')+TSF_splits[math.ceil(TSF_linenum):])
        else:
            if type(LTsv_linenum) in (int, long):
                TSF_splits.pop(LTsv_linenum); TSF_text = '\n'.join(TSF_splits)
    return LTsv_text

def TSF_Io_savedir(TSF_path):    #TSFdoc:「TSF_Io_savetext()」でファイル保存する時、1階層分のフォルダ1個を作成する。
    TSF_Io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_Io_workdir) and not os.path.isdir(TSF_Io_workdir) and len(TSF_Io_workdir): os.mkdir(TSF_Io_workdir)

def TSF_Io_savedirs(TSF_path):    #TSFdoc:「TSF_Io_savetext()」でファイル保存する時、一気に深い階層のフォルダを複数作れてしまうので取扱い注意(扱わない)。
    TSF_Io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_Io_workdir) and not os.path.isdir(TSF_Io_workdir) and len(TSF_Io_workdir): os.makedirs(TSF_Io_workdir)

def TSF_Io_savetext(TSF_path,TSF_text=None):    #TSFdoc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。空のファイルを作る場合はTSF_textに文字列長さ0の文字列変数を用意する。
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

def TSF_Io_writetext(TSF_path,TSF_text):    #TSFdoc:TSF_pathにTSF_textを追記する。
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


def TSF_Io_debug():    #TSFdoc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_Io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_argvs:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_Io_stdout])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("TSF_debug:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format("helloワールド\u5496\u55B1"),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_intstr0x("U+p128")),TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("\t{0}".format(TSF_Io_floatstrND("1.414|3")),TSF_debug_log)
    return TSF_debug_log
#helloワールド\u5496\u55B1

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_Io_argvs(sys.argv)
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/debug_pyIo.log"
    TSF_debug_log=TSF_Io_debug()
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("--- fin. ---")


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
