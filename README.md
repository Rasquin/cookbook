# MONICA'S COOKBOOK - project III

Data Centric Development Milestone Project. This consist of a data-driven web application.
The  backend code and frontend form allow users to access, add, edit, store and delete cooking recipes
 
One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.

## UX
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
Optionally, you may choose to add basic user registration and authentication to 
the site. This can as simple as adding a username field to the recipe creation 
form, without a password (for this project only, this is not expected to be secure)


This website has been designed to offer the users, possible new tourists in the
city, a nice experience when choosing where to go, what to eat or where to stay. 
The visitors of this website will be able to learn about the city of Caracas, 
principal tourism spots and the variety of flavor found in the city, 

-As a user, I would like a website I would like to know where is Caracas located,
its weather and get an idea about what to expect of this city; then it should be
a section that gives the user general information about the destination city. 
-As a user, I would like to know about the different tourist attractions that can
be found is this destination; then there should be a section giving information 
about it and some recommendations of places to visit. 
-As a user, I would be curious about the local food and types of restaurants in 
the area, besides I would like to know if I could go out at nihgt and where to 
go; then it should be a section where I can get this information and some advice
about local dishes.
-As a user, I would like to know about the lodging structure of the city, then 
it should be a section that speaks about it.
-As a user, I could get doubts or questions about the city or after visiting the
city as user, I would like to tell my experience; then it should be a section 
where the user can comunicate with the administrator of the website.
-As a user, I would like to check their facebook, twitter or instagram. The
website should allow me to visit also those sites.

The wireframes of this project were made with microsoft powerpoint 2010. You can
find them in https://github.com/Rasquin/project-2-CCS/tree/master/wireframes

## Features

### Existing Features

The project consist of two scrolling pages and a contact page, each of them has
a navbar and a footer.

The 2 scrolling pages together sum 6 sections and the third page is for asking
advice or telling your experience.

The 1st scrolling page has 2 sections:
a. The home: Big image of the city with links that invite the users to discover 
the charm of Caracas. 
b. About: Here the user can get a general description about Caracas (where is
located, its weather, what to expect) and a map. The js file associated to this map 
is the mapccs.js (mapccs stands for map Caracas)

The 2nd scrolling page has 4 section:

a. Attractions: small description of the principal sites of interest in the sity.

b. Bar and Restaurants: tells the user what kind of food to expect in the city
and give some advice of local dishes.

c. Hotels: Small description of accommodation in the city.

d. Interactive Map: the user can find what they would like to check inside the 
city. Here is the list of possible type of place of the  select list:
 Attractions: Amusement Park, Art Gallery, Bowling, Casino, Church, Library, 
Mosque, Movie Theater, Museum, Natural Area, Spa, Stadium, Synagogue and Zoo.
 Bar & Restaurants: Bar, Cafe, Night Club and Restaurants.
 Shopping: Book Store, Clothing Store, Convenience Store, Department Store, 
Electronics Store, Florist, Jewelry Store, Liquor Store, Pet Store, Shoe Store, 
Shopping Mall and Stores. 
 Accommodation: Hotels  and Campground.
 Others: Bakery, Car Rental and Supermarket.
The js file associated to this map is the mapccsl.js (mapccsl stands for map 
Caracas locations)

And the 3rd page is the contact page, from where the users can ask for advice 
and/or share their experience. The js file associated to this section  is the 
sendEmail.js

All pages have a navbar that allows the user to navegate between themselves and
to the different sections of the scrolling pages. The user can also go back to 
the top whenever he or she considers it necessary. They also share the footer,
where you can find direct acces to the contact page and the social media links 
( Facebook, Twitter and Instagram).

As a user, you have to hover what you would like to check in the navbar and 
click it. Then, you will be in the section that you have selected. If you want 
to comunicate with the administrator of the website, you have to send a message 
form that is available in the contact page. You can also check their social 
media by clicking the respective icon in the inferior left corner of the 
website, and you will be be redirected to a new browser window with the desired 
content.

The website also give you acces to more information outside the page. If you
want to know more over a place given in the page, you only have to click over 
the name of said place of interest, and the site will redirect you to Wikipedia
or the respective web site.


### Features Left to Implement
. Let the user know about the rating and reviews of a desired place and give access to the website after looking 
for it at the Select. Those characteristics are not  for free.
. Allow the user to view the experiences of other people when visiting the city (blog)

## Technologies Used

This project was made with HTML5, CSS3 and JavaScript. Besides those, the following tools were used:

Language: English.

MongoDB Atlas
https://www.mongodb.com/

Heroku
https://www.heroku.com/

Libraries: 

Bootstrap v4.1.3 scripts (JavaScript, jQuery and Popper.js) to get functionality 
in the Bootstrap's components, and css  for most of the applied style
http://getbootstrap.com/docs/4.1/getting-started/introduction/

Bootstrap-Select v1.13.2 scripts and css to have a more interective and styled 
select bottom https://developer.snapappointments.com/bootstrap-select/

Emailjs API  To link the message of the contact page to a email address 

https://www.emailjs.com/
Font awesome 5.6.1 to get the icons for location-arrow, map-marked, utensils, 
bed, globe-americas, message box, facebook, twitter and instagram
and CopyRight. https://fontawesome.com

Google Map API to get the map of the about section with the location of Caracas 
https://cloud.google.com/maps-platform/

Google Map Places API to get the place though the SearchBox and show it in the
map https://developers.google.com/places/web-service/intro

