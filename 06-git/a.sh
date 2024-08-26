#!/bin/bash

# Scenario-1
mkdir -p scenario1
cd scenario1
git init
git config --global user.name Shiva
git config --global user.email sh.ramezani94@gmail.com
echo 'This is initial content of README'>README.md
git add README.md
git commit -m "Initial commit"
echo'==============================================='

# Scenario-2
git branch feature-branch
git checkout feature-branch
echo 'Iinitial content of feature file'>feature.txt
git add feature.txt
git commit -m "Added feature.txt file"
echo'==============================================='


# Scenario-3
echo '**NOTE**: Create the app.py file and commit beforehand'
git blame app.py | grep 'def process_data'
COMMIT_ID=$(git blame app.py | grep 'def process_data' | cut -d ' ' -f 1)
git show $COMMIT_ID
echo'==============================================='


# Scenario-4
git clean -n -d
git clean -f -d
echo'==============================================='


# Scenario-5
echo '**NOTE**: do not override the ssh key if it is already created'
ssh-keygen
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_*.pub
# Add the public key to the github repo
ssh -T git@github.com
echo'==============================================='


# Scenario-6
echo '**NOTE**: Create a clean repository on github (named MLOps_HW06)'
git remote add origin git@github.com:shramezani/MLOps_HW06.git
git checkout master
git branch -M main
git push -u origin main
# Go to the feature-branch and push it to the repo
git checkout feature-branch
git push origin feature-branch
echo'==============================================='


# Scenario-7
git checkout main
git merge feature-branch
git push origin main