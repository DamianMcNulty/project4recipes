# Python Flask web application

| <a href="https://github.com/DamianMcNulty/project4recipes/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/project4recipes.svg?style=social" alt="GitHub stars"> </a> 	| [![Travis CI Testing](https://travis-ci.org/DamianMcNulty/project4recipes.svg?branch=master)](https://travis-ci.org/DamianMcNulty/project4recipes) 	|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------	|

## Goal
>To create a Cook book using a python and flask web application

## Table of Contents
- [Description](#description)
- [UX](#ux)
- [Technologies Used](#technologies-used)
    - HTML5
    - CSS3
    - Python
    - Flask
- [Development Environment](#development-environment)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
- [LICENSE](#license)

## Description
[(Back to top)](#table-of-contents)

## UX
[(Back to top)](#table-of-contents)

### User Stories

1. A user can input an ingredient
2. A user can input categories
3. A user can select multiple ingredients
4. A user can input a recipe
5. An ingredient is stored in a database
6. A recipe is stored in a database
7. A category is stored in a database
8. A user can filter a list of recipes based on various criteria, ordered by number of views or upvotes, pagination, showing some summary statistics, number of matching recipes, number of new recipes
9. A user can view detailed info about each recipe
10. A user can edit and delete recipes
11. A user can log in with a username

### [Wireframe prototype](https://xd.adobe.com/view/8b0bf512-6a50-492f-46c1-07d633b33a10-fd3a/)

### [Design Specs](https://xd.adobe.com/spec/3280e430-8e27-419d-6f08-fe04f9f7d897-44b1/)

### Design Demonstration 

<img src="https://github.com/DamianMcNulty/project4recipes/blob/master/static/img/AdobeXDCC13_12_2018Project4Re.gif" width=30% height=350px alt="Demonstration">

## Technologies Used
[(Back to top)](#table-of-contents)
1. [![HTML5](https://github.com/DamianMcNulty/my-first-website/blob/master/img/HTML5_logo_and_wordmark.svg)](https://en.wikipedia.org/wiki/HTML5) 

2. [![CSS3](https://github.com/DamianMcNulty/my-first-website/blob/master/img/CSS3_logo_and_wordmark.svg)](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  

3. [![Git](https://github.com/DamianMcNulty/my-first-website/blob/master/img/Git-logo.svg)](https://en.wikipedia.org/wiki/Git)  

## Development Environment

### windows
```pip install virtualenv
   python -m virtualenv env
   .\env\Scripts\activate
   pip install -r requirements.txt
   python runserver.py
   .\env\Scripts\deactivate
```
### Cloud9
```
    sudo pip3 install -r requirements.txt
    export DEVELOPMENT=True
    export SECRET_KEY="..."
    export MONGO_DBNAME="..."
    export MONGO_URI='...'
    sudo pip3 install pymongo
    sudo pip3 install Flask-PyMongo
    pip3 freeze --local > requirements.txt
    echo 'alias run="python3 ~/workspace/project4recipes/runserver.py"' >> ~/.bash_aliases
    source ~/.bash_aliases
    run
```

.env
```
    echo "SECRET_KEY='...'" > .env
    echo "export DEVELOPMENT=True" >> .env
    echo 'export MONGO_DBNAME="..."' >> .env
    echo 'export MONGO_URI="..."' >> .env
    echo ".env" >> .gitignore
```

## Deployment
[(Back to top)]
1. sudo pip3 install flask
2. pip3 freeze --local > requirements.txt
1. heroku login
2. heroku create damianmcdev1-project4recipes --region eu
3. pip3 freeze --local > requirements.txt
4. echo web: python runserver.py > Procfile
5. git push heroku master
7. heroku config:set IP="0.0.0.0"
8. heroku config:set PORT="8080"
9. heroku config:set SECRET_KEY="..."
10. heroku config:set MONGO_DBNAME="..."
10. heroku config:set MONGO_URI="..."

 
## Credits
[(Back to top)](#table-of-contents)
1. [Online Converter](https://www.onlineconverter.com/mp4-to-gif)
2. [Easy Table Filter TavoQiqe](https://bootsnipp.com/snippets/featured/easy-table-filter)

## License:

See [LICENSE](LICENSE).
