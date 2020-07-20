# Tipps for daily Linux work
Also includes a lot of useful snippets when working with the command line

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tipps for daily Linux work](#tipps-for-daily-linux-work)
- [Linux General](#linux-general)
  - [Permissions in Linux](#permissions-in-linux)
  - [User Handling](#user-handling)
  - [Process Handling](#process-handling)
  - [Links](#links)
  - [Packages](#packages)
  - [Printing](#printing)
  - [Searching](#searching)
  - [SVN](#svn)
  - [PDF](#pdf)
  - [ssh](#ssh)
    - [sshfs](#sshfs)
    - [scp](#scp)
    - [rsync](#rsync)
  - [gpg2](#gpg2)
  - [Everyday commands](#everyday-commands)
- [External Devices](#external-devices)
  - [Bluetooth](#bluetooth)
- [Change colors of command prompt:](#change-colors-of-command-prompt)

<!-- /code_chunk_output -->

bash in general: there are various types of shells: login, interactive, non-interactive
if a bash script is executed, this is usually done in a non-interactive shell. Therefore, custom commands from the .bashrc or .zshrc are not available there!

# Linux General
* What is a kernel? C't Articles: https://www.heise.de/select/ct/2019/16/softlinks/yzpg?wt_mc=pred.red.ct.ct162019.174.softlink.softlink
```bash
#Change kernel parameters at runtime
cd /proc/sys #Here, kernel parameters are stored
sysctl -a#list all parameters with value
sysctl -w parameter=value #make a non-persistent change (reset by reboot)
#persistent changes can be made by modifying the .conf files in /etc/sysctl.d/
```
* What are all the top level files in linux for: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard

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

## Process Handling
```shell
top -u User.Name #Show Interactive process overview
kill -HUP -1 #send SIGHUP ("Hang up") signal to all processes, the "friendly" request for termination
kill -KILL <pid> #send SIGKILL: process cannot ignore this signal
```

## Links
ln -s Source Destination#create symbolic link
readlink [-f]#get destination of existing link

## Packages
Using a package manager:
```bash
man apt #Good overview without details!
sudo apt install package #Install package
sudo apt update; sudo apt upgrade #update list and upgrade all packages
apt show neovim #Show package information (version, description, etc.)
```
Manually: put them into or create a link in e.g. /usr/bin/local. Meanwhile, many projects provide an AppImage which runs on most linux systems without installation. I collect them e.g. in ~/Software and create a link to a folder within the $PATH.


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
qpdf --encrypt pwd_user pwd_owner 256 -- A.pdf A_encrypt.pdf #Encrypt a pdf with 256 bit
qpdf -decrypt pdffile_protected.pdf pdffile_notprotected.pdf #Remove read only e.g. to make annotations to the pdf
pdfcrop in.pdf out.pdf #Crop all white space around the content in a pdf
```
## ssh
Usual directory: `~/.ssh`. There, you find your private key (`id_rsa`, keep it safe!) and your public key (`id_rsa.pub`). To use it for automatic login on a server, the public key must be added in the servers `.ssh/known_hosts` file. Therefore, you need to provide another method of authentification to the server, like a password or send an email to the admin, whatever. The usual way is to use ssh-copy-id, which automatically copies your public key in the servers known_hosts list (using e.g. password authentification). Now, the server trusts everyone who can prove to have the private key to the public one in known_hosts (Imagine the server encrypting a test message and sending it to the client. If the client can decrypt the message and send it back (encrypted with e.g. the servers public key, of course), the client can be trusted). 
```bash
ssh-keygen -t rsa -b 4096 -C "p-necko@t-online.de" #Generate a key public private key pair
ssh-copy-id -i id_rsa.pub My.Loginname@some.server.de #Add public key to server known_hosts
ssh -X User@ServerAddress #Now log in to server (use -X to enable X11 forwarding)
```
Config file for ssh. Use it for configuration, abbreviation of long names, etc.
```shell
Host MyNickname
  HostName ServerAddress
  User MyLoginNameOnTheServer
```
Control Master: Allows you to use one tcp connection for multiple ssh sessions. Has the advantage that you need to login only once!
```shell
Host MyNickname #Use "Host *" if you want it always
  controlmaster auto #enable it
  ControlPath  ~/.ssh/sockets/%r@%h-%p #files with the sockets will be created here. Can be any folder, e.g. in \tmp\... Create .ssh/sockets manually if not existent
  ControlPersist  600 #if you log out on the master session, the connections remains this many seconds open in background if other subsession are still connected. This allows a re-login without a blocked terminal, if you accidentally logged out.
```
### sshfs
```bash
sshfs -o idmap=user -o uid=$(id -u) -o gid=$(id -g) My.Loginname@some.server.de:/folder/on/server ~/Work #Usermapping: Map Ownership from remote user to current user
fusermount -uz ~/Mounts/Remote #Unmount directory "Remote"
killall -9 sshfs #If stuck :)
```
### scp
```bash
scp Path/fileTocopy user@university_computer:File/path/#Copy files via ssh from one computer to other
```
### rsync
```bash
rsync -a -v --exclude=".*" SimulationGit My.Loginname@server.de:
Ergebnisse zurückholen: rsync -a -v My.Loginname@UniversityLogin.de:SimulationGit/NamederErgebnisse.results . 
```
## gpg2
GnuPG, where pgp is 'pretty good privacy'. Use it to encrypt or decrypt files.
Working principle: The basis is the usual principle of asymmetric encryption. Like e.g. ssh, I have a public key and a private key, which is ideally additionally protected with a password. When creating, it is useful to create an additional revocation certificate. This certificate can only be created with the private key available, but afterwards it can be used to designate the key as invalid on a key server, even if the private key is lost (or compromised). Therefore, try to keep it safe as well.
```bash
gpg2 -k #list public keys in keyring
gpg2 -full-gen-key #create key pair
gpg2 --delete-secret-key <ID> #delete public and private key
gpg2 --keyserver 'pgpkeys.eu' --search-keys 'Prename Name' #Search key in web of trust. Server list: https://www.sks-keyservers.net/status/
gpg2 --recv-keys <ID> #download key from server
gpg2 --refresh-keys [ID] #refresh key (all if no ID given)
gpg2 -e -r Name1 -r Name2 File.txt #Encrypt file for recipients Name1, Name2. Use -a to get result as ascii instead of binary.
gpg2 -d -o Output.txt File.txt.asc #Decrypt file. 
gpg2 -b -a File.txt #Make a separate signature for File.txt
gpg2 --verify File.txt.asc #Verify signature. Without second argument, it is assumed in 'File.txt'
```
Web of Trust: Problem: I have a public key, but do I know that it really belongs to the person which owns the corresponding email address and name? (i.e. that person has the private key?) I can either: a) Ask the person itself for a proof and then trust this key, or b) ask anyone else who I trust that this key is trustworthy. The latter is the idea of the web of trust. There are 5 trust levels which you can assign to keys and which determine, whether gpg will trust new keys which are signed by one of the trusted keys. Usually, use 3, only if you really trust a person use 4. 5 is only for yourself.
```bash
gpg2 --edit-key Name #Start key editing
>sign #Sign this key if you are sure that it belongs to the person with this name and email. This is useful for others, which trust you such that they can also trust this key.
>trust #Choose a level of trust associated with this key. This is useful for you, because now gpg2 trusts other keys which are signed by this key.
>save #save your changes
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












######################################################zsh configurations############################
source ~/.zshrc #reload zshrc
#Change colors of command prompt:
host_color="%F{green}"
username_color="%F{blue}"
path_color="%F{blue}"
PROMPT="${username_color}$USERNAME%f@${host_color}%B%m%b%f ${path_color}%B%~%b%f > "




