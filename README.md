# Stones Gate

Stones Gate is a website aiming to serve as a e-shop for French hand-made jewellery with stones.

In this website, user can buy hand-made jewellery according to each stones' unique properties.
They also can register and integrate their personal informations in the website for further
purchases.

Only super users access to the create/edit/delete functionalities in order to protect the website & the database from random users deleting/editing.

## UX

This website is my fourth MileStone project for my Fullstack Software Develpment diploma.

The aim of this website was to create a e-shop.

**_External users goals_**

* As *any type of user*, I want to:

1. **Easily understand the purpose & goals of the website**

As a new user, I can read the description at the entrance of the website to quickly understand his goals.

2. **Easily navigate through the website**

The navbar and the and the buttons in the website are designed to allow an easy navigation through the website.

3. **Access the current products catalogue to gain some inspiration on what to buy**

By clicking on "explore the shop" in the introduction page or by navigating through the several sections offered by the website, I can access the products catalogue & browse it.

4. **Sort products to find the most expensive/cheapest ones**

In the navbar, some items allow to sort products by their price, their notation or their category (earings, necklaces, rings) and the moods they relate to (energetic, peaceful or fun).

5. **Find products that fits with particular moods**

In the navbar, some items allow to sort products by the moods they relate to (energetic, peaceful or fun).

6. **Get a synthetic overview of each product**

Once the user clicks on one particular product, a quick presentation of the properties of the stone is given. The price, the category and the mood it relates appear too.

7. **Be able to buy product(s) and get them deliver to my place**

I can checkout and buy a product and provide my address to get it deliver to my place.

8. **Be able to view a total cost of a potential multiple purchase.**

The shopping bag in the navbar, and then in the checkout page, automatically update when the total cost of purchases change.

9. **Be able to search for a specific product.**

In the navbar, a search bar allows the user to search for a specific product.

10. **Be able to register to a new account**
By clicking on the "My account" icon in the navbar, I can access the Register page. An email confirmation is sent to the email provided by the user. By clicking on the link provided in this email, the user confirms his registration. 

* As a *returning user*, I additionnaly want to:

1. **Be able to quickly register my details & create a profile saving my personal details & to edit it.**

After registering, I can log in my account by clicking on the navbar on the "My account" and then "Log in" icon. By fulfilling the information and logging in I can then access a new section of the navbar in "My account". The "My profile" section leads to a page where the user can save/edit his personal information.

2. **Be able to view my previous purchases.**

As a registered user, the user can see his previous purchases inside the "my profile" section of the website.


* As a *admin user*, I want to:

1. **Be able to add new products**

For admin users, a section 'product management' appears in the 'my profile' part of the navbar. By clicking on it, the admin user can add a new product with or without picture. Messages are provided to the admin user everytime a change is made.

2. **Be able to edit the products the user previously added**

Admin user can access a button in the product catalogue or inside the product details page allowing them to edit the current information. Messages are provided to the admin user everytime a change is made.

3. **Be able to delete products**

Admin user can access a button in the product catalogue or inside the product details page allowing them to delete the product. Messages are provided to the admin user everytime a deletion is made.

4. **Be able to view, update and delete customer orders in the admin panel.**

In the admin panel, the admin user can access, update or delete customer orders.

**_Internal user goal_**

* As a _site owner_, I want to :

1. **Share my knowledge on the stones I use to create my jewellery**

Every product is presented in the product details page with a description regarding the stone it is made with.

2. **Give visibility to the products I created**
Isn't it this all website's purpose?!

3. **Safely sell my products**

Users can buy easily and safely the products through the use of Stripe's plateform

4. **Protect the website against vandalism & random users deleting/updating the current catalogue in a destructive perspective by allowing only admin users to edit/delete the products they previously added.**

## Design

I am really interested regarding design, and paid a special attention to this website design. My goal was to make it simple, minimalist and interactive - in order to put the user in the heart of the website.

__Colour schemes__

