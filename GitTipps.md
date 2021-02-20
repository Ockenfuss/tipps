# Git Tipps
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Git Tipps](#git-tipps)
- [General](#general)
  - [Setup](#setup)
  - [Branches](#branches)
  - [Push/Pull](#pushpull)
  - [Rebase](#rebase)
  - [Miscellaneous commands](#miscellaneous-commands)
- [Rename a file or folder](#rename-a-file-or-folder)
- [Web frontends](#web-frontends)
  - [Github](#github)
- [SVN Tipps](#svn-tipps)

<!-- /code_chunk_output -->

Tutorial: https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud

# General

## Setup
```bash
git config --global user.name 'Name'
git config --global user.email 'a@b.com'
git config --global core.editor vim # standard is $EDITOR evn. variable
git config --list #see all settings
```

## Branches
```bash
git branch -a #Show available branches
git checkout -b newBranch #Create a new branch
```

## Push/Pull
```bash
git push origin master #Push the current branch to the remote branch 'master' on the remote repository 'origin' ('origin' is just a name for the remote url and can be customized)
git push -f origin master #Force push. Dangerous!
```
## Rebase
Suppose two branches, e.g. your local master and origin/master diverged after a certain commit. In this case, `git rebase` applies your local commits on top of the commits on origin master. The result looks like you would have done all your coding after the changes in origin happened and not in parallel.
```bash
#do some changes locally and commit them
git add ...
git commit ...
git fetch #fetch remote branches
git rebase origin/master #Apply the commits of your current branch (master) on top of origin/master
```

## Miscellaneous commands
#Rename a file or folder
```bash
git mv Old/ New/
```




# Web frontends
## Github
Set up the respository
```bash
git clone https://github.com/Ockenfuss/dotfiles.git #Download repository from github, or alternatively:
git remote add origin git@github.com:Ockenfuss/ComRun.git #Load existing repository to github (create an empty repository there first)
git push -u origin master #After adding the link
git remote set-url origin git@github.com:Ockenfuss/dotfiles.git #if we want to change e.g. from https to ssh
```


Neuen ssh key bei github registrieren:
https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent


# SVN Tipps
```bash
svn info #get info like upstream url
svn checkout url #checkout repository
svn status #get status of repo
svn up #update repository
svn switch --relocate OldURL NewURL
```
