set encoding=utf-8
scriptencoding utf-8
let s:kev_scriptdir = expand('<sfile>:p:h')

"「KanEditVim」の初期化初期設定(imap等含む)。
function! KEV2setup()
    let s:KEV2_menuid = 10000
    let s:KEV2_inputkeys = ['1','2','3','4','5','6','7','8','9','0','-','^', 'q','w','e','r','t','y','u','i','o','p','@','[', 'a','s','d','f','g','h','j','k','l',';',':',']', 'z','x','c','v','b','n','m',',','.','/','\']
    let s:KEV2_inputkeys += ['!','"','#','$','%','&',"'",'(',')','~','=','|', 'Q','W','E','R','T','Y','U','I','O','P','`','{', 'A','S','D','F','G','H','J','K','L','+','*','}', 'Z','X','C','V','B','N','M','<','>','?','_']
    let s:KEV2_inputkana = ["1(ぬ)","2(ふ)","3(あ)","4(う)","5(え)","6(お)","7(や)","8(ゆ)","9(よ)","0(わ)","-(ほ)","^(へ)","q(た)","s(て)","e(い)","r(す)","t(か)","y(ん)","u(な)","i(に)","o(ら)","p(せ)","@(＠)","[(ぷ)","a(ち)","s(と)","d(し)","f(は)","g(き)","h(く)","j(ま)","k(の)","l(り)",";(れ)",":(け)","](む)","z(つ)","x(さ)","c(そ)","v(ひ)","b(こ)","n(み)","m(も)",",(ね)","\\.(る)","/(め)","\\\\(ろ)"]
    let s:KEV2_inputkana += ["1(ヌ)","2(フ)","3(ア)","4(ウ)","5(エ)","6(オ)","7(ヤ)","8(ユ)","9(ヨ)","0(ワ)","-(ホ)","^(ヘ)","q(タ)","w(テ)","e(イ)","r(ス)","t(カ)","y(ン)","u(ナ)","i(ニ)","o(ラ)","p(セ)","@(｀)","[(プ)","a(チ)","s(ト)","d(シ)","f(ハ)","g(キ)","h(ク)","j(マ)","k(ノ)","l(リ)",";(レ)",":(ケ)","](ム)","z(ツ)","x(サ)","c(ソ)","v(ヒ)","b(コ)","n(ミ)","m(モ)",".(ネ)","\\.(ル)","/(メ)","\\\\(ロ)"]
    let s:KEV2_inputESCs = {"\t":"<Tab>",' ':"<Space>",'<':"<lt>",'\':"<Bslash>",'|':"<Bar>"}
    let s:KEV2_menuESCs = "\t\\:|< >.-"
    call KEV2pushmenu()
endfunction

function! KEV2imap(kankbd_kbdchar)
endfunction

"メニューの構築。
function! KEV2pushmenu()
    call KEV2pullmenu()
    execute "noremap <Plug>(KEV2help) :call KEV2help()<Enter>"
    execute "noremap <Plug>(KEV2exit) :call KEV2exit()<Enter>"
    let s:KEV2_helpmenuname = ".01 KEV2.ヘルプ(KEV\\.txt)"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".01 KEV2.ヘルプ(KEV\\.txt) <Plug>(KEV2help)"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".01 KEV2.終了(「call\\ KEV2setup()」で再開) <Plug>(KEV2exit)"
endfunction

"メニューの撤去。
function! KEV2pullmenu()
    :if exists("s:KEV2_helpmenuname")
        execute "aunmenu  <silent> " . "KEV2"
    :endif
    unlet! s:KEV2_helpmenuname
endfunction

"ヘルプファイル「KEV.txt」読込。
function! KEV2help()
    let s:kankbd_kanhelpfilepath = s:kev_scriptdir . "/KEV2.txt"
    :if filereadable(s:kankbd_kanhelpfilepath)
        execute "enew"
        execute "e " . s:kankbd_kanhelpfilepath . " | :se ro"
    :endif
endfunction

"「KEV2」の撤去。
function! KEV2exit()
    call KEV2pullmenu()
endfunction

call KEV2setup()
finish

"# Copyright (c) 2016-2017 ooblog
"# License: MIT
"# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
