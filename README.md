# Alices Wonderland: 

This website is designed for a fictional shop based in Wonderland. 

This website has been created as the Fifth Milestone project for Code Institute's Full Stack Software Development Diploma. It was built using a Full-Stack Toolkit, with the addition of E-commerce Applications such as Stripe. GitPod was used for writing the code for this website, as well as committing and pushing to GitHub. GitHub was then used to store the project after it had been pushed from GitPod. Once all the code had been written, Heroku was then used to deploy the website. 


### View the live website [here](https://alices-wonderland.herokuapp.com/)
![Live Website](/documents/images/readme_images/am_i_responsive.png)

***
## Table of content: 
 1. [Site Goals](#Site-Goals)
 1. [UX](#UX)
      1. [User Stories](#User-Stories)
      1. [Development Planes](#Development-Planes)
            * [Strategy](#Strategy)
            * [Scope](#Scope)
            * [Skeleton](#Skeleton)
            * [Surface](#Surface)
      1. [Color](#Color)
      1. [Font](#Font)
      1. [Images](#Images)
 1. [Features](#Features)
 1. [User Stories Met](#User-Stories-Met)
 1. [Bugs](#Bugs)
 1. [Technologies Used](#Technologies-Used)
 1. [Reports and Credits](#reports-and-credits)
      1. [Database Schema](#database-schema)
      1. [Marketing](#Marketing)
      1. [Testing](#Testing)
      1. [Validation](#Validation)
      1. [Accessibility](#Accessibility)
      1. [Deployment](#Deployment)
      1. [Credits](#Credits)
      1. [Acknowledgements](#Acknowledgements)

***
 
## Site Goals:

The goals for this site are as follows:
* Allow users to view products
* Allow users to add products to a basket
* Allow users to update or delete products from basket
* Allow users to make payments using Stripe
* Allow users to create a user profile
* Allow users to contact the store with any queries 
* Allow users to sign up for a monthly newsletter
* Allow authorised users to leave product reviews
* Allow store owner to collect user data to complete orders
* Allow store owners to approve user reviews 
* Allow the store owner to collect a database for marketing purposes in the form of a monthly newsletter

## UX:

### User stories:
To demonstrate the Agile approach that was used for this project, GitHub issues were used and a Kanban board was used to record all the user stories. 
The user stories were categorised using different labels, i.e MO - *Must have*, SO - *Should Have*, CO - *Could have* and W - *Won't have*.
Each story was then moved from 'To Do' to 'In Progress' to  'Done' as the project progressed, with some CO stories and WO stories moved to a future feature board.  


#### Project Progression: 
To view to progression of this project please view my project document by clicking [here](https://docs.google.com/spreadsheets/d/1tVnHzRfP0hPory2GUCfKkiKpfxxGOuGtRkeizTLchqo/edit?usp=sharing)

***

#### New User:  
* As a new user, I want to view all products   
* As a new user, I want to view products by price
* As a new user, I want to view products by category
* As a new user, I want to add products to my basket
* As a new user, I want to edit product quantities from my basket
* As a new user, I want to delete products straight from my basket
* As a new user, I want to securely checkout using a credit card
* As a new user, I want to create a profile 
* As a new user, I want to sign up for a newsletter
* As a new user, I want to contact the company with any queries


#### Returning User:
* As a returning user, I want to be updated on new products via the newsletter
* As a returning user, I want to contact the company with any queries
* As a returning user, I want to leave reviews on products I have purchased
* As a returning user, I want to edit my profile

## Development Planes:
To create a website that is comprehensive and informative for a user, as a developer you need to look at all aspects of the website and how someone who visits your website will use it. You have to consider all the user stories that have been outlined in the above sections.  

## Strategy
The strategy principle looks at user needs, as well as product/service objectives. This website's target audience was broken down into three categories:
### Roles: 
* New User
* Existing User  

### Demographic:
* Aged between 25 to 60
* Working individuals with disposable income

#### Lifestyle:
* Collectors
* Planet enthusiast
* Exotic Animal enthusiast


#### The website needs to allow users to:  
* View products by price, category or rating
* Add products to a basket
* Edit product quantities and delete products straight from the basket
* Make secure payments for their products via credit card
* Create a user profile
* Contact the store with enquiries
* Sign up for a newsletter
* Leave reviews for products they bought
* Visit the store's social media accounts straight from the site 

#### The website needs to allow the store owner to:  
* Add, edit and delete products straight from the frontend site 
* Collect information from order forms
* Collect email addresses for a monthly marketing newsletter


## Scope:  

With the structure in place, it was then time to move onto the scope plane. This was all about developing website requirements based on the goals set out in the strategy plane. These requirements are broken down into two categories. 

### Content Requirements:
1. The user will be looking for:
      * A list of products that can be purchased 
      * Information about the store owner
      * Links to the store's social media accounts

### Functionality Requirements:
1. The user will be able to:
      * Browse all the store's products
      * Add products to a basket
      * Edit their basket
      * Complete orders using Stripe
      * Create a user account
      * Update information on a user account
      * Leave reviews on products
      * Contact the store with enquires 
      * Sign up for a newsletter

***

## Skeleton:
[Wireframes](/documents/WIREFRAMES.md) were created to set out the initial appearance of the website while also making sure to keep the end-user in mind at all times. Wireframes were created using [Balsamiq](https://balsamiq.com/).  

## Surface:
[Please see the live site here](https://alices-wonderland.herokuapp.com/)  

***
[Back to top](#Alices-Wonderland)  

### Color: 
The green and purple colors used throughout this site were taken directly from the background image using a color picker. White has been used to enhance these colors and make the colors on the site pop on the screen. 
<details>
<summary>Color Palette</summary>

![Color Palette](/documents/images/readme_images/color_palette.png)
</details>


### Font:
Fonts used for this site were Merienda and Lora, both of which have been imported from [Google Fonts](https://fonts.google.com/)
 

### Images:
The images for this project were mostly taken from Pinterest.
 

***
[Back to top](#Alices-Wondeland)  


## Features:
There are several features on this site to help users get the most out of their visit to the site.  

### General:

<details>
<summary>Header and Nav Bar:</summary>

![Header and Nav Bar](/documents/images/readme_images/header.png)
</details>
Each page has a Header and Navigation bar section, located at the top of the page. 
The navigation bar consisted of links to a link to the About section, the user's Account section, the user's Shopping Basket and a search bar. As well as the shop logo when clicked will bring the user back to the home page. 
It also contains a navigation bar that has the categories the user can use to shop for the products. 


&nbsp;

<details>
<summary>Footer Information:</summary>

![Footer](/documents/images/readme_images/footer.png)
</details> 
Each page also contains a footer element that consists of the store's social media accounts, as well as usefull links and copyright information. 

&nbsp;

### Home page:
The *Home* page contains a main box that welcomes the user to the store and a link to shop, which brings the user to the *All Products* page  

<details>
<summary>Home:</summary>

![Home Page](/documents/images/readme_images/home.png)
</details> 

&nbsp;

### About Me page: 
The *About Me* page features an image of Alice and a bit about how Alices Wonderland came to be.  

<details>
<summary>About Me page:</summary>

![About Me](/documents/images/readme_images/about_me.png)
</details> 

&nbsp;

### All Products:  
The *All Products* page contains a list of all the products available in the shop. They are displayed using an image, the product name, price and rating. Users can click on the image of the product to bring them to that products *details* page

<details>
<summary>All Products:</summary>

![All Products](/documents/images/readme_images/all_products.png)
</details> 

&nbsp;

### Product Detail page:  
The *Products Details* page contains an image of the product, as well as the product name, description, price and rating. This is the page where a user can use the quantity input bar to decide how much of this product they would like. It also contains a "Keep Shopping" button which brings the user back to the *All Products* page and a "Add to Basket" button which adds the desired quantity of the product to their basket. Logged-in users will also see an "Add Product Review" button in the "Reviews" section of this page, allowing them to add product reviews.

<details>
<summary>Product Detail:</summary>

![Product Detail](/documents/images/readme_images/product_details.png)
</details> 

&nbsp;

### Basket: 
The *Basket* page contains a summary of the user's order. It is at this point that they can edit the quantity of the products in their basket, as well as delete them. It shows the users the total of their order, along with the shipping cost. It also contains a "Keep Shopping" button which brings the user back to the *All Products* page and a "Secure Checkout" button which brings the user to the *Checkout* page.

<details>
<summary>Basket:</summary>

![Basket](/documents/images/readme_images/basket.png)
</details> 

&nbsp;

### Checkout:
The *Checkout* page contains a summary of the user's order. It has an order form which the user will need to fill out to complete their order. It also contains an "Edit Basket" button which brings the user back to their *Basket* and a "Complete Order" button which will submit the order and product and order confirmation.
<details>
<summary>Checkout:</summary>

![Checkout](/documents/images/readme_images/checkout.png)
</details> 

&nbsp;

### Contact us page:
The *Contact Us* page contains a contact form which the user will need to fill out to send their enquiry to the store. Once the "Send Message" button is clicked the user will be directed back to *Home* and will be notified that they will be contacted soon.

<details>
<summary>Contact us:</summary>

![Contact us](/documents/images/readme_images/contact_us.png)
</details> 

&nbsp;

### Newsletter page:
The *Newsletter* page contains a form which the user will need to fill out to sign up for the store's newsletter. Once the "Sign Up!" button is clicked the user will be directed back to *Home* and will get a notification thanking them for signing up.

<details>
<summary>Newsletter:</summary>

![Newsletter](/documents/images/readme_images/newsletter.png)
</details> 

&nbsp;

### Sign up page:
The *Sign Up* page contains a form that the user will need to fill out if they wish to register for the site. Once the "Sign Up!" button is clicked the user will be directed back to a page informing them that a verification email has been sent to the email address provided and they will need to follow the link to complete their registration.

<details>
<summary>Sign up:</summary>

![Sign up](/documents/images/readme_images/sign_up.png)
</details> 

&nbsp;

### Login page:
The *login* page contains a form for the user to enter their login information. Once the "Sign In" button is clicked the user will be directed back to *Home*

<details>
<summary>Login:</summary>

![Login](/documents/images/readme_images/sign_in.png)
</details> 

&nbsp;

### My Profle page:
The *My Profile* page contains two elements. On the left-hand side of the screen, there is a form for users to update their shipping information. Once the "Update Information" button is clicked the page reloads with the new information. On the right-hand side of the screen, there is a list of the user's order history. If the user clicks on the Order number they will be directed to the order confirmation page. 

<details>
<summary>My Profile:</summary>

![My Profile](/documents/images/readme_images/my_profile.png)
</details> 

&nbsp;

### Logout page:
The *logout* page contains a notification asking the user if they are sure they would like to login out. Once the "Sign out" button is clicked the user is directed back to *Home*.

<details>
<summary>Logout:</summary>

![Logout](/documents/images/readme_images/log_out.png)
</details> 

&nbsp;

### 404 error page:
The *404 error* page contains a notification to let the user know that they have entered a URL that doesn't exist. There is an image of Alice falling down the rabbit hole and a link bringing the user back to the *All Products* page. 
<details>
<summary>Custom 404:</summary>

![Custom 404](/documents/images/readme_images/custom_404.png)
</details> 

&nbsp;



## Future Features:

1. Users can add their own ratings to products, which will then go towards the overall rating of the product.
1. Users can pay for their orders using PayPal
1. Users can register for an account using their social media account
1. Users can log in to their account using their social media account
1. User's accounts will be automatically logged out after a period of them being inactive. 

***


[Back to top](#Alices-Wonderland)  

## User Stories Met:
This section is to look back at the User stories we established during the strategy phase of the project. 
We are looking to see if we have met all the goals we set out. 
#### New User: 
* As a new user, I want to view all product  
**Met on the All Products Page**
* As a new user, I want to view products by price   
**Met on the All Products Page**
* As a new user, I want to view products by category    
**Met on the All Products Page**
*  As a new user, I want to add products to my basket  
**Met on the Product Details Page**
* As a new user, I want to edit product quantities from my basket   
**Met on the Basket page, users can edit products using the quantity bar and the edit button**
* As a new user, I want to delete products straight from my basket  
**Met on the Basket page, users can delete products using the delete button**
* As a new user, I want to securely checkout using a credit card  
**Met on the Checkout page, users can fill out the checkout form, add credit card details and make a secure payment using Stripe**
* As a new user, I want to create a profile  
**Met on the Register page**
* As a new user, I want to sign up for a newsletter  
**Met on the Newsletter page, users can fill out the form to sign up for a monthly newsletter**
* As a new user, I want to contact the company with any queries  
**Met on the Contact Us page, users can fill out the form to send queries to the store**

#### Returning User:
* As a returning user, I want to be updated on new products via the newsletter   
**Met on the Newsletter page, users can fill out the form to sign up for a monthly newsletter**
* As a returning user, I want to contact the company with any queries     
**Met on the Contact Us page, users can fill out the form to send queries to the store**
* As a returning user, I want to leave reviews on products I have purchased     
**Met on the Product Details page, once the user is logged in**
* As a returning user, I want to edit my profile    
**Met on the Profile page, once the user is logged in**


***

## Bugs:
### DataError:
After importing Django Countries, I edited the Country field in the checkout model so that a dropdown menu appeared on the checkout form for the country. When I tried to migrate the changes I was getting a "DataError". If I ran a planned migration there was no error occurring but as soon as I removed the plan the error would appear. 
* After a session with the CI tutors, it was noted that I had several test orders in the database that were done under the old model (writing in the actual Country) and the changes were making it so the Country Field used the official ISO 3166-1 list of countries which has a default max length of 2. Once these test orders were deleted from the database the migration was able to be completed. 

&nbsp;

### Card Details:
Card details not appearing on checkout:
* When I set up the checkout everything was working correctly except the card details box. This was not appearing at all. After re-watching the walk through video but everything seemed in order. After troubleshooting and chatting with some people in Slack and Stackoverflow it was suggested in the stripe_elements.js file to use the stripe public key in the "var stripe" instead of using an environment variable called stripePublicKey. Once I added the full key into the JS file that card details element appeared on the checkout page. 
<details>
<summary>Card Error:</summary>

![Card Details Error 1](/documents/images/readme_images/card_details_bug.png)
</details> 

<details>
<summary>Original JS file:</summary>

![Original JS file](/documents/images/readme_images/js.png)
</details> 

<details>
<summary>Updated JS file:</summary>

![Updated JS file](/documents/images/readme_images/updated_js.png)
</details>

&nbsp;

### Display Error:
If there were fewer than 4 images on a line they would display on top of each other:
* After speaking with my mentor it was found that the basic layout of my products template was not structured correctly. After removing an extra row that was in the content block fixed this problem straight away. 
<details>
<summary>Display Error:</summary>

![Display Error](/documents/images/readme_images/display_error.png)
</details> 

&nbsp;

### Edit Product Error:
When creating the add, edit and delete product functions for the site admin there was an Attribute Error occurring when I tried to test the 'Edit Product' functionality.
* After chatting with people on Slack it was suggested that I needed a for loop in the edit_products template to iterate through each field of the form. I tried this but I was still getting the Attribute Error. 
* I then went to ask the CI tutors. After a few different attempts to solve the issue, it was discovered that I was missing one of the asterisks in my forms.py file. Once this second asterisk was added the page and the form loaded correctly.  
<details>
<summary>Edit Product Error:</summary>

![Edit Product Error](/documents/images/readme_images/edit_product.png)
</details> 

&nbsp;

### Modal Error:
When adding the modal for a user to add reviews the modal was appearing but was faded and the user was not able to access the different elements:
* After doing some troubleshooting I saw several people say that the modal must be in a div where the position is fixed. I used Google Dev Tools to see if this was the case but still could not fix the error. I then contact the CI tutors who explained to me that because the modal position relates to the screen itself it was clashing with some CSS and by moving it to the end of the HTML file, outside the div. This solved the issue and the modal then worked correctly   
<details>
<summary>Modal Error 1:</summary>

![Modal Error 1](/documents/images/readme_images/modal_error.png)
</details> 

&nbsp;

### Webhook Error:
When an order was created the payment would go through but the user wouldn't receive a confirmation email. This was because the webhook handler wasn't being triggered. 
* After spending a lot of time going over the code and rewatching the CI videos to make sure I had set up the webhooks and Stripe correctly, I got onto the CI tutors. 
* We worked back through the code to see if we could get the terminal to print out the error. This wasn't working but Ger the tutor discovered that the Gitpod URL in the webhook on Stripe and the Gitpod URL for the workspace I was working in were different. Once I corrected this an error appeared in the terminal letting me know I had a FieldError as I had created a key called "original_basket" and it needed to be "originial_bag" for the Stripe webhooks to recognise it. As soon as this was changed the webhook handlers were triggered. 
* This led to another error in the terminal, this time it was a "TemplateDoesNotExist" error, as I had put the wrong paths in the webhook handler to the email subject and email body.
<details>
<summary>Webhook Error:</summary>

![Webhook Error](/documents/images/readme_images/webhooks.png)
</details> 

<details>
<summary>500 Error:</summary>

![500 Error](/documents/images/readme_images/webhook_500_error.png)
</details> 

<details>
<summary>Field Error:</summary>

![Field Error](/documents/images/readme_images/field_error.png)
</details> 

<details>
<summary>Template Error:</summary>

![Template Error](/documents/images/readme_images/template_does_not_exist.png)
</details> 


***

[Back to top](#Alices-Wonderland) 

## Technologies Used:
For this project, the following technologies were used.  

### Languages:
* HTML
* CSS
* Python
* Javascript
 

### Frameworks, Libraries, Programs & Applications Used:
* Django
* PostgreSQL
* Bootstrap
* AWS

#### Google Font
* Google Font was used to import the chosen fonts for this project.

#### Font Awesome
* Font Awesome was used on each page of the website to provide icons for UX purposes.  

#### GitPod
* GitPod was used for writing all the code for this project. It was also used to commit and push to GitHub.  

#### GitHub 
* GitHub was used to store this project.

#### Heroku
* Heroku was used to deploy the project.

#### Amazon Web Services
* AWS was used to store some of the images used in this project

#### Balsamiq 
* Balsamiq was used to draw initial Wireframes for this project.

#### Google Development Tools
* Google Dev Tools was used to edit code and check responsiveness before making the changes permanent.

*** 

[Back to top](#Alices-Wonderland)

## Reports and Credits:

### Database Schema:
To view the database schemas for this project click [here](/documents/DATABASE_SCHEMA.md)

### Marketing:
For marketing report please click [here](/documents/MARKETING.md)   
When adding the Facebook and Instagram links to the footer the *rel of "nofollow"* was used to inform search engines they can ignore these links.

## Testing:
Testing information can be viewed [here](/documents/TESTING.md)

### Validation:

* HTML:
      - Facebook Pixel code was removed from the base.html file as it was causing validation errors. To view this code please go to the [Marketing document](/documents/MARKETING.md) 
      - The HTML code came back it one error which was about using list items inside a nav tag. As this was something that was done in the CI walkthrough and these elements were an important part of the website I choose not to change the code. 

* CSS:
      - No errors were found when passed through the [W3C Validator tool](https://jigsaw.w3.org/css-validator/validator) 

* JavaScript: 
      - The Javascript used throughout this project was taken from the Code Institutes walkthrough project and edit to suit this project. 
      - No errors were found when passed through the [JSHints Validator](https://jshint.com/)

* Python: 
      - Since PEP8Online validator is no longer available, I followed the CI recommendation for validating my Python code. 
      - To view the steps taken to validate the Python code, please check the [Validation Document](/documents/VALIADTION.md)

***

[Back to top](#Alices-Wonderland)

### Accessibility:
To view the Lighthouse Reports for this project please click [here](/documents/LIGHTHOUSE_REPORT.md)

***

### Deployment and Development:
Deployment and Development information can be found [here](/documents/DEPLOYMENT_AND_DEVELOPMENT.md)

***

### Credits:
* The initial setup of the Django project was done following the Code Institutes walkthrough project.  


### Acknowledgements:
* I would like to thank Brian O’Hare for being my mentor for this project.
* I would like to thank Ed from tutor support.
* I would like to thank Ger from tutor support.
* I would like to thank Liz, who has been there to help and support me from the start
* I would like to thank the Slack community for all their support and encouragement during this and all my projects.


*** 
[Back to top](#Alices-Wonderland) 