In this way I decided to choose a simple contrast between three colors choosen thanks to the [Color Wheel of Adobe](https://color.adobe.com/fr/create).

__Typography__

Regarding the typography, I decided to use 2 Google fonts:

**[Alice](https://fonts.google.com/specimen/Alice)** : because of his soft-rounded features, as it looks like the typography of a supernatural book and fits well with the environment of the website.

**[Quicksand](https://fonts.google.com/specimen/Quicksand)** : to contrast with the round effect given by Alice & give more substance to the paragraph with a more classic typography.

**Icons** : I decided to use [Fontawesome](https://fontawesome.com/) in order to provide illustrations in my website as it offers a wide catalogue of icons.

## Frameworks

1. [Bootstrap](https://getbootstrap.com/) : I decided to stick to bootstrap as I find some of the functionalities really easy & handy to use and like his overall design & flexibility.

2. [DJango](https://www.djangoproject.com/) : I used Django framework to build this website as required by Code Institute.

## Wireframes

I used [Balsamic](https://balsamiq.com/) to build my wireframe prior to the website coding.

The idea was to get an idea of what sections I would build and what design I would roughly create. Wireframes were built regarding desktop, tablet and phone versions:

![Balsamic Wireframes](documentation/wireframes/MS4_Desktop_Tablet_Phone_Wireframes.pdf)

From the idea to the realization, a lot of changes have been performed.

**NB** : I created this wireframe before starting coding the project but forgot to add it to the repository at the beginning.

## Features

The website is classified by 7 applications: bag, checkout, home, products, profiles, stones_gate and templates.

### **1. Existing Features**

__*Navigation*__ :

I use the simple and clear navigation code suggests in [Bootstrap]. All sections are presented to ease the user experience and direct to relevant links when clicked.

__*Main content*__ :

I used Javascript in the following pages:

- **Bag.html**: Javascript code was widely adapted from Code Institue - Boutique Ado in order to :
1) Update quantity box 
2) Remove item and reload on click

- **Checkout.html > stripe_elements.js** : Javascript code was widely adapted from Code Institue - Boutique Ado in order to :
1) Handle realtime validation errors on the card element
2) Handle form submit

- **Products.html** : Javascript code was widely adapted from Code Institue - Boutique Ado in order to :
1) Add a button to go back to the top of the page 
2) Functionality to sort products by price/notation/category/mood

- **Product_details.html > quantity_input_script.html** : Javascript code was widely adapted from Code Institue - Boutique Ado in order to :
1) Increment/decrement quantity
2) Ensure proper enabling/disabling of all inputs on page load
3) Disable +/- buttons outside 1-99 range


### **2. Features to be added**

Features that will be added later due to time constraints on the project.

1. Contact form for users to message any queries to the website owner.
2. A pop up model appearing when deleting products to ensure products are not deleted by accident.

## Technologies used

**Languages**

