set encoding=utf-8
scriptencoding utf-8
let s:kev_scriptdir = expand('<sfile>:p:h')

"「KanEditVim」の初期化初期設定(imap等含む)。
function! KEV2setup()
    let s:KEV2_menuid = 10000
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

function! KEV2exit()
    call KEV2pullmenu()
endfunction

call KEV2setup()
finish

"# Copyright (c) 2016-2017 ooblog
"# License: MIT
"# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
