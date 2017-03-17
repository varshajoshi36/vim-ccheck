if !has('python')
	finish
endif

function ccheck#init()
	pyfile copyBuffer.py
	let s:path = expand('<sfile>:p:h') 
	let myparserFile = s:path."/myparser/myparser.py"
	let tempFile = s:path."/temporaryBufferCopyFile.c"
	let pythonComand = "!python"." ".myparserFile." ".tempFile
	execute pythonComand
endfunction

command! Ccheck call ccheck#init()