Google Fonts, from here it is got the font type of the whole website 
(ZCOOL XiaoWei) https://fonts.google.com/?selection.family=ZCOOL+XiaoWei

Own CSS style sheet. To make my own styles and overwrite some of the Bootstrap 
style library.
Own JavaScript files. To make the maps work with my own criteria.

## Testing
The whole code (html & CSS) was validated through the Markup Validation Service
(https://validator.w3.org/). The JavaScript was evaluated by JSHint (https://jshint.com/)
The code was continuously monitored through the "Inspect" function of the Google
Chrome Browser. Making sure that the website was completely responsive. The 
project looks as expected in different browsers (GoogleChrome InternetExplorer).

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
. When clicking on the respective icon in the map, the idea was that user will 
get not only the name of the place, but also the address, opening hours and a 
picture. I only could get the name place in the infowindow of the map. I get
all the info needed, but coldn't show it in the infowindow.
. In the map section of attractions.html, when nothing is selected, the map 
display several places without asking for it.


Problems solved:
. Sometimes the map didn't upload when the website was opened from github. Was 
solved cleaning the caches. js?key=AIzaSyD_huMnglI9aQ9AUlk7BcwiH2oSVckYmb0&callback=initMap:54 Google Maps JavaScript API error: RefererNotAllowedMapError
https://developers.google.com/maps/documentation/javascript/error-messages#referer-not-allowed-map-error
Your site URL to be authorized: https://rasquin.github.io/project-2-CCS/index.html#about
. When opening from GitHub, the map of attractions.html didn't upload. The
console said 'not allowed referrer', but the site was already added as referrer
in the key restrictions. Solved through copying the whole website address as
http referrer.
. Alert about having two times the scripts for Google MAp Place API. One of the 
scripts was content into the other, Solved erasing the extra script.
. Could not get the Google Map Place ApI to read the place of insterest  directly 
from the select buttom. Solved changing the function initMap.
. At firts, the idea of the interactive map was that the user had  2 options to 
find what they were looking for: a) select buttom that results in the display of 
a set of places, and option b) SearchBox where the user could look for a specific place.
At the end, I had to decide for only 1 method of search, because both methods where incompatible.
I chose the select method beacause it keeps the map centered in Caracas and
allowes me easier access to the place object given by Google Map API. Whereas the 
SearchBox would change the center of the map if you looked for a place outside of Caracas.
Then I had to  change a little the logic of my own scripts and the
presentation of the info in the HTML until I got a satisfactory result. 
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
The imagen for stepping stone was copied from Wikipedia https://en.wikipedia.org/wiki/I%27m_a_Believer#/media/File:The_Monkees_single_02_I%27m_a_Believer.jpg
Backgroung image: Caracas1 https://sh.m.wikipedia.org/wiki/Datoteka:Caracas_Panoramica_1.jpg
Collage of Caracas in the Get to Know our City section: Caracas3 https://commons.wikimedia.org/wiki/File:Caracas_Venezuela_VEN_2018.png
Proceres https://commons.wikimedia.org/wiki/File:Paseo_Los_Pr%C3%B3ceres.jpg
Pabellon https://commons.wikimedia.org/wiki/File:Pabellon-criollo2.jpg
Bedroom https://get.pxhere.com/photo/white-floor-interior-home-cottage-property-furniture-room-bedroom-decor-interior-design-textile-design-bed-suite-duvet-cover-bed-sheet-bed-frame-828940.jpg

### External links

Casa Natal & Museo Bolivar https://en.wikipedia.org/wiki/Birthplace_of_Sim%C3%B3n_Bol%C3%ADvar
Plaza Bolívar de Caracas https://en.wikipedia.org/wiki/Bolivar_Plaza_(Caracas)
Paseo Los Próceres https://es.wikipedia.org/wiki/Paseo_Los_Pr%C3%B3ceres
Caracas Botanical Garden https://en.wikipedia.org/wiki/Caracas_Botanical_Garden
Museo de Arte Contemporáneo https://es.wikipedia.org/wiki/Museo_de_Arte_Contempor%C3%A1neo_de_Caracas
National Art Gallery https://en.wikipedia.org/wiki/National_Art_Gallery_(Caracas)
Los Caobos Park https://en.wikipedia.org/wiki/Los_Caobos_Park
Plaza Francia https://en.wikipedia.org/wiki/Plaza_Francia_(Caracas)
El Ávila National Park https://en.wikipedia.org/wiki/El_%C3%81vila_National_Park
National Pantheon of Venezuela https://en.wikipedia.org/wiki/National_Pantheon_of_Venezuela
Parque del este https://en.wikipedia.org/wiki/Parque_del_Este
Caracas Cathedral https://en.wikipedia.org/wiki/Caracas_Cathedral
El Hatillo Town https://en.wikipedia.org/wiki/El_Hatillo_Municipality

Pabellon https://en.wikipedia.org/wiki/Pabell%C3%B3n_criollo
arepas https://en.wikipedia.org/wiki/Arepa
cachapas https://en.wikipedia.org/wiki/Cachapa

## Acknowledgements
The brief for this project was given by Code Institute. I received inspiration 
for this project from CARACAS, the city I was born and capital of my country of 
origen, I grew up in this beautiful city and know most of its secrets. Because
the political-economics and social situation I had to go out of the country to 
look for a better life. Hoping that someday everything will go back to normal 
and my city will be open to receive a big amount of tourism.