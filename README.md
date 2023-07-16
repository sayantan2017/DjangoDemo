# Django Demo

Step 1 - pip install djangorestframework
Step 2 - 
After installing the REST framework, go to settings.py, and in INSTALLED_APPS add ‘rest_framework’ at the bottom. 

![image](https://github.com/sayantan2017/DjangoDemo/assets/26603086/4563ee61-c3ca-48e8-a554-9e9da5d07fbe)

Step 3 - 
After installing the DRF and adding it to settings.py, let’s create an app using the command – 

python manage.py startapp demo (app name)

Let’s add this app to INSTALLED_APPS and urls.py also.

![image](https://github.com/sayantan2017/DjangoDemo/assets/26603086/6cc3a7c8-5a40-4af6-93ce-2b603abf5818)

Step 4 -
Creating the model

![image](https://github.com/sayantan2017/DjangoDemo/assets/26603086/405512da-83c2-4bc9-9fb9-8553eaecd56c)

Step 5 -
Serialization
Serializers in Django REST Framework convert the objects into data types that are understandable by javascript and front-end frameworks. 

Add a new python file called serializer.py

![image](https://github.com/sayantan2017/DjangoDemo/assets/26603086/d30bf650-c67d-496c-a3b7-4d39f2758a7f)

Step 6 -

Add routing

![image](https://github.com/sayantan2017/DjangoDemo/assets/26603086/e069bb3d-963c-49d3-a3a2-c3b34e2e024d)

![image](https://github.com/sayantan2017/DjangoDemo/assets/26603086/c63d48ff-b612-4693-b2a6-29df18afc99d)





