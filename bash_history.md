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
## Deploying to Vercel
```shell
vercel
vercel -d dev # Checking that this is working and press Ctrl+C to exit.
vercel --prod # to deploy the app
```
## Getting Started with Vercel Postgres
[Read more here](https://vercel.com/docs/storage/vercel-postgres/quickstart)
```shell
# This step requires you to link postgres database 
# to the project in your personal Vercel account.
vercel env pull .env.development.local
source .env.development.local
echo $POSTGRES_USER  # --> default
```
## Connecting the app to the database
```shell
pip install Flask-SQLAlchemy
pip install psycopg2-binary
pip freeze > requirements.txt
vercel -d dev # Checking that this is working and press Ctrl+C to exit.
vercel --prod # to deploy the app
git status
git add .
git commit -m'Added user table'
git push
```
