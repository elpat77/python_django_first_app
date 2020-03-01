# Using python and Django (for mac using python3)
## Instructions for setting up a project and a basic application

## Useful terminal commands:

- Show python version:
    > python3 —version

- Show pip version:
    > pip3 --version

- Show the installed packages: 
    > pip3 freeze 

- Install virtual environment (one time installation): 
    > pip3 install virtualenv 

- Deactivate the environment
    > deactivate

===========================================================================
## To create a new project:

*Do this from the terminal as it's easier to start the project this way, don’t launch VS code yet:*

1.  Create a new folder
    > mkdir new_folder

2.  cd into that folder
    > cd new_folder

3. Create a python environment (Can name it anwyay, but usually it'll be called env):
    > python3 -m venv venv

4. Activate the project
    > source venv/bin/activate

5. Install Django
    > pip3 install Django

6. Create the actuall project, in this case named todo_app
    > django-admin startproject todo_app

7. Launch VS Code
    > code .

8. Deactivate the project from terminal side, we will start it on VS Code now
    > deactivate 

9. On VS Code  we will now see the project, launch a new terminal inside this project. Note the project will have the prefix (venv)

10. cd into the actuall project (notice there will be a todo_app inside todo_app)
    > cd todo_app

11. Start a new app (can anme it anyway, in this case todo_list):
    > python3 manage.py startapp todo_list

12. Start a server to verify everything is up and running:
    > python3 manage.py runserver

13. We might need to migrate changes, there might be a message telling us to do this:
    > python3 manage.py migrate

14. Once the server opens we can also go to an admin dashboard by attaching "/admin" to the url:
http://127.0.0.1:8000/admin/
 - To Create a super user execute the command, enter a user name and a password
    > python3 manage.py createsuperuser
 - Use such credentials to login to the admin dashborad 

 15. The app should be open and running. Congratulations!


===========================================================================
## File Changes:

After verifying the app launches we can start editing certain files and building our app.

### Inside the todo_app folder:
0. Make sure you are in the todo_app folder
1. Open the settings.py file.
    - Under Installed_APPS add the new app (in this case todo_list) at the bottom of the list.

    Should look something like this:

        INSTALLED_APPS = [
            ..... ,
            ..... ,
            'todo_list'
        ]

2. Open the urls.py file. Here is where we will add our url paths. In this case we wanted to add the todo.list.url:

    The whole file should look like this:

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('todo_list.urls'))
        ]


### Inside the todo_list folder:

0. Make sure you are in the todo_list folder

1. Create a folder named templates, this is where the html files needed for the app will go. In this case I created home.html. 
This file will display the get, posts and delete requests. It looks like this:


        <body>
        <!-- this starts a block  -->
        {% block content %}

        <!-- the posts will be displayed here -->
        <form method="POST">
           <!-- The CSRF middleware and template tag provides easy-to-use 
            protection against Cross Site Request Forgeries -->
            {% csrf_token %}
            <!-- input box and submit button used to enter and submit posts -->
            <input type="text" name="item" placeholder="add todo">
            <button type="submit">Submit</button>
        </form>
        <!-- opening for block  where the items will be displayed  -->
        {% for todos in todo_list %}
        <h1>{{ todos.item }}</h1>
        <!-- This will communicate to the delete URL which handles the delete request -->
        <a href="{% url 'delete' todos.id %}">Delete</a>

        <!-- end both blocks -->
        {% endfor %}
        {% endblock %}
        </body>

2. Under todo_list create a file called > urls.py 

3. Open the urls.py file. Here is where we will add our url paths. In this case we wanted to add our route to home and and other app paths, such as the delete path. 


        from django.urls import path
        from . import views

        urlpatterns = [
            path(' ', views.home, name='home'),
            path('delete<todo_id>', views.delete, name='delete'),
        ]


4. Inside views.py define both routes and add the Post and delete logic:

        def home(request):

            if request.method == "POST":
                form = ListForm(request.POST or None)

                if form.is_valid():
                 form.save()

                 todo_list = List.objects.all
                    return render(request, 'home.html', {"todo_list": todo_list})

            else:
                todo_list = List.objects.all
                return render(request, 'home.html', {"todo_list": todo_list})


        def delete(request, todo_id):
            item = List.objects.get(pk=todo_id)
            item.delete()
            return redirect('home')


5. Inside models.py we set-up our database. In this case we used a class named  List

        from django.db import models

        # Create your models here.

        class List(models.Model):
            item = models.CharField(max_length=200)
            completed = models.BooleanField(default=False)

            def __str__(self):
                return self.item

6. On admin.py we import those models

        from django.contrib import admin
        from .models import List

        # Register your models here.

        admin.site.register(List)


7. In order for the changes to be reflected on the database, run :

    > python3 manage.py makemigrations

    > python3 manage.py migrate


8. Run the app and you should be able to make post and delete new items. 
    > python3 manage.py runserver

9. Login to the admin portal and using this UI, you should be able to make any changes, post , delete, view, etc.

10. I hope this is all very helpful!



