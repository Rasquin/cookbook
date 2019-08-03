# HERE IS AN EXAMPLE SCHEMA TO CREATE IN MONGODB

#{% if allergen['allergen_name'] == recipe['recipe_allergens'][0] %}
#<p>{{allergen['allergen_name']}} -----{{recipe['recipe_allergens']}}</p>

# Recipe Schema:
    
# {
#     "_id": "object_id_fkgjfg73kj48277694578586_58769",
#     "name": string
#     "author": string
#     "category": string
#     "image_url": string
#     "allergens": [],
#     "timestamp": 4387563487568
#     "ingredients": [],
#     "method": [],
#     "likes": 0,
#     "dislikes": 0,
#     "liked_by": [],
#     "disliked_by": []
# }

# RECIPE EXAMPLE:
{
    "_id": "object_id_fkgjfg73kj48277694578586_58769",
    "name": "Recipe Name blah blah blah",
    "author": "User1",
    "category": "Italian",
    "image_url": "https://www.imgur.com/hg4jhdujd",
    "allergens": [
        "nuts",
        "milk",
        "eggs",
    ],
    "timestamp": "875873768764", # Unix epoch time - look into python library called datetime (datetime.now())
    "ingredients": [
        {
            "ing_name": "eggs",
            "ing_amount": "2",
            "ing_unit": "units"
        },
        {
            "ing_name": "milk",
            "ing_amount": "2",
            "ing_unit": "cups"
        },
    ],
    "method": [
        {
            "step_num": "1",
            "step_description": "crack eggs into bowl and beat with milk",
            "additional_instructions": [
                "additional thing 1",
                "additional thing 2",
                "additional thing 3"
            ]
        }
    ],
    "likes": 0,
    "dislikes": 0,
    "liked_by": [
        "user1"
    ],
    "disliked_by": [
        "user2",
        "user3"
    ]
}

# USERS TABLE:

{
    "_id": "object_id_fkgjfg73kj8338728586_58769",
    "username": "user1",
    "password": "A75KSBFJFF7K48SJJHAAYC76CJ3JXSGYAHFGHTS763JDHGFAGFKHFDK" # bcrypt can hash this
}







# To access an ingredient:
recipe = mongo.db.recipes.find(name="Recipe Name blah blah blah") #This will be the recipe object from above
ingredients = recipe.ingredients # This will be the ingredients object for this recipe

for ingredient in ingredients:
    print(ingredient.ing_name)
    print(ingredient.ing_amount)
    print(ingredient.ing_unit)
    
method = recipe.method # This will be the ingredients object for this recipe
for step in method:
    print(method.step_num)
    print(method.step_description)
    
if "milk" in recipe.allergens:
    pass
    # reject this recipe
    
# To increment or decrement likes or dislikes:
if not user.username in recipe.liked_by:
    if user.username in recipe.disliked_by:
        recipe.disliked_by.remove(user.username)
        recipe.disliked_by -= 1
    recipe.likes += 1
    recipe.liked_by.append(user.username)
else:
    # return some error
    
recipe.dislikes -= 1

# To check if user is authenticated in your templates:
{% if request.user.is_authenticated %}
    <button>Like</button>
    <button>Disike</button>
    <button>Edit</button>
    <button>Delete</button>
{% endif %}

@app.route('/get_recipes')
def get_recipes():
    categories=mongo.db.categories.find()
    recipes=mongo.db.recipes.find()
    for category in categories:
        for recipe in recipes: 
            if category.category_name == recipe.category_name:
                category.number_of_recipes += 1
        
    return render_template("recipes.html", recipes=recipes, categories=categories)
