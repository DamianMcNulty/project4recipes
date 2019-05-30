from os import environ
from datetime import datetime

from flask import Flask, render_template, redirect, request, url_for

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/')
@app.route('/home')
def get_recipes():
    page=1
    """Renders the home page."""
    return render_template(
       'recipes.html',
        title='Home Page',
        year=datetime.now().year,
        recipes=mongo.db.recipes.find().skip((page - 1)*5).limit(5),
        categories=mongo.db.categories.find(),
        ingredients=mongo.db.ingredients.find()
    )

@app.route('/add_category')
def add_category():
    """Renders the add category page."""
    return render_template(
        'add_category.html',
        title='Add Category',
        year=datetime.now().year,
        message='Add a category',
        categories=mongo.db.categories.find()
    )

@app.route('/add_ingredient')
def add_ingredient():
    """Renders the add ingredient page."""
    return render_template(
        'add_ingredient.html',
        title='Add ingredient',
        year=datetime.now().year,
        message='Add an ingredient',
        ingredients=mongo.db.ingredients.find()
    )

@app.route('/settings')
def settings():
    """Renders the settings page."""
    return render_template(
        'settings.html',
        title='Settings',
        year=datetime.now().year,
        message='Settings',
        recipes=mongo.db.recipes.find(),
        categories1=mongo.db.categories.find(),
        ingredients1=mongo.db.ingredients.find()
    )
    
@app.route('/add_recipe')
def add_recipe():
    """Renders the add recipe page."""
    return render_template(
        'add_recipe.html',
        title='Add Recipe',
        year=datetime.now().year,
        message='Add a recipe here',
        categories2=mongo.db.categories.find(),
        ingredients2=mongo.db.ingredients.find()
    )

@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = {'category_name': request.form['category_name']}
    categories.insert_one(category_doc)
    return redirect(url_for('settings'))

@app.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    ingredients = mongo.db.ingredients
    ingredient_doc = {'ingredient_name': request.form['ingredient_name']}
    ingredients.insert_one(ingredient_doc)
    return redirect(url_for('settings'))

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('add_recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/delete_ingredient/<ingredient_id>')
def delete_ingredient(ingredient_id):
    mongo.db.ingredients.remove({'_id': ObjectId(ingredient_id)})
    return redirect(url_for('settings'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('settings'))

@app.route('/recipe_detail/<recipe_id>')
def recipe_detail(recipe_id):
    return render_template('recipe_detail.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


if environ.get('DEVELOPMENT'):
    development = True
else:
    development = False

if __name__ == '__main__':
    HOST = environ.get('IP')
    if development:
        PORT = int(environ.get('C9_PORT'))
    else:
        PORT = int(environ.get('PORT'))
    app.run(HOST, PORT, debug=development)