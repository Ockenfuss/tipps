#######Variables###########
test=hallo #simple variable
test=$(ls) #store function output in variable !there are no spaces allowed around the "="!
test="$variable"variable2 #Insert the variable expression and directly add variable2



######Set PATH###########
#not in .zshrc or similar, because these will be synchronized between computers via my git repo!
#in ~/.profile (works only for bash login shells): 
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
#Alternative: create link in /usr/local/bin (not in /usr/bin, this is managed by the package manager)
#############################Pipes and redirection######################################
|#Pipes: send stdout of the left command to stdin of the right command
#Remind: stderr is not sent to the right!
cmd> NewFile#Redirection: Redirect all the output from one command to a (new) file. Its content will be overwritten!
cmd>>#Redirection with appending the new content
cmd>&1#Redirect output to stdout. "0" is stdin, "1" is stdout, "2" is stderr
2>&1#Redirect only errors to stdout

/dev/null #Black hole: Swallows all input redirected to it

#Pipes
Befehl1 | Befehl2

### xargs
```bash
command1 | xargs -p -i command2 -flag1 {} -flag2#execute command2 with each output line from command1. With -i, "{}" is replaced by the output from command1. With -p, you get asked before execution.
```

##############Background jobs###########
Ctrl-Z: Pause job
bg:Continue job in background
fg: bring job to foreground
jobs #list jobs
kill %1 # '1' is the Job ID you get by calling jobs: "[1] + Running ..."
