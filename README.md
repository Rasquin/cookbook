# MONICA'S COOKBOOK - project III

Data Centric Development Milestone Project. This consist of a data-driven web application.
The  backend code and frontend form allow users to access, add, edit, store and delete 
cooking recipes, types of categories and cuisines.

This project is deployed at [Heroku](https://monicas-cookbook.herokuapp.com/)


## UX
This website has been designed to offer the users a nice experience at looking for
new recipes to try.The visitors of this website will be able to look for recipes
based on category, cuisine or difficulty level. Once selected the desired recipe,
the user will redirected to a new page where he/she will be able to see a picture 
of the recipe followed  by the recipe name, views, author, the author's country, 
the category, cuisine, description, portions, level of difficulty, possible allargens,
ingredients and method. 

- As a user, I would like a website that display the featured recipes, such as newest 
recipes or most viewed recipes. Then the home page of the site should display those
recipes in a place easy to locate.
 
- As a user, I may be interested in a specified category of recipe, I may find 
interesting how many recipes has each of the categories. Then the site should have
a section where it shows the different categories available and their respective
number of available recipes .

- As a user, I may be interested in a specified cuisine recipe, I may find 
interesting how many recipes has each of the types of cuisine. Then the site should have
a section where it shows the different cuisines available and their respective
number of available recipes.

- As a user, I may think that there are not enough categories/ cuisines to clasify 
the recipes, or that a name is misspelled or the category/cuisine is wrong. Then the site 
should allow the user add, edit the name or delete such category/cuisine.

- As a user, I could be interested in follow a recipe that would fit my skill as a cook.
Then the site should also display the recipes by level of difficulty.

- As user I would show more interest in taking a look on the most popular recipes when
a list of recipes is displayed. Then the website should display the recipes in 
order following a criteria such as number of views.

- As a user I would like to know as much as possible about the recipe I am interested in.
Then the website should give all relevant information about the requested recipe in 
a format that be friendly to the user.

- As a user, I would like to follow up this website through social media (pinterest, 
twitter or instagram) So I can be updated of new recipes or to know what the communuty is doing.
Then the website should contain link that allow the user to check its available social media.

## Features

This project works with databases collections (mongoDB Atlas). The backend of the 
project is centered in the app.py, from there are made all the routes of the priject.
The principal template of this project is the cookbook.html.  All the general html
code is donde in the base.html template, this one is shared by all the other templates
through the use of block-contents.


### Existing Features

**app.py** (backend) Here are imported all the neccesary libraries in order to make the 
caractheristics of the project work. There are a total of 24 routes, together they 
help to render templates, redirect to other template of make calculus of variables.
- Imported: os, from flask imported Flask, render_template, redirect, request, url_for. From flask_pymongo imported PyMongo. From bson.objectid imported ObjectId. From datetime imported datetime.
- Routes: 
   * '/cookbook': Home website
   * '/number_of_recipes_by_category': Calculating the number of recipe by each category.
   * '/add_category': Add new category.
   * '/inser_category', methods=['POST']: Inserting new category.
   * '/edit_category/<category_id>': Editing a new category.
   * '/update_category/<category_id>', methods=["POST"]: Updating a  category.
   * '/delete_category/<category_id>': Deleting a  category.
   * '/number_of_recipes_by_cuisine':  Calculating the number of recipe by each cuisine.
   * '/add_cuisine': Adding a new cuisine.
   * '/inser_cuisine', methods=['POST']: Inserting a new cuisine.
   * '/edit_cuisine/<cuisine_id>': Editing a new cuisine.
   * '/update_cuisine/<cuisine_id>', methods=["POST"]: Updating a  cuisine.
   * '/delete_cuisine/<cuisine_id>': Deleting a  cuisine.
   * '/number_of_recipes_by_difficulty': Calculating the number of recipe by levels of difficulty.
   * '/get_recipes_by_category/<category_id>': Display of Recipes by category.
   * '/get_recipes_by_cuisine/<cuisine_id>': Display of Recipe by cuisine.
   * '/get_recipes_by_difficulty/<difficulty_id>': Display of Recipes by Difficulty Level.
   * '/all_recipes': Display of all recipes.
   * '/the_recipe/<recipe_id>': Display of the requested reciped.
   * '/add_recipe': Adding New Recipe.
   * '/inser_recipe', methods=['POST']: Insertin a new recipe.
   * '/edit_recipe/<recipe_id>': Editing Recipe.
   * '/update_recipe/<recipe_id>', methods=["POST"]: Updating recipe.
   * '/delete_recipe/<recipe_id>': Deleting recipe.

**templates** There are 13 html templates. Each of them displays a different functionality
of this website.
- base: it has all the rehusable html that is share to all the other templates. Here 
 it is contained the navbar and the footer, here is added all the style-sheets and 
scripts.  The navbar allows the user to navegate through the different sections of the 
cookbook template, to check directly all recipes and/or add a new recipe. The footer
contains links to social media and copy-right text.
- cookbook: It is the home of the site.It has 5 sections
   * Home: Welcome to the website and invitation to the user to know 'what do they would like to eat today?
   * Newest and most viewed recipes: Each of the list contains the 3 recipes most relevant to the respective category.
   * Categories: Here a list of the current categories with recipes is displayed in order of more number of recipes to the less. If the category is empty won't be displayed.
   * Cuisinesies: Here a list of the current cuisines with recipes is displayed in order of more number of recipes to the less. If the cuisine is empty won't be displayed.
   * Dfficulty level: Here a list of the difficulty levels is displayed in order of more number of recipes to the less. 

- addcategory / addcuisine / addrecipe: All of them allow to the user to add the 
 respective feature. Each template gives the option to save or cancel the action.
    * addcategory: The user is requested to write the name for the new category. The number of recipes variable is fixed to 0 automatically.
    * addcuisine: The user is requested to write the name for the new cuisine type. The number of recipes variable is fixed to 0 automatically.
    * addrecipe: the user is requested to fill a form where he/she has to give the Recipe Name, Author, Author Country of Origin, Category, Cuisine, Description, Portions, Level of difficulty, Possible allergens, Ingredients, Image url and method. Variables such as timestamp or views are fixated automatically.
- allrecipes / recipesbycategory / recipesbycuisine / recipesbydifficulty: Display  of each criteria recipes a list  based on the number of views. The user can view, edit and/or delete the recipe. 
- editcategory / editcuisine / editrecipe: Edit the selected feature. The user can save chamges or cancel the action
- recipe: display the actual recipe.

**style** The bootstrap library was used to apply style. Besides there is the own style.
The project was made considering the "first small screen" principle, from there it
was adapted to larger sizes of screens.

**JavaScript** The project content the neccesary JS to make its components to work.
Some come from the bootstrap/ bootstrap-select functionality. There is also own JS 
to make the add/ edit recipe form works.
- Ingredients Add: jQuery that allow user to add a new ingredient to the list of ingredients
- Method Add: jQuery that allow user to add a new steep in to the method.

### Features Left to Implement
- Authentification of user, then only the registered user would be allowed to add recipes. And the site administrator would be to only one who could be able to delete or edit recipes.
- Pagination: eventually the site will gorup up and pagination for the recipes would be neccesary.
 
 
## Technologies Used

This project was made with HTML5, CSS3, JavaScript and python3. Besides those, the following tools were used:

- Language: English.
- [MongoDB Atlas](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
- [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/)


Libraries: 
- [Bootstrap v4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) scripts (JavaScript, jQuery and Popper.js) to get functionality in the Bootstrap's components, and css  for most of the applied style 
- [Bootstrap-Select v1.13.9](https://developer.snapappointments.com/bootstrap-select/) scripts and css to have a more interective and styled select bottom.
- [Fontawesome Version 5.9.0](https://fontawesome.com/).
- [Google Fonts](https://fonts.google.com/specimen/Charm), from here it is got the font type of the whole website ('Charm', cursive).


Own CSS style sheet. To make my own styles and overwrite some of the Bootstrap style library.
Own JavaScript file. To make the functionality of the add/remove ingredients and steeps in the method, also to change the color of the heart icom for the 'likes' .

## Testing
The whole code (html & CSS) was validated through the [Markup Validation Service](https://validator.w3.org/). The JavaScript was evaluated by [JSHint](https://jshint.com/)
The code was continuously monitored through the "Inspect" function of the Google Chrome Browser. Making sure that the website was completely responsive. The  project looks as expected in different browsers (GoogleChrome, InternetExplorer, Samsung internet).

Testing for the app.py:
1. each time a new collection was introduced, its content was corroborate through the
print function of python. Same was done while creating the diferents for's that belong 
to the routes. Example: for index, category in enumerate(categories): 
print (index,category['category_name'])
2.  navbar: all links of the navbar where manually tested.
3.  All the Searches by Category/ Cuisine / Difficulty Level give the expected result.
4.  All buttoms work as expected. 
5.  Each time the user want to add a new ingredient or steep method, the form works perfect. Same at editing.
6.  When clicking at the name of a recipe you are redirect to where you can get more infor about it.
7.  Form: if you try to submit it empty, a message telling you to fill the missing area appears.


Problems unsolved:
- When adding or editing a recipe, if 'none' option of allergens is selected, the other options can still be selected.
- The form is not completely validated before submitting. The user can submit the form without selecting any allergens.

Problems solved:
- TypeError: 'NoneType' object is not iterable. Solved through making sure the the attribute has no null value, so the object is iterable.
- AttributeError: 'dict' object has no attribute 'views' Solved by changing the method to access the dict attribute. Example: Intead of dict.attribute use 
dict['attribute']
- AttributeError: 'str' object has no attribute 'int'. Solved by converting the string to integer through the  python int() function
- TypeError: must be str, not int. Solved through checking the type of att of the dict and converting to int what was needed.
- TypeError: if no direction is specified, key_or_list must be an instance of list. Solved through changing the format of the sorting from sort({"attribute": 1}) to sort([("attribute", 1)])
- When editing the <textarea> didn't show the content. I was using wrong the sintaxis. Solved through changing <textarea value="the value"></textarea> to <textarea>the value </textarea>
- favicon.ico:1 GET https://rasquin.github.io/favicon.ico 404  Solved by creating an icon and uploading it into the site.

Problems found by the code validator and solved:
- CSS: no errors
- HTML: It is the home of the site.It has 5 sections
   *  Error: Stray end tag div. Fixed deleting the extra </div>
   *  Error: Element spam not allowed as child of element h3 in this context. The spam wasnt really neccesary, so it was taken out.
   *  Error: Duplicate ID method. Delete the duplicated ids, they resulted to be unnecessaries.

Problems found by the code validator and NO solved (HTML):

- Error: The element a must not appear as a descendant of the button element.
- Warning: The document is not mappable to XML 1.0 due to two consecutive hyphens in a comment.
- Warning: The type attribute is unnecessary for JavaScript resources.


Result of evaluation with JSHint:
- Missing semicolon. Fixed adding the respective semicolons.
- Metrics for own script located at the end of base.html: There are 5 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 12 statements in it, while the median is 4. The most complex function has a cyclomatic complexity value of 2 while the median is 1.


## Deployment
- This project is available in Github platform under the name of  [Cookbook](https://github.com/Rasquin/cookbook)
- This project is available in Heroku  platform under the name of [ monicas-cookbook](https://git.heroku.com/monicas-cookbook.git)


- The wireframes are located in [static/wireframes/](https://github.com/Rasquin/cookbook/tree/master/static/wireframes)

- You can check this project in the next  [Link](https://monicas-cookbook.herokuapp.com/ )


## Credits
### Content
The recipes were taken from the next places:
- [Slow cooker chicken casserole](https://www.bbcgoodfood.com/recipes/slow-cooker-chicken-casserole)
- [Pineapple & lime mocktail](https://www.bbcgoodfood.com/recipes/shine-light)
- [Sponge cake](https://www.bbcgoodfood.com/recipes/sponge-cake)
- [Ponche Crema Venezuelan Eggnog](https://thecookwaregeek.com/ponche-crema-venezuelan-eggnog/)
- [Caesar Salad](https://www.simplyrecipes.com/recipes/caesar_salad/)
- [Venezuelan Tamales (Hallacas)](https://www.myrecipes.com/recipe/venezuelan-tamales)
- [Chinese Steamed Rice Cake—Bai Tang Gao](https://www.chinasichuanfood.com/chinese-rice-cake-bai-tang-gao/)
- [Chicken with rice /  Spanish Style](https://mommyshomecooking.com/chicken-with-rice-spanish-style-arroz-con-pollo/)
- [Watermelon & Feta Salad](https://www.jamieoliver.com/recipes/fruit-recipes/watermelon-feta-salad/)

### Media
The photos used in this project are labelled  for reuse.
- The imagen for Good_Food_Display can be found at  [Link](https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg)
- The imagen condiments.jpg can be found at  [Link](https://pixabay.com/tr/photos/pazar-baharat-%C3%A7e%C5%9Fniler-2380566/)


## Acknowledgements
The brief for this project was given by Code Institute. I received inspiration for this project from my siter Aurora, who is studying to become a cook. I always wished that we had our own cookbook full of our crazy recipes that we invent during the weekends when we share on family.