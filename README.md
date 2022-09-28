# Recipe Manager

| <a href="https://github.com/DamianMcNulty/project4recipes/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/project4recipes.svg?style=social" alt="GitHub stars"> </a> | [![CircleCI](https://dl.circleci.com/status-badge/img/gh/DamianMcNulty/project4recipes/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/DamianMcNulty/project4recipes/tree/master) |
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
-   [LICENSE](#license)

## Description

[(Back to top)](#table-of-contents)

## UX

[(Back to top)](#table-of-contents)

### User Stories

1.  As a user, I can input a new ingredient, add it to the database and delete it.
2.  As a user, I can input a new category, add it to the database and delete it.
3.  As a user, I can input a new recipe, add it to the database and delete it.
4.  As a user, I can filter a list of recipes by meal.
5.  As a user, I can view detailed info about each recipe

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

### install

    pip install flask pymongo Flask-PyMongo
    pip3 freeze --local > requirements.txt

### windows

    setx /m DEVELOPMENT True
    setx /m SECRET_KEY "..."
    setx /m MONGO_DBNAME "..."
    setx /m MONGO_URI '...'
    pip install virtualenv
    python -m virtualenv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    python runserver.py
    .\env\Scripts\deactivate

## Local Testing

[(Back to top)](#table-of-contents)

    npm i
    python runserver.py
    npm run cy:open

    python test.py

## Deployment

[(Back to top)](#table-of-contents)

    git clone https://github.com/DamianMcNulty/project4recipes.git
    pip3 install -r requirements.txt
    heroku login
    heroku create damianmcdev1-project4recipes --region eu
    echo web: python runserver.py > Procfile
    heroku config:set IP="0.0.0.0"
    heroku config:set PORT="8080"
    heroku config:set SECRET_KEY="..."
    heroku config:set MONGO_DBNAME="..."
    heroku config:set MONGO_URI="..."
    git push heroku master

## Research

[(Back to top)](#table-of-contents)

-   [Add many ingredients](https://stackoverflow.com/questions/45590988/converting-flask-form-data-to-json-only-gets-first-value)
-   [add an active class to the current element with JavaScript](https://www.w3schools.com/howto/howto_js_active_element.asp)

## Credits

[(Back to top)](#table-of-contents)

-   [Easy Table Filter TavoQiqe](https://bootsnipp.com/snippets/featured/easy-table-filter)

## License:

See [LICENSE](LICENSE).
