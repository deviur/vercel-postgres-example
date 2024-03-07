# .bash_history
## Creating a project
```shell
git init
git add .
git commit -m'Init commit'
git remote add origin git@gitflic.ru:deviur/vercel-postgres-example.git
git push -u origin --all
git push -u origin --tags
```
## Creating a flask application
```shell
pip install --upgrade pip
pip install flask
pip freeze > requirements.txt
export FLASK_APP=index.py
echo $FLASK_APP  # --> index.py
flask run  # Checking that everything is working and press Ctrl+C to exit.
# Do commit
git status
git add .
git commit -m'Added hello world html page'
git push --set-upstream origin master
```