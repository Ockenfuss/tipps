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

