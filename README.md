environment setup
```git clone https://github.com/Hustlesgp/Hustle.git```

if already forked, you can update your local repo with the the master by
```git fetch upstream```
```git checkout master```
```git merge upstream/master```
(I think. some one try and lmk if this is correct LOL)

Dependencies required:
```pip install flask```
```pip install flask-wtf```
```pip install flask-sqlalchemy```


Navigate your terminal to the root folder
if on windows:
```set FLASK_APP=app.py```
```flask run``` to view the webpage

after coding,
u can use ```git status``` anytime to check what u have yet to stage/commit
```git add -A``` to stage everything
```git commit -m "whatever comments u want to put to describe this update"``` to commit the changes
```git push``` to upload the files to your forked repo
then send a pull request to merge with the master
