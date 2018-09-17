# :grin:__PERSONAL BLOG__:grin:

# __AUTHOR: BRIGHTON ASUMANI__

# __ABOUT APPLICATION__
> this is an application that enables a user to sign and create a blog of his choice
> other users can be able to log in and comment your account.


# DEPLOYMENT TO HEROKU
1. $ heroku apps:destroy
> This removes your application so that we can start a fresh

2. $ heroku create <app>
> to create the application name

3. $ heroku addons:create heroku-postgresql:hobby-dev
> to create a new postgresql in the heroku database which is an addons application...i think..but the application will
not have your current data in your localhost

4. $ heroku run python3.6
> just to make it clear the application we would like to make in the heroku website will not be based in your localhost..it will be in the heroku database so your DATABASE_URL will >
> change.Looking like it will be encrypted or something.that is why we are running run python.

__we first import the os to get the necessary methods__
* import os
* os.environ.get("DATABASE_URL")
* you will get a foreign url like
> 'postgres://sahkwiwajjbmmm:40aea754da09ca490ed37e87c04aa36b931a04aa1713569561ab9d062c8c0131@ec2-54-235-196-250.compute-1.amazonaws.com:5432/d3f9jva5utjk0t'
> this is a good sign....it means progress
> Then paste it to the exports in the start.sh

> **export DATABASE_URL='postgres://komkrhtvhkqhpf:d1f780c5d2f7b58754ef26f4b85a8dbd6934d59cba70f8400ffca2845f5bb1b7@ec2-54-227-247-225.compute-1.amazonaws.com:5432/d6bgqi19ennurv'
python3.6 manage.py server**

> afterward we do this in the ProdConfig function in the config.py this line of code
> class ProdConfig(Config):
>   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
> and this will help you to recieve the localhost in Heroku.
> we then run this in our terminal after doing the git stuff...
> $ git add .
> $ git commit -m "Deploying to heroku"
> $ git push heroku master
> $ heroku run python3.6 manage.py shell
> this will head us to our shell where we need to create the db so as to run it right?
> db.create_all()
> exit()
> now we have created our database so we will need to export everything to our heroku
> if you had exports such as
> MAIL,PASSWORDS,SECRET_KEY
> $ heroku config:set <the line of export>
> the line of export may be like SECRET_KEY='MoringaSchool'
> PLease make sure you have no error
> to confirm if your psql is working run
> $ heroku pg:psql

***for any queries please contact @ asumanibrighton@gmail.com***
