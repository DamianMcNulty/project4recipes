# Recipe Manager

| <a href="https://github.com/DamianMcNulty/project4recipes/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/project4recipes.svg?style=social" alt="GitHub stars"> </a> | [![Travis CI Testing](https://travis-ci.org/DamianMcNulty/project4recipes.svg?branch=master)](https://travis-ci.org/DamianMcNulty/project4recipes) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |

## Goal

> To create a Cook book using a python and flask web application

## Table of Contents

-   [Description](#description)
-   [UX](#ux)
-   [Technologies Used](#technologies-used)
-   [Development Environment](#development-environment)
-   [Local Testing](#local-testing)
-   [Deployment](#deployment)
-   [Credits](#credits)
    -   [Content](#content)
    -   [Media](#media)
    -   [Acknowledgements](#acknowledgements)
-   [LICENSE](#license)

## Description

[(Back to top)](#table-of-contents)

## UX

[(Back to top)](#table-of-contents)

### User Stories

1.  As a user, I can input an ingredient
2.  As a user, I can input categories
3.  As a user, I can select multiple ingredients
4.  As a user, I can input a recipe
5.  An ingredient is stored in a database
6.  A recipe is stored in a database
7.  A category is stored in a database
8.  A user can filter a list of recipes based on various criteria, ordered by number of views or upvotes, pagination, showing some summary statistics, number of matching recipes, number of new recipes
9.  As a user, I can view detailed info about each recipe
10. As a user, I can edit and delete recipes
11. As a user, I can log in with a username

### Design Demonstration

<img src="https://github.com/DamianMcNulty/project4recipes/blob/master/static/img/AdobeXDCC13_12_2018Project4Re.gif" width=30% height=350px alt="Demonstration">

## Technologies Used

1.  [HTML5](https://en.wikipedia.org/wiki/HTML5) 

2.  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  

3.  [Git](https://git-scm.com/)  

4.  [Github](https://github.com/)

5.  [Online Converter](https://www.onlineconverter.com/mp4-to-gif)

6.  [Site24x7 Link Checker](https://www.site24x7.com/link-checker.html)

7.  [HTML5 Validator](https://validator.w3.org/)

8.  [CSS3 Validator](https://jigsaw.w3.org/css-validator/)

9.  [Axe](https://chrome.google.com/webstore/detail/axe/lhdoppojpmngadmnindnejefpokejbdd?hl=en)

10. [Python 3.7.2](https://www.python.org/)

## Development Environment

[(Back to top)](#table-of-contents)

### windows

    pip install virtualenv
    python -m virtualenv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    python runserver.py
    .\env\Scripts\deactivate

### Cloud9

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

.env

    echo "SECRET_KEY='...'" > .env
    echo "export DEVELOPMENT=True" >> .env
    echo 'export MONGO_DBNAME="..."' >> .env
    echo 'export MONGO_URI="..."' >> .env
    echo ".env" >> .gitignore
    source .env

## Local Testing

[(Back to top)](#table-of-contents)

    npm i
    npm run cy:open

## Deployment

[(Back to top)](#table-of-contents)

    sudo pip3 install flask
    pip3 freeze --local > requirements.txt
    heroku login
    heroku create damianmcdev1-project4recipes --region eu
    pip3 freeze --local > requirements.txt
    echo web: python runserver.py > Procfile
    git push heroku master
    heroku config:set IP="0.0.0.0"
    heroku config:set PORT="8080"
    heroku config:set SECRET_KEY="..."
    heroku config:set MONGO_DBNAME="..."
    heroku config:set MONGO_URI="..."

## Research

[(Back to top)](#table-of-contents)

-   [Add many ingredients](https://stackoverflow.com/questions/45590988/converting-flask-form-data-to-json-only-gets-first-value)

## Credits

[(Back to top)](#table-of-contents)

-   [Easy Table Filter TavoQiqe](https://bootsnipp.com/snippets/featured/easy-table-filter)

## License:

See [LICENSE](LICENSE).
