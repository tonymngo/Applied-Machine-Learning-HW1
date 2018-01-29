#!/bin/sh
mkdir repository
cd repository
git init

touch 1
git add 1
git commit 1 -m "Add file 1"

touch 2
git add 2
git commit 2 -m "Add file 2"

touch 3
git add 3
git commit 3 -m "Add file 3"

touch 4
git add 4
git commit 4 -m "Add file 4"

touch 5
git add 5
git commit 5 -m "Add file 5"

git checkout HEAD~4
git branch feature
git checkout feature

touch 6
git add 6
git commit 6 -m "Add file 6"

touch 7
git add 7
git commit 7 -m "Add file 7"

touch 8
git add 8
git commit 8 -m "Add file 8"

git checkout master
git rebase HEAD~2 --onto feature

git checkout HEAD@{12}
git branch debug
git checkout debug

touch 9
git add 9
git commit 9 -m "Add file 9"

git reflog > ../reflog.txt
