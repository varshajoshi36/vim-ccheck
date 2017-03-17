if !has('python')
	finish
endif

function ccheck#init()
	pyfile copyBuffer.py
	let s:path = expand('<sfile>:p:h') 
	let myparserFile = "~/.vim/bundle/vim-ccheck/plugin/myparser/myparser.py"
	let tempFile = "~/.vim/bundle/vim-ccheck/plugin/temporaryBufferCopyFile.c"
	let pythonComand = "!python"." ".myparserFile." ".tempFile
	execute pythonComand
endfunction

command! Ccheck call ccheck#init()
