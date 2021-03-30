<!-- @format -->
<h1 align="center">Milestone 4 Project</h1>
<h1 align="center">Gate Fittings Direct 4 Trade</h1>

[View the live site here](https://gfd4trade.herokuapp.com/)

This is my project for my fourth and final milestone at Code Institute. It is designed
with responsiveness in mind and can be used and views on many devices. This site is an
e-commerce platform for a unique seller of gate fittings and fencing goods. It will
provide an easy way for people to purchase from the website securely. With the ability
to view their past orders and get in touch with the owner.

## Contents

1. [**Aim**](#aim)

## Aim

This site is an e-commerce site for a business that sells gate fittings and fencing
products. It's main simple aim is to provide a working, easy to navigate site that
customers can purchase from. It is aimed at those in the gate or fencing trades and
already has a customer base.

The audience is people in the trade, fencers, carpenters, farmers etc. Due to this, the
site has been made as easy to use as possible. Doesn't include any fancy animations or
anything that isn't straight to the point and easy to use. The audience that will want
to use this site are doing it for work rather than pleasure. Therefore waiting around
for an animation or to look at a pretty picture isn't a priority.

The owner of the site aims to make money from this website when it is put live onto a
hosting platform other than heroku for obvious reasons.

## UX

-   ### User Stories

    [User Stories in google sheets](https://docs.google.com/spreadsheets/d/1OmIXVfdEDepPAUjL9QAewhfWkyhaD6l8JftUSTrhdsQ/edit?usp=sharing)

    Above is a link to a google sheet containing the user stories I employed during this
    project. The one's ticked are those that have not been yet as of finishing the project
    these will be satisfied after the submission for the live website.

-   ### Design

    -   #### Colour Scheme

        -   The main colours on the site we're chosen by the owner of the business.
            despite that they fit rather well and I was happy to employ them without any changes.
            The blue is their signature colour which is present on all merchandise such as pens
            and packaging. The greys and white's were chosen as the products and business is
            for the industry which align fairly well to that aesthetic.

    -   #### Typography

        -   I chose to work with Montserrat for normal text and Spectral for titles and
            other important information. I used these as Montserrat is very easy to read for large
            walls of text. Spectral has a slight more flare to it, pleasing to the eye and different
            enough from other text on the internet that it makes it feel unique rather than
            another copy/past website.

    -   #### Imagery / Layout

        -   The layout of this project was important, but simple. With any e-commerce website you
            can either take it wild and make something truly different, but the audience and products
            also have to be just as niche. The industry this business is selling to is standard and
            quick. A simple grid layout for all the items make them easy to place, easy to expect and
            easy to understand at a first glance.
        -   Imagery was chosen by the business. They wanted colour on the front page and reasonable
            sized pictures for each project. They would have liked the home page to be covered from
            top to bottom in photos of their goods, I chose not to due to it looking a little dated if
            the website is lacking in white space and simple design.

-   ### Information Architecture

    -   To suit the needs of a first time buyer or someone that frequently buys from this store
        all the information and products needed to be layed out in a fashion that was easy to
        digest and easy to return to without having to strain on what to do. Some newer websites fall
        into this trap. Making it beautiful to look at, but function for an e-commerce site, in my
        opinion outranks beauty.

    -   A single thin navbar that is always accessible was suited best. With the largest item being
        the search bar. Most people coming to an ecommerce site, especially one like this are looking
        for a particular item. They know what they want and they want to get to it as quickly as possible.
        So the search bar will be one of the first things they see. Then the products are all under one
        dropdown, which is easy to use and displays all of the categories in a neat fashion so the user
        knows what to look for immediately.

    -   Pagination. Due to there possibly being thousands of items eventually in the website pages
        are needed so the user doesn't have to endlessly scroll down to find something they want.

-   ### Wireframes

    -   An album of wireframes can be found here: [Wireframes](https://ibb.co/album/6cSW4r)

## Features

-   ## User Login / Registration

    -   Customers can log in to the website to save delivery information while also being able to see
        past order.

-   ## Contact Page

    -   Customers can access the contact page via the navbar or the footer to be able to send an
        email directly to the owner of the site in case they need help with anything, or have a
        question.

-   ## Category Pages

    -   Pages that display all of the products relating to the sub or main category

-   ## Search

    -   A large search bar that the customers can use to find items via title, description and SKU

-   ## Basket

    -   A cart that displayed the users current basket, showing total, what items and how many. Which
        links to the checkout page

-   ## Checkout / Stripe

    -   Checkout page, where the users can place an order for their goods, this is powered by Stripe
        for the payments. Which takes the users card details.

-   ## Profile

    -   A profile page where users can see their saved deliery information, update it and also see
        their past orders.

-   ## Admin Add product

    -   Admins have the ability to add new products to the page

## Feastures that could be implemented

-   ## Trade login

    -   Users could sign up for a trade account, which would allow them to recieve discounted prices
        on all items.

-   ## Messenger chat

    -   A live chat that links to the owners facebook messenger account. Allowing users instant access
        to talking to the owner for help on an item

-   ## Reviews

    -   Reviews of the products

-   ## Category Searching

    -   Currently users cannot search for a category, while not important due to searching for "hinge"
        will turn all of the items that have "hinge" in them. Which would cover the items anyway

-   ## Stock management

    -   Have the application read from a stock system, updating and displaying how many items are left
        in stock. Updating them once an item has been purchased.

-   ## Delivery Times

    -   At checkout display how long the delivery time is for their cart.

## Technologies Used

[HTML5](https://html.spec.whatwg.org/multipage/)
[CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
[Bootstrap](https://getbootstrap.com/) - The framework of the site
[JavaScript](https://www.javascript.com/)
[jQuery](https://jquery.com/)
[Python (v3.8)](https://www.python.org/)
[Django](https://www.djangoproject.com/)
[SQLite3](https://www.sqlite.org/index.html)
[Git](https://git-scm.com/)
[Google Fonts](https://fonts.google.com/)
[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
[VS Code](https://code.visualstudio.com/)

Please see the requirements.txt file for all other minor packages and technologies used during
this project.

## Fixture Structure

-   ### Products

    {
    "pk": 1,
    "model": "products.product",
    "fields": {
    "sku": "OBJECT",
    "name": "A suitable name",
    "description": "A Description",
    "material": "Material steel, iron etc.",
    "brand": "Brand",
    "price": 27.95,
    "trade_price": 22.35,
    "main_category": 2,
    "sub_category": 1,
    "rating": null,
    "image": "OBJECT.jpg"
    }
    },

    The important parts here are the main and sub category foreign keys, these link to the
    fixtures for relevant categories which can then be pulled from the database.

-   ### Categories

    #### Main

    {
    "pk": 1,
    "model": "products.main_category",
    "fields": {
    "name": "hinges",
    "friendly_name": "Hinges"
    }
    },

    #### Sub

    {
    "pk": 1,
    "model": "products.sub_category",
    "fields": {
    "name": "mortice_latches",
    "friendly_name": "Mortice Latches",
    "main_category": 2,
    "image": "mortlatch-cat.jpg"
    }
    },

    Each one of these contains a DB name which can be called on through python and also
    a friendly name for displaying on the front end.

## Testing

I tried to use the W3C Markup Validators for CSS and HTML although due to the implementation
of django the html validator will never pass. But the CSS test came up clean, no errors on all
of my css files.

I also ran my code through autopep8 for each python file to make sure everthing was formatted
to this standard. The same goes for flake8, although some issues cannt be resolved due to them
being files I didn't manually create etc.

### Testing User Stories

[User Stories Testing in a google doc](https://docs.google.com/spreadsheets/d/1vPskYcMuUXf41IYL93_jZ15PCKGBZeh9otY5SzItdxY/edit?usp=sharing)

### Automatic Testing

I implemented a few automatic testing procedures, to at least test the URL of each app.

I would've added more, but I was told it was not a requirement and wouldn't fail me, therefore
other things took precedant as I was short for time.

### Further Testing

-   The website was tested on Chrome, Edge, Firefox, Safari and Android Internet
    -   As I have not set a background colour to the main site. On firefox in dark mode all white
        is changed to black and black text visa-versa, this was an unintended feature but the site
        still works and is readable in dark mode. Therefore I didn't change any of the code to correct
        this action.
    -   The website was created with mobile design first, styling it for smaller devices first and scaling
        up after. It was tested when deployed on various models of phones and desktop screens.
    -   Throughout the production fase countless amounts of manual tests were completed making
        sure that every time I created a new function or changed old code, everything on the website
        still worked. This included scraping the whole site after every big commit to check every button,
        page or link.
    -   A few friends tested the website who are also programmers to see if they could break or find
        obvious flaws. Family also viewed the site once deployed to check for styling issues and to give
        feedback regarding the experience on the site.

## Other Notes

### If using VS Code or other local based code editor for Stripe:

While stripe will work without a hitch if you get every bit of code correct without needing to
test it, you may still want to make sure that webhooks are working correctly. If using a "live"
IDE like gitpod then stripe will take your site as being "live" and therefore the webhooks can
be handled on their main site. What is different for VS Code and similar editors is that because
the website is only hosted locally, Stripe cannot send data over the internet to test it.

To work around this you have to install Stripe CLI on your computer. Below are the links to the
docs that will explain how to perform this action.

https://stripe.com/docs/stripe-cli
https://stripe.com/docs/stripe-vscode

Of course, VS Code does have an extension for Stripe as well. This inconjunction with Stripe CLI
will allow you to test Webhooks, trigger events, see them produced etc. Although I think working in
and env prevents VS Code from registering that Stripe CLI is downloaded. So it never worked for me.
The workaround I employed is running the process through the CMD. Below are instructions on how I
used Stripe CLI

1. Download the CLI
2. Unzip the file
3. Go the CMD and cd to where you downloaded it (This can be made easier by downloading the item
   Straight to the root of your files)
4. Run stripe.exe
5. Run stripe login
    1. You will be given a "key" for verification
    2. Press enter and login to the Stripe website when prompted
    3. Return back to the CMD
6. Run stripe listen --forward-to (your local domain e.g. http://127.0.0.1:8000)
    1. For it to work with this patricular project at the end of your domain add /checkout/wh
7. You will be given a secret key, use this in your site for STRIPE_WH_SECRET
    1. For this site I have my secret keys in an .env file located in the main projects folder with settings.py etc.
    2. You have to manually add this file, but it keeps your keys safe in production
    3. Also make sure to .gitignore .env files when using Github etc.
8. Once completed run your site
9. Open a seperate CMD, without closing the other one
10. Run stripe trigger <event>
    1. These events can be anything a user might do, to find all the events please see here: https://stripe.com/docs/cli/trigger
11. If all works you will be presented with a status code in the editors terminal and also the first CMD
12. This will confirm whether or not Stripe Webhooks is working as intended or not

## Current Major issue with devlopment mode

After deploying to heroku and pushing static files to AWS on the production version of the webite
somehow it broke the development version of this website. When running the website 'runserver'
the website returns all media and static files as 404.

I approached the code institute tutor team to see what I had done, hopeful thinking it was a simple fix.
Neither of us could them come to a conclusion on why this broke, how and how to fix it. Therefore I have left
it in it's current state. This may be a mistake but without going back to a previous commit I cannot
fix it. I have worked poorly within the time given and have run out of air to breathe.

For the markers that are reading this, when you manage to fix it, as I'm sure you will, even if it
causes a failure please let me know how to undo these changes if possible... Thanks

## Deployment

### AWS

I used AWS to store all static and media files

To create a bucket please follow below:

1. Create an account with aws.amazon.com.
2. In the find services search box, I searched for S3 (Scalable storage in the cloud)
3. Once in S3 buckets I clicked the blue "Create Bucket" Button.
4. I gave my bucket a unique name and selected the region closest to me ie EU (Ireland), and clicked next.
5. On the next page as there is nothing that I needed to change, so I just clicked next.
6. On this page I unchecked the "Block all public access" option and clicked next.
7. I then clicked create bucket.

Once the bucket is created:

1. Go to properties on the bucket
2. Select static website hosting, and select "Use this bucket to host a website"
3. Enter "Index.html" and "Error.html" respectively as defaults (we dont use these)
4. Then save and go to permissions tab, select CORS
5. Enter the below:
   [
   {
   "AllowedHeaders": [
   "Authorization"
   ],
   "AllowedMethods": [
   "GET",
   "PUT"
   ],
   "AllowedOrigins": [
   "*"
   ],
   "ExposeHeaders": []
   }
   ]
6. Go to the bucket policy and copy and paste the below:
   {
   "Version": "2012-10-17",
   "Id": "Policy1617103285819",
   "Statement": [
   {
   "Sid": "Stmt1617103283972",
   "Effect": "Allow",
   "Principal": "_",
   "Action": [
   "s3:GetObject",
   "s3:PutObject",
   "s3:PutObjectAcl",
   "s3:PutObjectTagging",
   "s3:DeleteObject"
   ],
   "Resource": "arn:aws:s3:::gfd4trade/_"
   }
   ]
   }

Create IAM User/Group

1. Search for IAM in the search bar, select IAM app
2. Create group and name
3. Click until you have created the group
4. Next click 'policies' from the left hand menu, and then selected the 'JSON' tab.
5. Next click the 'import managed policy' link at the top right of the editor.
6. Search for S3 and selected the 'AmazonS3FullAccess' policy.
7. Click the 'Review Policy' Button, and gave it a name associated with my bucket, ie 'your-group-name', followed by clicking the 'create policy' button.
8. Go back to the group that you created earlier, so I selected 'Groups' from the left hand menu, and select the 'your-group-name' link.
9. Then select the 'Permissions' tab, click 'attach a policy'
10. Then search for the 'your-group-name' that you created, check it and click 'attach policy'
11. Then click create user
12. Name, ie 'your-user-name' and check the 'Programmatic access' option.
13. Click the 'Next: Permissions' button, and select you group and click next
14. Skip through till you have created the user
15. Then download the .csv file as you will need these for Secret keys in heroku

### Heroku deployment of this project

1. Login to heroku
2. Create a new app - easy to name it something similar to your python app
3. Go back to project and type in terminal 'heroku login'
4. Login to your profile on Heroku
5. Install the following:
    - gunicorn
    - psycopg2
    - dj_database_url
6. pip freeze the new install to a requirements.txt file so heroku can read them
7. Migrate all changes
8. push to git
9. In terminal run 'heroku config:set DISABLE_COLLECTSTATIC=1' to prevent collection of static and media files, AWS handles this
10. Create Procfile with the following:
    - web: gunicorn gate_fittings_direct.wsgi:application
11. Go to your heroku app and add the following config vars for the project:
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WH_SECRET
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - SECRET_KEY
12. use git push heroku main
13. Wait for all static files to be collected and then visit your site

### Cloning This Repository

Cloning is the process of downloading all the code still in format and run it locally on your own code editor.

To make a clone follow these steps:

1. Visit the repository [here](https://github.com/HowellsJonathan/milestone-4-gfd)
2. On the top of the file layout there will be a dropdown called "code", in the drop down there will be a clone option, navigate there
3. With the HTTPS method selected copy the URL.
4. Go to your desired code editor, make sure GIT is installed and in the terminal run
    ```
    git clone https://github.com/HowellsJonathan/milestone-4-gfd.git
    ```
5. All the files will then have been cloned to your workspace
6. Don't forget to add your own mongodb collection link and env.py file containing the config vars as seen above
7. To download the required packages run in the terminal
    ```
    pip install -r requirements.txt
    ```
    This will download every package that is in the file, allowing you to run the code without errors

## Credit

All images and information for products in property of [Gate Fittings Direct](https://www.ebay.co.uk/str/gatefittingsdirect)

[W3Schools](https://www.w3schools.com/)
[Stackoverflow](https://stackoverflow.com/)
[Code Institute](https://codeinstitute.net/) for all of their videos and tutor support on every matter
[Contact Email Sending Help](https://www.youtube.com/watch?v=05tut5WbyFA&t=18s)
