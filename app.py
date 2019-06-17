import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')

@app.route('/cookbook')
def cookbook():
    return render_template("cookbook.html", recipes=mongo.db.recipes.find(),  categories=mongo.db.categories.find())
    
@app.route('/all_recipes')
def all_recipes():
    return render_template("allrecipes.html", recipes=mongo.db.recipes.find())
 
@app.route('/get_recipes/<category_id>')
def get_recipes(category_id):
    the_category=  mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    all_recipes =  mongo.db.recipes.find()
    return render_template("recipes.html", recipes=all_recipes,  category=the_category)

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', categories=mongo.db.categories.find())


#@app.route('/edit_recipe/<recipe_id>')
#def edit_task(recipe_id):
#    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
#    all_categories =  mongo.db.categories.find()
#    return render_template('edit_recipe.html', recipe=the_recipe,
#                           categories=all_categories)

#@app.route("/recipe/<recipe_name>")
#def user(username):  
 #   return render_template("recipe.html")
    
@app.route('/get_categories')
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)