- [HTML](https://developer.mozilla.org/fr/docs/Learn/HTML): The project uses HTML to create the content of the website and his structure.

- [CSS](https://developer.mozilla.org/fr/docs/Web/CSS): The project uses CSS for the design of the website

- [Javascript](https://developer.mozilla.org/fr/docs/Web/JavaScript): The project uses Javascript to add interactivity with the user.

- [JQuery](https://jquery.com/): The project uses JQuery to manipulate the DOM.

- [Python](https://www.python.org/): My main Back-End programming language.

- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) which provides the templating language for Python.

**Frameworks & libraries**

- [Django](https://www.djangoproject.com/) : The web framework encouraging rapid development and clean, pragmatic design. 

- [Pip3](https://pip.pypa.io/en/stable/) : in order to install the tools, libraries and frameworks necessary to this project.

- [AWS Amazon](https://aws.amazon.com/fr/) : in order to store static and media files.

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) : for compatibility in AWS.

- [Gunicorn](https://pypi.org/project/gunicorn/) : in order to enable deployment to Heroku.

- [Spycopg2](https://pypi.org/project/gunicorn/) : in order to enable the PostGreSQL database to connect with Django.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) : in order to style the Django forms

- [Stripe](https://stripe.com/fr) : in order to secure payments

- [Bootstrap](https://getbootstrap.com/): The project uses Bootstrap in the overall design. Grid, navbar, form, modal and many other features described in the Features' section were coded from Bootstrap interface.

- [Fontawesome](https://fontawesome.com/): The project uses Fontawesome in several places of the website everytime an icon appears.

- [Googlefonts](https://fonts.google.com/): The project uses GoogleFonts to choose the two fonts family used for the design of this website (Alice and Quicksand)

- [Heroku](https://dashboard.heroku.com/): Host of my full stack website.

**Databases**
- [SQlite3](https://www.sqlite.org/index.html): SQlite3 is the database used at the development phase.
- [PostgreSQL](https://www.postgresql.org/) : PostgreSQL is the database used as the production database.

## Tools used
- [Bootstrap](https://getbootstrap.com/)
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [PEP8 Validator](http://pep8online.com/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

## Testing

**1. Testing tools used**

- [W3C HTML Validator](https://validator.w3.org/) - I run all my html files through the validator & errors identified were linked to the use of [Ginger](https://ginger.readthedocs.io/en/latest/) language (presence of "{{ }}" or whitespace in ID format, absence of head section or language at the top of each page, etc.)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - I run my `style.css`, `checkout.css` and `profile.css` codes through the validator & no errors were identified.

- [PEP8 Online Validator](http://pep8online.com/):
I run all the following python codes through the validator & no errors were identified:

    * **bag app** : `contexts.py` ; `urls.py` ; `views.py` ; `admin.py` ; `apps.py` ; `models.py` ; `tests.py`
    * **checkout app** : `admin.py` ; `apps.py` ; `forms.py` ; `models.py` ; `signals.py` ; `urls.py` ; `views.py` ; `tests.py` ; `webhook_handler.py` ; `webhooks.py`
    * **home app** : `admin.py` ; `apps.py` ; `models.py` ; `tests.py` ; `urls.py` ; `views.py`
    * **profiles app** : `admin.py` ; `apps.py` ; `forms.py` ; `models.py` ; `urls.py` ; `views.py` 
    * **stones_gate** : `asgi.py` ; `settings.py` ; `urls.py` ; `wsgi.py`
    * **`custom_storages.py`**
    * **`manage.py`**


- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - No problems identified regarding design & responsiveness for the following devices:

__Phone__: Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, Iphone 5/SE, Iphone 6/7/8, Iphone 6/7/8 Plus, Iphone X

__Tablet__: Ipad, Ipad Pro, Surface Duo


**2. Test UX**

Details of the full test performed (with screenshots) on this project can be found here.


## Deployment

Because of their clarity & transparence, I widely adapted this section from the README of Juan Stelling [project](https://github.com/juanstelling/MS4-prints).

**Tools used to deploy**

- **Github**
- **Heroku**
- **Python3**
- **Stripe**
- **Gmail**
- **AWS Amazon Account**

**Clone the project** 

To make a local clone:

- Log in to GitHub and go to the repository.
- Click on the “Code” button.

**Working with a local copy**

1. In the workspace of the local copy, type in the terminal window: **pip3 install -r requirements.txt**.

2. Set up the environment variables:

- Create a `.gitignore` file
- Create a `.env` file. which contains these environment variables:

> Import os

> os.environ("SECRET_KEY", "To be added by the developer")

> os.environ("STRIPE_PUBLIC_KEY", "To be added by the developer")

> os.environ("STRIPE_SECRET_KEY", "To be added by the developer")

> os.environ("STRIPE_WH_SECRET", "To be added by the developer")

> os.environ("MAILCHIMP_API_KEY", "To be added by the developer")

> os.environ("MAILCHIMP_DATA_CENTER", "To be added by the developer")

> os.environ("MAILCHIMP_EMAIL_LIST_ID", "To be added by the developer")

- Add the `.env` file to the `.gitignore` file. 

3. Migrate the models to create the database with these commands:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

4. Load the data fixtures in this order:

`python3 manage.py loaddata categories`

`python3 manage.py loaddata products`

5. Create a superuser which will be able to acces to the admin environment.

- `python3 manage.py createsuperuser`
- Enter your username, email and password.

6. Run the app: Open your terminal window in your IDE and type: 
`python3 manage.py runserver`

7. Then, to acces the admin environment, you can add `/admin` at the end of your url and login with the superuser.

**Heroku Deployment**

1. **Set up local workspace for Heroku**

- In terminal window type: `pip3 freeze -- local > requirements.txt.`
- In terminal window type: `web: gunicorn <name app>.wsgi:application` to create a Procfile
- Push all these files to Github

2. **Set up Heroku**
- Create an account, a new app and select a region
- Search for postgess inside 'resources' section. Select the free version and add it to the project.
- Set up the settings inside the 'settings' section  by going on **Config Vars**. After revealing the variables, you then add the following variables:

| VALUE | KEY |
| ------|----|
| **AWS_ACCESS_KEY_ID** | aws access key |  
| **AWS_SECRET_ACCESS_KEY** | aws secret access key|
| **DATABASE_URL** | postgres database url|
| **EMAIL_HOST_PASS** | email password(generated by Gmail)|
| **EMAIL_HOST_USER** | email address |
| **SECRET_KEY** | your secret key|
| **STRIPE_PUBLIC_KEY** | your stripe public key|
| **STRIPE_SECRET_KEY** | your stripe secret key|
| **STRIPE_WH_SECRET** | your stripe wh key|
| **USE_AWS** | True|

3. **Set up the database**

- Copy the DATABASE_URL from the config variables of Heroku and past it into the default database in `setting.py`: 
>DATABASES = {
>    
>    'default': dj_database_url.parse("<DATABASE_URL here>")
>
>}

- Migrate models to create the database by typing the following commands in the terminal:
> python3 manage.py makemigrations
> python3 manage.py migrate

- Load the data fixtures in this order:
> python3 manage.py loaddata categories
> python3 manage.py loaddata products

- Create a superuser. The superuser has acces to the admin environment.
> python3 manage.py createsuperuser

- Enter your username, email and password.
Now you can remove the DATABASE_URL from `settings.py` and set the 'old' default DATABASE settings.

- Adjust the ALLOWED_HOSTS in you `settings.py` with the following:
> ALLOWED_HOSTS = ['<your Heroku app URL>', 'localhost]

- Push to Github.

4. **Connect with Heroku**

- Connect to GitHub in the deploy section in Heroku: Search the repository to connect with. (Click on connect)
- Set automatic deployments ('Deploy' tab > Automatic deployment > Enable Automatic Deploys). Then, by clicking on **Open App** the app will open and the live link will be available from the address bar.

5. **Host static and media files with AWS
Static and media files are hosted in the AWS S3 Bucket.**

In order to host its, an account, a S3 bucket, a group, a policy and a user needs to be set up in the IAM environement. 

_More information:_
- about S3 Bucket storage can be found [here](https://aws.amazon.com/fr/s3/).
- about the storage in your project click [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)



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