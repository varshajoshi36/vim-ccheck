if !has('python')
	finish
endif

function! ContainsBooleanOperator()
	let curr_cond =  getline('.')
	if match(curr_cond, "==") != -1 || match(curr_cond, "!=") != -1 || match(curr_cond, "<") != -1 || match(curr_cond, ">") != -1
		return '0'
	endif

	return '-1'
endfunction

function test#Hello()
	pyfile myparser.py
	""let curr_line = getline('.')
	""if match(getline('.'), "if") != -1
		""let foldexpr = ContainsBooleanOperator()
		""if foldexpr != '0'
			""let line = line('.')
			""echo printf('Syntax error at line %d',line)
			""return -1
		""endif
	""endif

endfunction

""function test#init()
""	if test#Hello() != -1
""		:startinsert<CR>newline<C-W>
""	endif
	""if test#Hello() == -1
		
	""endif
""endfunction

command! Ccheck call test#Hello()
""inoremap newline <ENTER>
""inoremap continueWriting i<CR>newline<C-W>
""inoremap showError <CR>
""imap <ENTER> <ESC>:call test#init()<CR>
