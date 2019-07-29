# MONICA'S COOKBOOK - project III

Data Centric Development Milestone Project. This consist of a data-driven web application.
The  backend code and frontend form allow users to access, add, edit, store and delete 
cooking recipes, types of categories and cuisines.



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

-As a user I would like to know as much as possible about the recipe I am interested in.

-As a user, I would like to check their facebook, twitter or instagram. The
website should allow me to visit also those sites.



The wireframes of this project were made with microsoft powerpoint 2010. You can
find them in https://github.com/Rasquin/project-2-CCS/tree/master/wireframes

## Features

The 
database schema based on recipes, and any other related properties and entities 
(e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of
origin, cuisine etc…).
the backend code to group and summarise the recipes on the site, based on their
attributes such as cuisine, country of origin, allergens, ingredients, etc. and 
a frontend page to show this summary, and make the categories clickable to dril
l down into a filtered view based on that category. This frontend 
Create the backend code to retrieve a list of recipes, filtered based on various
criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable
aspect (e.g. number of views or upvotes). Create a frontend page to display these,
and to show some summary statistics around the list (e.g. number of matching 
recipes, number of new recipes. Optionally, add support for pagination, when the 
number of results is large
Create a detailed view for each recipes, that would just show all attributes for
that recipe, and the full preparation instructions
Allow for editing and deleting of the recipe records, either on separate pages,
or built into the list/detail pages



### Existing Features

Routes:

index
/cookbook --> cookbook() -->render template to cookbook.html

Recipes
/all_recipes --> all_recipes() --> render template to allrecipes.html
/add_recipe --> add_recipe() --> render template to addrecipe.html
/the_recipe/<recipe_id>  -->  the_recipe(recipe_id) --> render template to recipe.html
/inser_recipe', methods=['POST'] --> insert_recipe() --> redirect to cookbook.html
/edit_recipe/<recipe_id> --> edit_recipe(recipe_id) --> render template to editrecipe.html
/update_recipe/<recipe_id>, methods=["POST"] -->update_recipe(recipe_id)--> redirect to  cookbook.html
/delete_recipe/<recipe_id> --> delete_recipe(recipe_id) ---> redirect to cookbook.html

Categories
/get_recipes_by_category/<category_id> --> get_recipes_by_category(category_id) --> render_template to recipesbycategory.html
/add_category -->add_category() --> render_template to addcattegory.html
/inser_category, methods=['POST'] -->inser_category() ---> redirect  to cookbook.html
/edit_category/<category_id> --> edit_category(category_id) --> render template to editcategory.html
/update_category/<category_id>, methods=["POST"] --> update_category(category_id) -->redirect  to cookbook.html
/delete_category/<category_id> --> delete_category(category_id) -->redirect  to cookbook.html

Cuisines
/get_recipes_by_cuisine/<cuisine_id> --> get_recipes_by_cuisine(cuisine_id)--> render_template to recipesbycuisine.html
/add_cuisine --> add_cuisine() --> render_template to addcuisine.html
/inser_cuisine', methods=['POST'] --> insert_cuisine() --> redirect  to cookbook.html
/edit_cuisine/<cuisine_id> --> edit_cuisine(cuisine_id) --> render_template to editcuisine.html
/update_cuisine/<cuisine_id>', methods=["POST"] --> update_cuisine(cuisine_id) --> redirect  to cookbook.html
/delete_cuisine/<cuisine_id> --> delete_cuisine(cuisine_id) --> redirect  to cookbook.html

Difficulty Level

## Technologies Used

This project was made with HTML5, CSS3, JavaScript and python. Besides those, the following tools were used:

Language: English.

MongoDB Atlas
https://www.mongodb.com/

Heroku
https://www.heroku.com/

Jinja 2.10
http://jinja.pocoo.org/docs/2.10/

Libraries: 
Bootstrap v4.3.1 scripts (JavaScript, jQuery and Popper.js) to get functionality 
in the Bootstrap's components, and css  for most of the applied style
https://getbootstrap.com/docs/4.3/getting-started/introduction/

Bootstrap-Select v1.13.9 scripts and css to have a more interective and styled 
select bottom https://developer.snapappointments.com/bootstrap-select/

Fontawesome Version 5.9.0  https://fontawesome.com/


Google Fonts, from here it is got the font type of the whole website 
('Charm', cursive) 
https://fonts.google.com/specimen/Charm

Own CSS style sheet. To make my own styles and overwrite some of the Bootstrap 
style library.
Own JavaScript file. To make the functionality of the add/remove ingredients and 
steeps in the method, also to change the color of the heart icom for the 'likes' .

## Testing
The whole code (html & CSS) was validated through the Markup Validation Service
(https://validator.w3.org/). The JavaScript was evaluated by JSHint (https://jshint.com/)
The code was continuously monitored through the "Inspect" function of the Google
Chrome Browser. Making sure that the website was completely responsive. The 
project looks as expected in different browsers (GoogleChrome InternetExplorer).

Testing for the app.py:
1 each time a new collection was introduced, its content was corroborate through the
print function of python. Same was done while creating the diferents for's that belong 
to the routes. Example: for index, category in enumerate(categories): 
print (index,category['category_name'])

1 navbar:the navbar in both pages allows you to nav to the exact place you want
in the website between them.
2 Both maps open in the right location.
3 When select a type of place with  the Select buttom, its value is transferred
to the SearchBox.
4 When looking for a type of place in the SearchBox you get several places as 
result.
5 When clicking over the name of a place of interest in the map, you get info 
about it. 
6 When writing the name of a place that is not located in Caracas, the map gives
no result.
7 Each external link was clicked to check that it redirect you to the place it 
is supposed to.
8 Form: if you try to submit it empty, a message telling you about the relevant
error appears.

Problems unsolved:
.

Problems solved:
. TypeError: 'NoneType' object is not iterable. Solved through making sure the 
the attribute has no null value, so the object is iterable.
. AttributeError: 'dict' object has no attribute 'views' Solved by changing the
method to access the dict attribute. Example: Intead of dict.attribute use 
dict['attribute']
. AttributeError: 'str' object has no attribute 'int'. Solved by converting the 
string to integer through the  python int() function
. TypeError: must be str, not int. Solved through checking the type of att of the
dict and converting to int what was needed.
.TypeError: if no direction is specified, key_or_list must be an instance of list. 
Solved through changing the format of the sorting from sort({"attribute": 1})
to sort([("attribute", 1)])
. When editing the <textarea> didn't show the content. I was using wrong the 
sintaxis. Solved through changing <textarea value="the value"></textarea> to
<textarea>the value </textarea>


. favicon.ico:1 GET https://rasquin.github.io/favicon.ico 404  Solved by creating 
an icon and uploading it into the site.

Problems found by the code validator and solved:
. CSS: no errors
. HTML: Stray end tag img. I took out all the tags. 

Result of evaluation with JSHint:
. Missing semicolon. Fixed adding the respective semicolons.
. Variables that were already defined. Fixed erasing what was extra.
. Metrics for mapccsl.js: There are 6 functions in this file.
Function with the largest signature take 2 arguments, while the median is 1.
Largest function has 8 statements in it, while the median is 4.
The most complex function has a cyclomatic complexity value of 3 while the median is 1.
. Metrics for mapccs.js: There is only one function in this file.
It takes no arguments. This function contains 3 statements.
Cyclomatic complexity number for this function is 1.
. Metrics for sendEmail.js: There are 3 functions in this file.
Function with the largest signature take 1 arguments, while the median is 1.
Largest function has 2 statements in it, while the median is 1.
The most complex function has a cyclomatic complexity value of 1 while the median is 1.
 
## Deployment
This project is available in the GitHub platform under the name of project-2-CCS
https://github.com/Rasquin/project-2-CCS

The wareframes are located in assets/wareframes/wireframeXS.pdf for xs wireframe
and assets/wareframes/wireframeXL.pdf for xl wireframe.


The principal different between the deployed version and the development version
is that in the developer version there is an extra html and js file (tryout.html &maptry.js) used to 
develop each section of the code.  After having a perfectly functional code, 
this was moved to its final  file.

You can check this project in the next URL https://rasquin.github.io/project-2-CCS/


## Credits
### Content
Text of Caracas Get to know our city was got from https://en.wikipedia.org/wiki/Caracas

### Media
The photos used in this project are labelled  for reuse.
The imagen for Good_Food_Display can be found in https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg
### External links

Casa Natal & Museo Bolivar https://en.wikipedia.org/wiki/Birthplace_of_Sim%C3%B3n_Bol%C3%ADvar


## Acknowledgements
The brief for this project was given by Code Institute. I received inspiration 
for this project from my siter Aurora, who is studying to become a cook. I always 
wished that we had our own cookbook full of our crazy recipes that we invent 
during the weekends when we share on family.



      