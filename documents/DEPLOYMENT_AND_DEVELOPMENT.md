## Deployment and Development:   

This project was developed using [GitPod](https://gitpod.io/), committed and pushed to [GitHub](https://github.com/) using a GitPod terminal and deployed using [Heroku](https://id.heroku.com/login)  


The following steps were taken:

### Step one: 
#### Setting up a new app in Heroku.
1. Select "New" and "Create new app".
1. Name the new app and click "Create new app".
1. In "Settings" under the Config Vars (we will discuss these at a later point)
click on  "Add BuildPack" and add Heroku/Python.

***

### Step two: 
#### Add the datebase: 
1. Once the app is created click on the "Resources" tab and search for Postgres. Once option appear add Heroku Postgres to the project.
1. Click on the "Settings" tab at the top of the page
1. Open the "Reveal Config Vars" section to reveal the DATABASE_URL: this is automatically generated when you add Heroku Postgres to the project
1. In GitPod create an env.py file and copy in the string value from Heroku.

***

### Step three: 
#### Add the Config Vars: 
1. As above, click on the "Settings" tab at the top of the page
1. Open the "Reveal Config Vars" section and input the following information:
      * SECRET_KEY: This is a key that you make up but do not give to anyone 
      * AWS_ACCESS_KEY: set to the key provided by [AWS](https://aws.amazon.com/) to be used as a storage platform for all the media and static file for this site     
      * AWS_SECRET_ACCESS_KEY: tset to the key provided by [AWS](https://aws.amazon.com/)        
      ***(These two keys need to be kept secret or else someone would be able to use them to store data in your account and you will be cahrged for it by Amazon)***
      * USE_AWS: This should be set to TRUE and will be used to check if you are in a development enviroment or if your are on the deployed Heroku site and use the correct static and media files accordingly 
     
#### Note:
All the above Heroku Config vars have also been put into an env.py file in Gitpod. This is done in the following way. 
1. At the top level add a file called env.py 
1. Find your gitignore file and add env.py it. This will provent the env.py fil from being pushed to your GitHub repo when you push files. 
1. In the env.py file `import os` at the top of the file. 
1. The envirment variables will then be set up as followed    
`os.environ["USE_AWS"] = "True"`   
Following this stucture add all the Config vars that are required from Heroku 
*The env.py file is used to protect keys that should only be accessed by the developer*  

***

### Step Four:
#### Linking GitHub and Heroku:
1. Now go to the "Deploy" tab at the top of the page and select your deploy method and repository.
1. In "Deployment Method" click on "GitHub" to connect them.
1. Once they are connected search for the repository you want and hit "connect".

***

### Step Five:
#### Update the settings.py file:
1. Import Path from pathlib, dj_database_url and os into the settings.py file within the project.
1. Update the default SECRET_KEY variable provided by Django to the SECRET_KEY you created in the env.py file. 
1. Update the DATABASES so it uses the one from the env.py file. 
1. Perform a Migrations so that Heroku Database is now being used as the backend database. 

***


### Step Six: 
#### Setting up templates:
1. In settings.py under the BASE_DIR key add a TEMPLATES_DIR variable and make it equal to `os.path.join(BASE_DIR, 'templates')`
1. Then scroll down to TEMPLATES and update 'DIRES' with the new TEMPLATE_DIR variable

***

### Step Seven:
#### Set up Allowed Hosts:
1. Under DEBUG = TRUE to the ALLOWED_HOSTS key. Inside the square brackets make it equal to your heroku app url and 'localhost'

***

### Step Eight:
#### Set up AWS S3 bucket in settings.py:   
 ***(To set up an AWS account and buckets check out the [Amazon Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) )*** 
1. After you have created the Config vars for AWS (as above) and added it to the env.py you must now set it up in the settings.py 
1. Before this you will need to install two new packages. 
      * boto3 
      * django storages
1. Don't forget to freeze your requirements.txt file once these are installed 
1. In your settings.py file make your way down to INSTALLED_APPS, then add  'storages'. Put these under the django apps and don't forget the comma at the end or you will get an error.
1. You now have to tell your app to use AWS as the storage for your media and static files but only when it has been deployed to Heroku. This is done by writting the following code in your settings.py file, under the STATIC_URL.
`if 'USE_AWS' in os.environ:`   
`# S3 Bucket Config`   
`AWS_STORAGE_BUCKET_NAME = 'alices-wonderland'`   
`AWS_S3_REGION_NAME = 'eu-west-1'`   
`AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')`   
`AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')`   
`AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`   
`# Static and media files`   
`STATICFILES_STORAGE = 'custom_storages.StaticStorage'`   
`STATICFILES_LOCATION = 'static'`   
`DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'`   
`MEDIAFILES_LOCATION = 'media'`   
`# Override static and media URLs in production`   
`STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'`   
`MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'`   


***

### Step Nine:
#### Set up Stripe settings.py:   
 ***(To set up Stipe account visit [Stripe](https://stripe.com/) )*** 
1. After you have created your stripe account you will need to add some more variables to your Config vars in Heroku and your env.py file
      * STRIPE_PUBLIC_KEY
      * STRIPE_SECRET_KEY
1. You will then need to install Stripe in Gitpod.   
***Don't forget to freeze your requirements.txt file once these are installed***   

1. You now have to set up Stripe in your settings.py file. This can be done in the following way
`# Stripe`   
`FREE_SHIPPING_THRESHOLD = 100`   
`STANDARD_SHIPPING_PERCENTAGE = 10`   
`STRIPE_CURRENCY = 'EUR'`   
`STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')`   
`STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')`        

To find out more about using Stripe check out their documentation [here](https://stripe.com/docs)

***

### Step Ten:
#### Set up Emailing in settings.py:   
 ***(This is used to send emails from a Gmail account from your site )*** 
1. Log into your gmail account. 
1. Go to the settings tab and navigate to "Accounts and Imports"
1. Once there click on "Other Google Account Settints"
1. Click in the "Security" tab and then turn on "2-Step Verification"
1. Once that is done you can now create an app password specific to your django app, this will allow you send emails from Gmail.
1. Under the "Sign into Google" heading you will now see a new option called "App Passwords". Click on it
1. On the "App Password" screen, select Main for the app and Other for the device. Then type in Django for the device name.
1. Click on the "Generate" button, this will bring up a 16 character that you can then add to Heroku and yout env.py file as you Email password.

1. You now can set up emailing in your settings.py file. This can be done in the following way:
When we are using the development enviroment the emails will still be sent from django but for the deployed site it will be sent by Gmail. 
`EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`   
`EMAIL_USE_TLS = True`   
`EMAIL_PORT = 587`   
`EMAIL_HOST = 'smtp.gmail.com'`   
`EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')`   
`EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')`  
`DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')`           

***

### Step Eleven:
#### Create a Procfile:
1. On the same level as your env.py and README.md files create a Procfile.
1. Inside this file write **web: gunicorn *Your App Name*.wsgi`**
1. This tells Heroku how to run our project.

***

### Step Twelve:
#### Create a robots.txt:
1. On the same level as your env.py and README.md files create a robots.txt file.
1. Inside this file write   
`User-Agent: *`   
`Disallow: /private/`   
`Disallow: /junk/*`   
1. Then in your main app views.py file add   
`@require_GET`   
`def robots_txt(request):`   
    `lines = [`   
        `"User-Agent: *",`   
        `"Disallow: /private/",`   
        `"Disallow: /junk/",`  
    `]`   
    `return HttpResponse("\n".join(lines), content_type="text/plain")`   
1. This file is very important for the SEO of your site as it can be used to prevent search engines from crawling specific parts of your website and to give search engines helpful tips on how they can best crawl your website.


***

### Step Thirteen:
#### Create a sitemap.xml file:
1. On the same level as your env.py and README.md files create a sitemap.xml file.
1. To generate a sitemap you can use a site such as [Free Online Sitemap Generator](www.xml-sitemaps.com )  
1. This file is aslo quite important for the SEO of your site. It is used to provide information about the pages, videos, and other files on your site, and the relationships between them. Search engines like Google read this file to crawl your site more efficiently.


***

### Step Fourteen:
#### Deploying: 
1. You can choose to either deploy your project using "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
      * Note, if you click on Automatic Deploys, you will still need to hit deploy branch to build the site
1. Heroku will now deploy the site.
      * Note: before delpoying the final project you must remember to change DEGUGG from TRUE to FALSE in your app settings through GitPod

***

Back to [Top of Page](#deployment)   
Back to [README.doc](/README.md)
