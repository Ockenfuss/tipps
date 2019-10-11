#######Variables###########
test=hallo #simple variable
test=$(ls) #store function output in variable !there are no spaces allowed around the "="!

#############################Pipes and redirection######################################
|#Pipes: send stdout of the left command to stdin of the right command
#Remind: stderr is not sent to the right!
cmd> NewFile#Redirection: Redirect all the output from one command to a (new) file. Its content will be overwritten!
cmd>>#Redirection with appending the new content
cmd>&1#Redirect output to stdout. "0" is stdin, 1" is stdout, "2" is stderr
2>$1#Redirect only errors to stdout

/dev/null #Black hole: Swallows all input redirected to it

#Pipes
Befehl1 | Befehl2
