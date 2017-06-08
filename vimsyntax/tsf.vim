" TSF syntax file
" Language:	TSF_Tab-Separated-Forth:
" Maintainer:	ooblog
" Last Change:	2017 June 8


"syntax iskeyword	[,#,@,_,-,|,.,],48-57,192-255
setlocal iskeyword=32-127,192-255

syntax match tsfIdentifier		"^[^\t^\n]*\ze\n"
syntax match tsfIdentifier		"^[^\t^\n]*\ze\t"
syntax match tsfstatement	"\t\zs\#[^\t^\n]*\ze\t"
syntax match tsfstatement	"\t\zs\#[^\t^\n]*\ze\n"
syntax match tsfcomment		"^\zs#!.*\ze$"	display
syntax match tsfpreproc		"\%^#!.*$"	display
syntax match tsfnumber		/n|0/

highlight def link tsfpreproc	PreProc
highlight def link tsfcomment	Comment
highlight def link tsfIdentifier	Identifier
highlight def link tsfstatement	Statement
highlight def link tsfnumber		Number

let b:current_syntax = "tsf"


"# Copyright (c) 2017 ooblog
"# License: MIT
"# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
