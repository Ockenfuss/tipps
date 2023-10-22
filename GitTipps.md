# Git Tipps

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Git Tipps](#-git-tipps)
- [General](#-general)
  - [Setup](#-setup)
  - [Branches](#-branches)
    - [Merging branches](#-merging-branches)
  - [Push/Pull](#-pushpull)
  - [Rebase](#-rebase)
  - [Submodules](#-submodules)
  - [Miscellaneous commands](#-miscellaneous-commands)
- [Web frontends](#-web-frontends)
  - [Github](#-github)
- [SVN Tipps](#-svn-tipps)
  - [Checkout](#-checkout)

<!-- /code_chunk_output -->



Tutorial: https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud

# General

## Setup
```bash
git config --global user.name 'Name'
git config user.email 'user@users.noreply.github.com' #It is adivisable to use the provided noreply address, if you want to push to Github
git config --global user.email 'a@b.com'
git config --global core.editor vim # standard is $EDITOR evn. variable
git config --list #see all settings
```

## Branches
```bash
git branch #show all local branches with active one marked by '*'
git branch -a #Show available branches
git checkout -b newBranch #Create a new branch
git switch -c newBranch #switch to a new branch (-c: create if not existent). Your unstaged changes will be taken with you to the new branch. Like git checkout <branchname>.
git branch -d branchname #Delete a branch (only if its commits are merged in another branch before)
git branch --set-upstream-to=origin/<branchname> <local_branchname> #set the local branch to track a remote branch. This way, you don't have to type 'git pull <remote> <local> everytime'
```

### Merging branches
```bash
git checkout main #First, checkout the merge-receiving branch, i.e. the branch you want to have a merge commit introducing the changes from the other branch.
git fetch #Make sure you have the latest information from the remote repository
git pull #Make sure main, the merge receiving branch, is updated.
git merge <other-branch> #merge the other branch into main.
git branch -d <other-branch> #Delete the other branch. With -d, git deletes only if everything is merged into main. (-D would delete in every case - dangerous!)
```

## Remotes
```bash
git remote -v #show remote destinations with urls
git remote add name url #add remote
git remote set-url name url #change url of existing remote
git remote rename old new #rename remote
git remote remove name #remove remote

```

## Push/Pull
```bash
git fetch #Download remote changes to see what has happened remotely, but do not touch the state of your local content.
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

## Submodules
```bash
git clone --recursive <url> #clone repo including submodules
git submodule update --init -- <specific relative path to submodule> #clone only one specific submodule
```

## Miscellaneous commands
```bash
git mv Old/ New/ #Rename a file or folder
```




# Web frontends
## Github
### General
It is advisable not to use your private email address for commits pushed to Github! Github provides you with a special email address, which you can use with you git. Look it up in your account.
```bash
git config --global user.email "123456+username@users.noreply.github.com"
```
If you need to rewrite some comments, use:
```bash
git rebase -i HEAD~3 #do an interactive rebase of the last 3 comments
#chose 'edit' for all comments you want to change in the editor, that opens
git commit --ammend --reset-author #use the new default author for the first comment
git rebase --continue #continue to next comment
#...
```

Set up the respository
```bash
git clone https://github.com/Ockenfuss/dotfiles.git #Download repository from github, or alternatively:
git remote add origin git@github.com:Ockenfuss/ComRun.git #Load existing repository to github (create an empty repository there first)
git push -u origin master #After adding the link
git remote set-url origin yourname@github.com:Ockenfuss/dotfiles.git #if we want to change e.g. from https to ssh
```


Neuen ssh key bei github registrieren:
https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent


# SVN Tipps
## Checkout
```bash
svn checkout --username myname url #checkout repository
svn checkout --force url #This allows you to checkout into an existing, unversioned folder structure. Any differences to the repo will be visible as "local changes" after the checkout, which you can either commit or revert to the version of the repo.
```
```bash
svn info #get info like upstream url
svn status #get status of repo
svn up #update repository
svn up -r 123 file.txt #checkout a specific version of a file
svn switch --relocate OldURL NewURL
svn add file #Add new file for version control in the next commit. Unlike in git, this has to be done only when adding the file for the first time.
svn commit file.txt #commit changes. "-m logmessage" to specify the commit message
svn rm file.txt #remove a file and schedule it for deletion with the next commit
```
