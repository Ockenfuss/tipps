# Tipps for daily Linux work
Also includes a lot of useful snippets when working with the command line

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tipps for daily Linux work](#tipps-for-daily-linux-work)
- [Linux General](#linux-general)
  - [Permissions in Linux](#permissions-in-linux)
  - [User Handling](#user-handling)
  - [Links](#links)
- [Useful bash commands](#useful-bash-commands)
  - [Printing](#printing)
  - [Searching](#searching)
  - [SVN](#svn)
  - [PDF](#pdf)
  - [Everyday commands](#everyday-commands)
- [External Devices](#external-devices)
  - [Bluetooth](#bluetooth)
- [Usermapping: Map Ownership from remote user to current user](#usermapping-map-ownership-from-remote-user-to-current-user)
- [Meteo](#meteo)
- [Change colors of command prompt:](#change-colors-of-command-prompt)

<!-- /code_chunk_output -->

bash in general: there are various types of shells: login, interactive, non-interactive
if a bash script is executed, this is usually done in a non-interactive shell. Therefore, custom commands from the .bashrc or .zshrc are not available there!

# Linux General
What is a kernel? C't Articles: https://www.heise.de/select/ct/2019/16/softlinks/yzpg?wt_mc=pred.red.ct.ct162019.174.softlink.softlink
#Change kernel parameters at runtime
cd /proc/sys #Here, kernel parameters are stored
sysctl -a#list all parameters with value
sysctl -w parameter=value #make a non-persistent change (reset by reboot)
#persistent changes can be made by modifying the .conf files in /etc/sysctl.d/

## Permissions in Linux
https://www.guru99.com/file-permissions.html
Syntax:
-rwxr-xr-x#file Type | rwx: User permissions|r-x: Group permissions| r-x: World permissions (all others)
r: read, w: write, x: execute
chmod u=rwx #change permissions of user to rwx
/etc/group #all groups
groups #command to show my groups

## User Handling
`useradd test` Add new account
`userdel -r test` remove user including his home directory

## Links
ln -s Source Destination#create symbolic link
readlink [-f]#get destination of existing link


# Useful bash commands
```bash
more#show content of ascii file
command1 | xargs -p -i command2 -flag1 {} -flag2#execute command2 with each output line from command1. With -i, "{}" is replaced by the output from command1. With -p, you get asked before execution.
```
## Printing
All options: https://www.cups.org/doc/options.html
```bash
lpstat -p #show printers
lp -d Printer_Name dokument.pdf #print pdf
lpq -a #all jobs of current computer
lprm -P Druckername Job-ID
```
## Searching
```bash
grep#: For searches within files 
find#: for searching a file/folder
```
## SVN
```bash
svn co https://svn.physik.uni-muenchen.de/repos/libRadtran/trunk libRadtran#Checkout repository
svn up#Update repository
svn diff --summarize#show changed files
svn revert -R src/#Revert all changes in src/ (recursive, be aware that changes can be lost!)
```

## PDF
```bash
qpdf -decrypt pdffile_protected.pdf pdffile_notprotected.pdf #Remove read only e.g. to make annotations to the pdf
```

## Everyday commands
Rename
```bash
rename -n#show how files would be renamed. Overview: https://www.computerhope.com/unix/rename.htm
rename -n 's/Expr1/Expr2/' files#Replace all Expr1 in the given filenames with Expr2
```
Zip
```bash
unzip file.zip -d DestinationFolder
```
Diskusage
`du -h --max-depth=1 #-h: Human readable`

```bash
time -o time.txt -f "%e" command #measure runtime of command in seconds ("%e" specifier) and write it to file time.txt
wc # counts words (-w), lines (-l) or characters (-m)
```
.zshrc
`source ~/.zshrc #reload configurations`

# External Devices
## Bluetooth
Bose qc 35 verbinden: https://askubuntu.com/questions/833322/pair-bose-quietcomfort-35-with-ubuntu-over-bluetooth
in /etc/bluetooth/main.conf: "ControllerMode = bredr" setzen und danach "sudo service bluetooth restart"
=> neu im Bluetooth Menü verbinden. Anschließend kann ggf. wieder "#ControllerMode = dual" gesetzt werden (LE=Low energy) und wieder "sudo service bluetooth restart"








########################ssh##########################################
sshfs:
killall -9 sshfs
fusermount -uz ~/Mounts/Remote #Unmount directory "Remote"
#Usermapping: Map Ownership from remote user to current user
sshfs -o idmap=user -o uid=$(id -u) -o gid=$(id -g) Paul.Ockenfuss@login.meteo.physik.uni-muenchen.de:/project/meteo/work/Paul.Ockenfuss ~/Work

scp Path/fileTocopy user@university_computer:File/path/#Copy files via ssh from one computer to other
Login at cip pool: ssh Paul.Ockenfuss@cip-sv-login01.cip.physik.uni-muenchen.de
Copy to cip pool: scp Bilderseite.pdf Paul.Ockenfuss@cip-sv-login01.cip.physik.uni-muenchen.de:~/

#Meteo
ssh Paul.Ockenfuss@login.meteo.physik.uni-muenchen.de
ssh Paul.Ockenfuss@ComputerName
rsync -a -v --exclude=".*" SimulationGit Paul.Ockenfuss@login.meteo.physik.uni-muenchen.de:
Ergebnisse zurückholen: rsync -a -v Paul.Ockenfuss@login.meteo.physik.uni-muenchen.de:SimulationGit/NamederErgebnisse.results . <=Punkt: legt Ergebnisse in akt. Verzeichnis

SSHFS:
sshfs Paul.Ockenfuss@login.meteo.physik.uni-muenchen.de:/home/p/Paul.Ockenfuss Ordner_wo_der_Baum_eingehängt_werden_soll




######################################################zsh configurations############################
source ~/.zshrc #reload zshrc
#Change colors of command prompt:
host_color="%F{green}"
username_color="%F{blue}"
path_color="%F{blue}"
PROMPT="${username_color}$USERNAME%f@${host_color}%B%m%b%f ${path_color}%B%~%b%f > "




