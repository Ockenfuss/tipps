# Various Tipps for vim


Setting up neovim (nvim):

Install plug.vim, a package manager which allows for plugin installation from inside your vimrc:
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

Create if not existing the file:
~/.config/nvim/init.vim
Add in this file:
set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath=&runtimepath
source ~/.vimrc
Then execute in nvim:
:PlugInstall

## Editing
```
i #Insert
a #Insert after cursor
o #Insert new line
O #Insert new line above
d + <move> #delete
3dd #delete 3 lines
```

## Navigation
```
hjkl #Move around
$ #Line ending
^ #Start of line
fy #go to next y
```

## Searching
```
/word #search for word
n #next occurence
1,$/search/replace/<g,i> #search and replace from first to last line. g: global, all occurences per line. i: case insensitive
```

## Copy-Paste
```
y #Yank (Copy)
p #Put (Paste)
yy #Yank line
```

## Commands
```
. #Repeat command
q #Start recording
```

## Marks
```
ma #set mark 'a'
'a #go to mark 'a'
d'a #delete until mark 'a'
```

# Pure vi
```
:set nu #add line numbering
:syntax on #syntax highlighting
```

