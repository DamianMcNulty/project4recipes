from os import environ
from datetime import datetime
import math

from flask import Flask, render_template, redirect, request, url_for

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.secret_key = environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/')
@app.route('/home/<int:page>')
def get_recipes(page=1):
    num=5
    total=mongo.db.recipes.find({}).count()
    numOfPages=math.floor(total/num)
    pagerange=range(numOfPages)
    """Renders the home page."""
    return render_template(
       'recipes.html',
        title='Home Page',
        year=datetime.now().year,
        page=page,
        num=num,
        pagerange=pagerange,
        recipes=mongo.db.recipes.find().sort("likes", -1).skip((page-1)*num).limit(num),
        categories1=mongo.db.categories.find(),
        ingredients1=mongo.db.ingredients.find()
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
    recipe_name = request.form['recipe_name']
    category_name = request.form['category_name']
    recipe_ingredients = request.form.to_dict(flat=False)['recipe_ingredients']
    recipe_instructions = request.form.to_dict(flat=False)['recipe_instructions1']
    recipe_instructions2 = request.form['recipe_instructions2']
    recipe_instructions3 = request.form['recipe_instructions3']
    likes = 0
    if(recipe_instructions2 != ""):
        recipe_instructions.append(recipe_instructions2)
    if(recipe_instructions3 != ""):
        recipe_instructions.append(recipe_instructions3)
    recipe={'recipe_name': recipe_name, 'category_name': category_name,'recipe_ingredients': recipe_ingredients, 'recipe_instructions': recipe_instructions, 'likes': likes}
    recipes.insert_one(recipe)
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    _categories = mongo.db.categories.find()
    _ingredients = mongo.db.ingredients.find()
    return render_template('edit_recipe.html', recipe=_recipe, categories2=_categories, ingredients2=_ingredients)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipe_name = request.form['recipe_name']
    category_name = request.form['category_name']
    recipe_ingredients = request.form.to_dict(flat=False)['recipe_ingredients']
    recipe_instructions = request.form.to_dict(flat=False)['recipe_instructions1']
    recipe_instructions2 = request.form['recipe_instructions2']
    recipe_instructions3 = request.form['recipe_instructions3']
    likes = int(request.form['likes'])
    if(recipe_instructions2 != ""):
        recipe_instructions.append(recipe_instructions2)
    if(recipe_instructions3 != ""):
        recipe_instructions.append(recipe_instructions3)
    recipe = {'recipe_name': recipe_name, 'category_name': category_name, 'recipe_ingredients': recipe_ingredients, 'recipe_instructions': recipe_instructions, 'likes': likes}
    recipes.update({'_id': ObjectId(recipe_id)}, recipe)
    return redirect(url_for('get_recipes'))

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

@app.route('/recipe_detail_like/<recipe_id>', methods=['POST'])
def recipe_detail_like(recipe_id):
    num = 1
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, {"$inc": {"likes": num} } )
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe_detail.html',
    recipe=recipe)
    return redirect(url_for('recipe_detail_like'))

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