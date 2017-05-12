" TSF syntax file
" Language:	TSF_Tab-Separated-Forth:
" Maintainer:	ooblog
" Last Change:	2017 May 12


"syntax iskeyword	[,#,@,_,-,|,.,],48-57,192-255
setlocal iskeyword=32-127,192-255

syntax match tsfComment		"^#.*$"
syntax match tsfIdentifier		"^[^\t^\n]*\ze\n"
syntax match tsfIdentifier		"^[^\t^\n]*\ze\t"
syntax match tsfStatement	"\t\zs\#[^\t^\n]*\ze\t"
syntax match tsfStatement	"\t\zs\#[^\t^\n]*\ze\n"
syntax match tsfNumber		/n|0/

highlight def link tsfComment	Comment
highlight def link tsfIdentifier	Identifier
highlight def link tsfStatement	Statement
highlight def link tsfNumber		Number

let b:current_syntax = "tsf"


"# Copyright (c) 2017 ooblog
"# License: MIT
"# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
