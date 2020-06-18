# Git Tipps
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Git Tipps](#git-tipps)
- [General](#general)
  - [Branches](#branches)
  - [Push/Pull](#pushpull)
  - [Miscellaneous commands](#miscellaneous-commands)
- [Rename a file or folder](#rename-a-file-or-folder)
- [Web frontends](#web-frontends)
  - [Github](#github)

<!-- /code_chunk_output -->

Tutorial: https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud

# General
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
## Miscellaneous commands
#Rename a file or folder
git mv Old/ New/




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

