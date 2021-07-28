# Stones Gate

Stones Gate is a website aiming to serve as a e-shop for French hand-made jewellery with stones.

In this website, user can buy hand-made jewellery according to each stones' unique properties.
They also can register and integrate their personal informations in the website for further
purchases.

Only super users access to the create/edit/delete functionalities in order to protect the website & the database from random users deleting/editing.

## UX

This website is my fourth MileStone project for my Fullstack Software Develpment diploma.

The aim of this website was to create a e-shop.

**External users goals**

As a *new user*, I want to:

1. Easily understand the purpose & goals of the website
As a new user, I can read the description at the entrance of the website to quickly understand his goals.
2. Easily navigate through the website
The navbar and the buttons in the website are designed to allow an easy navigation through the website.
3. Access the current products catalogue to gain some inspiration on what to buy
By clicking on "explore the shop" in the introduction page or by navigating through the several sections offered by the website, I can access the products catalogue & browse it.
4. Sort order of products to find cheapest/most expensive products
In the navbar, some items allow to sort products by their price, their notation or their category (earings, necklaces, rings) and the moods they relate to (energetic, peaceful or fun).
5. Find products that fits with particular moods 
In the navbar, some items allow to sort products by the moods they relate to (energetic, peaceful or fun).
5. Get a synthetic overview of each product
Once the user clicks on one particular product, a quick presentation of the properties of the stone is given. The price, the category and the mood it relates appear too.
6. Be able to buy product(s) and get them deliver to my place
I can checkout and buy a product and provide my address to get it deliver to my place.
7. Be able to view a total cost of a potential multiple purchase.
The shopping bag in the navbar, and then in the checkout page, automatically update when the total cost of purchases change.
8. Be able to search for a specific product.
In the navbar, a search bar allows the user to search for a specific product.

As a *returning user*, I want to:
1. Be able to quickly register my details & create a profile saving my personal details.
By clicking on the "My account" icon in the navbar, I can access the Register page. An email confirmation is sent to the email provided by the user. By clicking on the link provided in this email, the user confirms his registration. 
2. Be able to view my previous purchases.
As a registered user, the user can see his previous purchases inside the "my profile" section of the website.
3. Edit my personal details on my profile.
As a registered user, the user can update his personal informations in the "my profile" icon that appears in the website.

As a *admin user*, I want to:
1. Be able to add new products,
For admin users, a section 'product management' appears in the 'my profile' part of the navbar. By clicking on it, the admin user can add a new product with or without picture. Messages are provided to the admin user everytime a change is made.

2. Be able to edit the products the user previously added
Admin user can access a button in the product catalogue or inside the product details page allowing them to edit the current information. Messages are provided to the admin user everytime a change is made.

3. Be able to delete products
Admin user can access a button in the product catalogue or inside the product details page allowing them to delete the product. Messages are provided to the admin user everytime a deletion is made.

4. Be able to view, update and delete customer orders in the admin panel.
In the admin panel, the admin user can access, update or delete customer orders.

**Internal user goal**

As a site owner, I want to :

1. Share my knowledge on the stones I use to create my jewellery
Every product is presented in the product details page with a description regarding the stone it is made with.
2. Give visibility to the products I created 
Isn't it this all website's purpose?!
3. Safely sell my products
Users can buy easily and safely the products through the use of Stripe's plateform
4. Protect the website against vandalism & random users deleting/updating the current catalogue in a destructive perspective by allowing only admin users to edit/delete the products they previously added.

## Design

I am really interested regarding design, and paid a special attention to this website design. My goal was to make it simple, minimalist and interactive - in order to put the user in the heart of the website.

__Colour schemes__

