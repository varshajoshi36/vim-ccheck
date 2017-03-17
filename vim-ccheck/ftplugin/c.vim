if !has('python')
	finish
endif

function c#ccheck()
	pyfile copyBuffer.py
	let myparserFile = "~/.vim/bundle/vim-ccheck/ftplugin/myparser/myparser.py"
	let tempFile = "~/.vim/bundle/vim-ccheck/ftplugin/temporaryBufferCopyFile.c"
	let pythonComand = "!python"." ".myparserFile." ".tempFile
	execute pythonComand
endfunction

command! Ccheck call c#ccheck()
