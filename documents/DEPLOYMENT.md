## Deployment:   

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
      * CLOUDINARY_URL: set to the url provided by [Cloudinary](https://cloudinary.com/) (***This also needs to be added to your env.py file in GitPod***)
      * SECRET_KEY: This is a key that you make up but do not give to anyone (***This Secert Key is the same one you created in your env.py file in GitPod***)  
*The env.py file is used to protect keys that should only be accessed by the developer*  

***

### Step Four:
#### Update the settings.py file:
1. Import Path from pathlib, dj_database_url and os into the settings.py file within the project.
1. Update the default SECRET_KEY variable provided by Django to the SECRET_KEY you created in the env.py file. 
1. Update the DATABASES so it uses the one from the env.py file. 
1. Perform a Migrations so that Heroku Database is now being used as the backend database. 

***

### Step five:
#### Set up Cloudinary in settings.py:
1. After you have created the Config vars for Cloudinary (as above) and added it to the env.py you must now set it up in the settings.py 
1. In your settings.py file make your way down to INSTALLED_APPS, then add  'cloudinary_storage' and 'cloudinary'. Put these under the django apps and don't forget the comma at the end or you will get an error.
1. You now have to tel your app to use Cloudinary as the storage for your media and static files. This is done by writting the following code under the STATIC_URL   
`STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'`
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`
`STATICROOT = os.path.join(BASE_DIR, 'staticfiles')`
`MEDIA_URL = '/media/'`
`DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`

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
#### Create a Procfile:
1. On the same level as your env.py and README.md files create a Procfile.
1. Inside this file write **web: gunicorn *Your App Name*.wsgi`**
1. This tells Heroku how to run our project.

***

### Step Nine:
#### Linking GitHub and Heroku:
1. Now go to the "Deploy" tab at the top of the page and select your deploy method and repository.
1. In "Deployment Method" click on "GitHub" to connect them.
1. Once they are connected search for the repository you want and hit "connect".

***

### Step Ten:
#### Deploying: 
1. You can choose to either deploy your project using "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
      * Note, if you click on Automatic Deploys, you will still need to hit deploy branch to build the site
1. Heroku will now deploy the site.
      * Note: before delpoying the final project you must remember to change DEGUGG from TRUE to FALSE in your app settings through GitPod

***

Back to [Top of Page](#deployment)   
Back to [README.doc](/README.md)