In this way I decided to choose a simple contrast between three colors choosen thanks to the [Color Wheel of Adobe](https://color.adobe.com/fr/create).

__Typography__

Regarding the typography, I decided to use 2 Google fonts :

**Alice** : because of his soft-rounded features, as it looks like the typography of a supernatural book and fits well with the environment of the website.
**Quicksand** : to contrast with the round effect given by Alice & give more substance to the paragraph with a more classic typography.
Icons I decided to use Fontawesome in order to provide illustrations in my website as it offers a wide catalogue of icons.

## Frameworks

1. [Flask](https://flask.palletsprojects.com/en/2.0.x/) : A framework written in Python that gives a lot of flexibility to the coding

2. [Bootstrap](https://getbootstrap.com/) : I decided to stick to bootstrap as I find some of the functionalities really easy & handy to use and like his overall design & flexibility.

3. [DJango](https://www.djangoproject.com/) : I used Django framework to build this website as required by Code Institute.

## Wireframes

I used [Balsamic](https://balsamiq.com/) to build my wireframe prior to the website coding.

The idea was to get an idea of what sections I would build and what design I would roughly create. Wireframes were built regarding desktop, tablet and phone versions:

![Balsamic Wireframes (desktop, tablet, phone)](/workspace/MS4_Stones_Gate/documentation/wireframes/MS4_Desktop_Tablet_Phone_Wireframes.pdf/)

From the idea to the realization, a lot of changes have been performed.

NB : I created this wireframe before starting coding the project but forgot to add it to the repository at the beginning.

## Features

1. Existing Features

__Navigation__ :

I use the simple and clear navigation code suggests in [Bootstrap]. All sections are presented to ease the user experience and direct to relevant links when clicked.

__Main content__ :

I used Javascript to :
XXXXXXXXXXXXXX

2. Features to be added

Features that will be added later due to time constraints on the project.

1. Contact form for users to message any queries to the website owner.
2. A pop up model appearing when deleting products to ensure products are not deleted by accident.

## Technologies used
- [HTML](https://developer.mozilla.org/fr/docs/Learn/HTML): The project uses HTML to create the content of the website and his structure.

- [CSS](https://developer.mozilla.org/fr/docs/Web/CSS): The project uses CSS for the design of the website

- [Javascript](https://developer.mozilla.org/fr/docs/Web/JavaScript): The project uses Javascript to add interactivity with the user.

- [JQuery](https://jquery.com/): The project uses JQuery to manipulate the DOM.

- [Django](https://www.djangoproject.com/) : The web framework encouraging rapid development and clean, pragmatic design. 

- [Bootstrap](https://getbootstrap.com/): The project uses Bootstrap in the overall design. Grid, navbar, form, modal and many other features described in the Features' section were coded from Bootstrap interface.

- [Fontawesome](https://fontawesome.com/): The project uses Fontawesome in several places of the website everytime an icon appears.

- [Googlefonts](https://fonts.google.com/): The project uses GoogleFonts to choose the two fonts family used for the design of this website (Alice and Quicksand)

- [Heroku](https://dashboard.heroku.com/): Host of my full stack website.

- [Python](https://www.python.org/): My main Back-End programming language.

Flask

Flask - Open-source micro framework for web development in Python

Click - A Python package to create command line interfaces.

DNSpython - Domain Name system toolkit used by Python

Jinja - Useful to template in relation with Flask

itsdangerous - Permits to cryptographically sign data

Werkzeug - A CGI Library for Flask

MongoDB: Storage of my database.

## Tools used
- [Bootstrap](https://getbootstrap.com/):
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
!!!!!!!!!!!!!!!!!! PEP8 Validator !!!!!!!!!!!!!!!!!!!!!!!
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

## Testing

1. Testing tools used

- [W3C HTML Validator](https://validator.w3.org/) - I run my url website through the validator & errors identified were linked to the use of [Ginger](https://ginger.readthedocs.io/en/latest/) language (presence of "{{ }}" or whitespace in ID format, absence of head section or language at the top of each page, etc.)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

I run my style.css, checkout.css and profile.css codes through the validator & no errors were identified.

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

No problems identified regarding design & responsiveness for the following devices:
__Phone__: Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, Iphone 5/SE, Iphone 6/7/8, Iphone 6/7/8 Plus, Iphone X
__Tablet__: Ipad, Ipad Pro, Surface Duo

2. Test UX
Details of the full test performed (with screenshots) on this project can be found here.


## Credits
__Content:__

Texts were written by myself to fit with this website's goals.

__Images:__

All images used in this website have been taken by my mother that actually created all these jewellery (and allowed me to use them).

__Acknowledgements:__

The site is WIDELY based on the Boutique Ado code insitute tutorial project.

Eventually I received help for my code 
- by reading answers from questions on the Slack chat
- by contacting Code Institute Tutoring

Thank you for all this help!