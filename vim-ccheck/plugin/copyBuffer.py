import vim
import string

data = string.join(vim.current.buffer, "\n")
filename = "temporaryBufferCopyFile.c"
f = open(filename, "w+")
f.write(data)
f.close()
