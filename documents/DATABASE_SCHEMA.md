## Database Schema for Alices Wonderland:

To view the database schema for this project please see below 

## Table of content: 
 1. [Order Model](#order-model)
 1. [Order Line Item Model](#database-schema-for-alices-wonderland)
 1. [Sign Up Model](#sign-up-model)
 1. [Contact Us Model](#contact-us-model)
 1. [Category Model](#category-model)
 1. [Product Model](#product-model)
 1. [Review Model](#review-model)
 1. [User Profile Model](#user-profile-model)
 


### Order Model:

| Title             | Key in Database   | Form Validation                                                               | Data Type    |
| ----------------- | ----------------- | ----------------------------------------------------------------------------- | ------------ |
| Order Number      | order_number      | max length=32, null=False, editable=False                                     | CharField    |
| User Profile      | user_profile      | UserProfile, null=True, blank=True, on_delete=SET_NULL, related_name="orders" | Foreign Key  |
| Full Name         | full_name         | max_length=120, null=False, blank=False                                       | CharField    |
| Email Adress      | email_address     | max_length=350, null=False, blank=False,                                      | Email        |
| Phone             | phone             | max_length=20, null=True, blank=True                                          | CharField    |
| Country           | country           | blank_label='Country', max_length=200, null=False, blank=False                | CountryField |
| Postcode          | postcode          | max_length=20, null=False, blank=False                                        | CharField    |
| Town or City      | town_or_city      | max_length=40, null=True, blank=True                                          | CharField    |
| Street Address 1  | street_address_1  | max_length=80, null=True, blank=True                                          | CharField    |
| Street Address 2  | street_address_2  | max_length=80, null=True, blank=True                                          | CharField    |
| County            | county            | max_length=80, null=True, blank=True                                          | CharField    |
| Date              | date              | auto_now_add=True                                                             | DateTimeField|
| Shipping Cost     | shipping_cost     | max_digits=6, decimal_places=2, null=False, default=0                         | DecimalField |
| Order Total       | order_total       | max_digits=10, decimal_places=2, null=False, default=0                        | DecimalField |
| Grand Total       | grand_total       | max_digits=10, decimal_places=2, null=False, default=0                        | DecimalField |
| Original Bag      | original_bag      | null=False, blank=False, default=''                                           | TextField    |
| Stripe Payment ID | stripe_pid        | max_length=254, null=False, blank=False, default=''                           | CharField    |

***
&nbsp;

### Order Line Item Model:

| Title           | Key in Database | Form Validation                                                                    | Data Type    |
| --------------- | --------------- | ---------------------------------------------------------------------------------- | ------------ |
| Order           | order           | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | Foreign Key  |
| Product         | product         | Product, null=False, blank=False, on_delete=models.CASCADE                         | Foreign Key  |
| Quantity        | quantity        | null=False, blank=False, default=0                                                 | IntegerField |
| Line Itam Total | lineitem_total  | max_digits=6, decimal_places=2, null=False, editable=False                         | DecimalField |

***
&nbsp;

### Sign Up Model:

| Title         | Key in Database | Form Validation                        | Data Type  |
| ------------- | --------------- | ---------------------------------------| -----------|
| First Name    | first_name      | max_length=60, null=False, blank=False | CharField  |
| Last Name     | last_name       | max_length=60, null=False, blank=False | CharField  |
| Eamil Adresss | email_address   | null=False, blank=False                | EmailField |

***
&nbsp;

### Contact Us Model:

| Title         | Key in Database | Form Validation                                      | Data Type  |
| ------------- | --------------- | ---------------------------------------------------- | -----------|
| First Name    | first_name      | max_length=60, null=False, blank=False               | CharField  |
| Last Name     | last_name       | max_length=60, null=False, blank=False               | CharField  |
| Email Adresss | email_address   | null=False, blank=False                              | EmailField |
| Enquiry Type  | enquiry_type    | max_length=50, choices=ENQUIRY_CHOICE, blank=False   | CharField  |
| Enquiry       | enquiry         | max_length=500, null=True, blank=True                | TextField  |

***
&nbsp;

### Category Model:

| Title         | Key in Database | Form Validation                       | Data Type   |
| ------------- | --------------- | ------------------------------------- | ----------- |
| Name          | name            | max length=300                        | CharField   |
| Friendly Name | friendly_name   | max_length=300, null=True, blank=True | CharField   |

***
&nbsp;

### Product Model:

|    Title    | Key In Database |                    Form Validation                           |  Data Type   |
| ----------- | --------------- | ------------------------------------------------------------ | ------------ |
| Category    | category        | 'Category', null=True, blank=True, on_delete=models.SET_NULL | Foreign Key  |
| SKU         | sku             | max_length=150, null=True, blank=True                        | CharField    |
| Name        | name            | max_length=300                                               | CharField    |
| Description | description     | No validation                                                | TextField    |
| Price       | price           | max_digits=6, decimal_places=2                               | DecimalField |
| Rating      | rating          | max_digits=6, decimal_places=2                               | DecimalField |
| Image       | image           | null=True, blank=True                                        | ImageField   |

***
&nbsp;

### Review Model:

|    Title    | Key In Database |                    Form Validation  |  Data Type    |
| ----------- | --------------- | ----------------------------------- | ------------- |
| Reviewer    | reviewer        | User, on_delete=models.CASCADE      | Foreign Key   |
| Product     | product         | Product, on_delete=models.CASCADE   | Foreign Key   |
| Title       | review_title    | max_length=150                      | CharField     |
| Review      | content         | No validation                       | TextField     |
| Created On  | created         | auto_now=True                       | DateTimeField |
| Status      | status          | choices=STATUS, default=1           | IntegerField  |

***
&nbsp;

### User Profile Model:

| Title            | Key In Database        | Form Validation                              | Data Type     |
| -----------------| -----------------------| -------------------------------------------- | ------------- |
| user             | user                   | max length 50                                | OneToOneField |
| Phone Number     | users_phone            | max_length=20, null=True, blank=True         | CharField     |
| Town or City     | users_town_or_city     | max_length=40, null=True, blank=True         | CharField     |
| Street Address 1 | users_street_address_1 | max_length=80, null=True, blank=True         | CharField     |
| Street Address 2 | users_street_address_2 | max_length=80, null=True, blank=True         | CharField     |
| County           | users_county           | max_length=80, null=True, blank=True         | CharField     |
| Postcode         | users_postcode         | max_length=20, null=True, blank=True         | CharField     |
| Country          | users_country          | blank_label='Country', null=True, blank=True | CountryField  |


***
&nbsp;

Back to [Top of Page](#database-schema-for-alices-wonderland)    
Click [here](/README.md) to get back to README.doc