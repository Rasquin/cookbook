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
    
    
#-------------------------------------------------------------- Managment of Categories

#---- Adding a new category
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

#---- Inserting a new category
@app.route('/inser_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    print (request.form.to_dict())
    return redirect(url_for('cookbook'))
    
#---- Editing a new category
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    the_category =  mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template('editcategory.html', category=the_category)

#---- Updating a  category
@app.route('/update_category/<category_id>', methods=["POST"])
def update_category(category_id):
    categories = mongo.db.categories
    categories.update( {'_id': ObjectId(category_id)},
    {
        'category_name':request.form.get('category_name'),
        'number_of_recipes':request.form.get('number_of_recipes')
    })
    return redirect(url_for('cookbook'))
    
#---- Deleting a  category
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('cookbook'))
    
#-------------------------------------------------------------- Display of  Recipes
@app.route('/get_recipes/<criteria>')
def get_recipes(criteria):
    the_criteria=  mongo.db.categories.find_one({"_id": ObjectId(criteria)})
    all_recipes =  mongo.db.recipes.find()
    return render_template("recipesbycategory.html", recipes=all_recipes,  criteria=the_criteria)

@app.route('/all_recipes')
def all_recipes():
    return render_template("allrecipes.html", recipes=mongo.db.recipes.find())
 


@app.route('/the_recipe/<recipe_id>')
def the_recipe(recipe_id):
    the_recipe=  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
   # allergens= the_recipe.allergens
    #ingredients= the_recipe.ingredients
    #method= the_recipe.method
    return render_template("recipe.html", recipe=the_recipe)

#-------------------------------------------------------------- Adding New Recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', categories=mongo.db.categories.find(), difficulty=mongo.db.difficulty.find(), cuisines=mongo.db.cuisines.find(), allergens=mongo.db.allergens.find())
    
@app.route('/inser_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    print (request.form.to_dict())
    return redirect(url_for('cookbook'))

#-------------------------------------------------------------- Editing Recipe

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    all_cuisines = mongo.db.cuisines.find()
    all_difficulties = mongo.db.difficulty.find()
    all_allergens = allergens=mongo.db.allergens.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories, cuisines=all_cuisines, difficulty=all_difficulties, allergens=all_allergens)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'author':request.form.get('author'),
        'author_country': request.form.get('author_country'),
        'recipe_category': request.form.get('recipe_category'),
        'number_of_portions':request.form.get('number_of_portions'),
        'difficulty_level':request.form.get('difficulty_level'),
        'recipe_description':request.form.get('recipe_description'),
        'cuisine': request.form.get('cuisine'),
        'recipe_allergens': request.form.get('recipe_allergens'),
        'recipe_image':request.form.get('number_of_portions'),
        'ingredients':request.form.get('ingredients'),
        'method':request.form.get('method'),
        'likes': request.form.get('likes'),
        'dislikes': request.form.get('dislikes'),
        'liked_by':request.form.get('liked_by'),
        'disliked_by':request.form.get('disliked_by'),
        'views':request.form.get('views'),
        'timestamp':request.form.get('timestamp')
    })
    return redirect(url_for('cookbook'))
    
#-------------------------------------------------------------- Delete Recipe

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('cookbook'))
    
#-------------------------------------------------------------- Managing Categories
    


    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)