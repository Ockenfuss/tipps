#######Variables###########
test=hallo #simple variable
test=$(ls) #store function output in variable !there are no spaces allowed around the "="!




######Set PATH###########
#not in .zshrc or similar, because these will be synchronized between computers via my git repo!
#in ~/.profile (works only for bash login shells): 
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
#Alternative: create link in /usr/local/bin (not in /usr/bin, this is managed by the package manager)