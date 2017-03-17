import vim
import string
from os.path import expanduser

homePath = expanduser("~")

data = string.join(vim.current.buffer, "\n")

filename = homePath+"/.vim/bundle/vim-ccheck/plugin/temporaryBufferCopyFile.c"
f = open(filename, "w")
f.write(data)
f.close()
