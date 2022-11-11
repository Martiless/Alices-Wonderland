# Alices Wonderland: 

This website is designed for a fictional shop based in Wonderland. 

This website has been created as the Fifth Milestone project for Code Institute's Full Stack Software Development Diploma. It was built using a Full-Stack Toolkit, with the addition of E-commerce Applications such as Stripe. GitPod was used for writing the code for this website, as well as committing and pushing to GitHub. GitHub was then used to store the project after it had been pushed from GitPod. Once all the code had been written, Heroku was then used to deploy the website. 


### View the live website [here](https://alices-wonderland.herokuapp.com/)
![Live Website]()

***
## Table of content: 
 1. [Site Goals](#Site-Goals)
 1. [UX](#UX)
      1. [User Stories](#User-Stories)
      1. [Development Planes](#Development-Planes)
            * [Strategy](#Strategy)
            * [Scope](#Scope)
            * [Structure](#Structure)
            * [Skeleton](#Skeleton)
            * [Surface](#Surface)
      1. [Color](#Color)
      1. [Font](#Font)
      1. [Images](#Images)
 1. [Marketing](#Marketing)
      1. [Facebook](#Facebook)
      1. [Instagram](#Instagram)
      1. [SEO](#SEO)
 1. [Features](#Features)
 1. [Testing](#Testing)
 1. [User Stories Met](#User-Stories-Met)
 1. [Bugs](#Bugs)
 1. [Technologies Used](#Technologies-Used)
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
* As a new user, I want to securly checkout using a credit card
* As a new user, I want to create a profile 
* As a new user, I want to sign up for a newsletter
* As a new user, I want to contact the company with any queries


#### Returning User:
* As a returning user, I want to be updated on new products via newsletter
* As a returning user, I want to contact the company with any queries
* As a returning user, I want to leave reviews on products I have purchased
* As a returning user, I want to edit my profile

## Development Planes:
To create a website that is comprehensive and informative for a user, as a developer you need to look at all aspects of the website and how someone who visits your website will use it. You have to consider all the user stories that have been outlined in the above sections.  

## Strategy
The strategy principal looks at user needs, as well product/service objectives. This website's target audience was broken down into three categories:
### Roles: 
* New User
* Existing User  

### Demographic:
* Aged between 25 to 60
* Working individuals with disposable income

### Psychographic:

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
* Visit the stores social media accounts straight from the site 

#### The website needs to allow the store owner to:  
* Add, edit and delete products straight from the frontend site 
* Collect information from order forms
* Collect email address for the purpose of monthly marketing newsletter
* Approve of product reviews to unsure they are genuine customer reviews and not spam


## Scope:  

With the structure in place, it was then time to move onto the scope plane. This was all about developing website requirements based on the goals set out in the strategy plane. These requirements are broken down into two categories. 
### Content Requirements:
1. The user will be looking for:
      * A list of products that can be purchased 
      * Information about the store owner
      * Links to the stores social media accounts

### Functionality Requirements:
1. The user will be able to:
      * Browse all the stores products
      * Add products to a basket
      * Edit their basket
      * Complete orders using Stripe
      * Create a user account
      * Update information on user account
      * Leave reviews on products
      * Contact the store with enquires 
      * Sign up for a newsletter

***

## Structure:

The information above was then used to create a structure for the website. Below is a site map showing how users can navigate the website intuitively 
<details>
<summary>Sitemap</summary>

![Sitemap]()
</details>


## Skeleton:
[Wireframes](/documents/WIREFRAMES.md) were created to set out the initial appearance of the website while also making sure to keep the end-user in mind at all times. Wireframes were created using [Balsamiq](https://balsamiq.com/).  

## Surface:
[Please see the live site here](https://alices-wonderland.herokuapp.com/)  

***
[Back to top](#Alices-Wonderland)  

### Color: 
The green and purple colors used throughout this site were taken directly from the backgroud image using a color picker. White was then used to enhace them and make them pop on hte screen. 



### Font:
Fonts used for this site were Merienda and Lora, both of which have been imported from [Google Fonts](https://fonts.google.com/)
 

### Images:
The images for this project were mostly taken from Pinterest.
 


***
[Back to top](#Alices-Wondeland)  

## Marketing:
For marketing report please click [here](/documents/MARKETING.md)


## Features:
There are several features on this site to help users get the most out of their visit to the site.  

### General:

<details>
<summary>Header and Nav Bar:</summary>

![Header and Nav Bar]()
</details>
Each page has a Header and Navigation bar section, located at the top of the page. 
The navigation bar consisted of links to a link to the About section, the users Account section, the users Shopping Basket and a search bar. As well as the shop logo with when click will bring the user back to the home page. 
It also contains a navigation bar that has the categories the user can use to shop the products. 

&nbsp;

<details>
<summary>Footer Information:</summary>

![Social Media]()
</details> 
Each page also contains a footer element that consists of the store's social media accounts, as well as usefull links and copyright information. 

&nbsp;

### Home page:
The *Home* page contains the header and footer as mentioned above. It also contains a main box that welcomes the user to the store and a link to shop, which brings the user to the *All Products* page  

<details>
<summary>Home Page:</summary>

![Home Page]()
</details> 

&nbsp;

### About Me page:  

<details>
<summary>About Me page:</summary>

![About Me page]()
</details> 

&nbsp;

### All Products page:  

<details>
<summary>All Products page:</summary>

![All Products page]()
</details> 

&nbsp;

### Product Detail page:  

<details>
<summary>Product Detail page:</summary>

![Product Detail page]()
</details> 

&nbsp;

### Basket: 

<details>
<summary>Basket:</summary>

![Basket]()
</details> 

&nbsp;

### Checkout:

<details>
<summary>Checkout:</summary>

![Checkout]()
</details> 

&nbsp;

### Contact us page:

<details>
<summary>Contact us page:</summary>

![Contact us page]()
</details> 

&nbsp;

### Newsletter page:

<details>
<summary>Newsletter page:</summary>

![Newsletter page]()
</details> 

&nbsp;

### Sign up page:

<details>
<summary>Sign up page:</summary>

![Sign up page]()
</details> 

&nbsp;

### Login page:

<details>
<summary>Login page:</summary>

![Login page]()
</details> 

&nbsp;

### 404 error page:

<details>
<summary>404 error page:</summary>

![404 error page]()
</details> 

&nbsp;



## Future Features:


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
* As a new user, I want to securly checkout using a credit card  
**Met on the Checkout page, users can fill out the checkout form, add credit card details and make a secure payment using Stripe**
* As a new user, I want to create a profile  
**Met on the Register page**
* As a new user, I want to sign up for a newsletter  
**Met on the Newsletter page, users can fill out the formto sign up for a monthly newsletter**
* As a new user, I want to contact the company with any queries  
**Met on the Contact Us page, users can fill out the form to send queries to the store**

#### Returning User:
* As a returning user, I want to be updated on new products via newsletter   
**Met on the Newsletter page, users can fill out the formto sign up for a monthly newsletter**
* As a returning user, I want to contact the company with any queries     
**Met on the Contact Us page, users can fill out the form to send queries to the store**
* As a returning user, I want to leave reviews on products I have purchased     
**Met on the Product Details page, once the user is logged in**
* As a returning user, I want to edit my profile    
**Met on the Profile page, once the user is logged in**

***

## Testing:
Testing information can be viewed [here](/documents/TESTING.md)

***

## Bugs:
### DataError:
After importing Django Countries, I edited the Country field in the checkout model so that a dropdown menu appeared on the checkout form for the country. When I tried to migrate the changes I was getting a "DataError". If I ran a planned migration there were no error occuring but as soon as I removed plan the error would appear. 
* After a session with the CI tutors it was noted that I had a number of test orders in the database that were done under the old model (writting in the actual Country) and the changes were making it so the Country Field used the official ISO 3166-1 list of countries which has a default max lenght of 2. Once these test orders were deleted from the database the migration was able to be completed. 

&nbsp;

### Card Details:
Card details not appeating on checkout:
* When I set up the checkout eveything was working correctly except the card details box. This was not appearing at all. After rewatching the walk through video but everything seemed in order. After troubleshooting and chatting with some people in Slack and Stackoverflow it was suggested in the stripe_elements.js file to use the stripe public key in the "var stripe" instead of using an environment variable called stripePublicKey. Once I added the full key into the JS file that card details element appeared on the checkout page. 
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
If there were less than 4 images on a line they would display on top of eachother:
* After speaking with my mentor it was found that the basic layout of my products template was not structured correctly. After removing an extra row that was in the content block fixed this problem straight away. 
<details>
<summary>Display Error:</summary>

![Display Error](/documents/images/readme_images/display_error.png)
</details> 

&nbsp;

### Edit Product Error:
When creating the add, edit and delete product functions for the site admin there was an Attribute Error occuring when I tried to test the 'Edit Product' functionality.
* After chatting with people on Slack it was suggested that I needed a for loop in the edit_products template to iterate through the each field of the form. I tried this but I was still getting the Attribute Error. 
* I then went to ask the CI tutors. After a few different attempts to solve the issue, it was discovered that I was missing one of the asterisks in my forms.py file. Once this second asterisk was added the page and the form loaded correctly.  
<details>
<summary>Edit Product Error:</summary>

![Edit Product Error](/documents/images/readme_images/edit_product.png)
</details> 

&nbsp;

### Modal Error:
When adding the modal for user to add reviews the modal was appearing but was faded and the user was not able to access the different elements:
* After doing some troubleshooting I saw a number of people say that the modal must be in a div where the position is fixed. I used Google Dev Tools to see if this was the case but still could not fix the error. I then contact the CI tutors who explained to me that because the modal postion relates to the screen itself it was clashing with some css and by moving it to the end of the html file, outside the div. This solved the issue and the modal then worked correctly   
<details>
<summary>Modal Error 1:</summary>

![Modal Error 1](/documents/images/readme_images/modal_error.png)
</details> 

&nbsp;

### Modal Submit Error:
When adding the modal for user to add reviews the modal was appearing but was faded and the user was not able to access the different elements:
* After doing some troubleshooting I saw a number of people say that the modal must be in a div where the position is fixed. I used Google Dev Tools to see if this was the case but still could not fix the error. I then contact the CI tutors who explained to me that because the modal postion relates to the screen itself it was clashing with some css and by moving it to the end of the html file, outside the div. This solved the issue and the modal then worked correctly   

&nbsp;

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

#### Figma
* Figma was used during the structure phase of this project. It was used to create a sitemap of the website. 

#### Google Development Tools
* Google Dev Tools was used to edit code and check responsiveness before making the changes permanent.

*** 

[Back to top](#Alices-Wonderland)

## Validation:

* HTML:
      - No errors were found when passed through the [W3C Validator tool]()
      - To view screenshots of validations please click [here](/documents/VALIDATION.md)

* CSS:
      - No errors were found when passed through the [W3C Validator tool]() 

* JavaScript: 
      - No costume Javascript was used in this project. The Javascript included at the end of my base.html was taken from the Code Institutes walkthrough project. 

* Python: 
      - No errors were found when passed through [PEP8 Validator]()

***

[Back to top](#Alices-Wonderland)

## Accessibility:
![LightHouse Report]()

***

## Deployment:
Deployment information can be found [here](/documents/DEPLOYMENT.md)

***

## Credits:
* The initial setup of the Django project was done following the Code Institutes walkthrough project.  


## Acknowledgements:
* I would like to thank Brian O’Hare for being my mentor for this project.


*** 
[Back to top](#Alices-Wonderland) 