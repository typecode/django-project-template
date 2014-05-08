
# How to start a new Django Project
> #### Disclaimer
> I'm assuming that most of the setup has already been done so I won't be going over how to setup Python, `pip`, and `virtualenv` for the first time.

Throughout the following instructions I'll be using **`newproject`** as a placeholder for the project we're creating. Please, for all of our sakes, choose a better name.

----------

Start off my making sure all of the prerequisites are up-to-date:

    > pip install -U virtualenv virtualenvwrapper
    > npm update -g bower
    
Create a new `virtualenv` for the project and manually install Django so we can use the management commands:

    > mkvirtualenv newproject
    > pip install django
    
Move to the directory where you keep all of your projects (I use `~/Projects` but I think I've seen some of us using `~/Sites`) and create a new project using the most recent template:

    > cd ~/Projects
    > django-admin.py startproject newproject \
            --template=https://github.com/typecode/django-project-template/archive/develop.zip \
            --name bower.json
    
A new directory `newproject` will be created with the project's directory structure already in place.  Move into the new project and install the default Python:

    > cd newproject
    > pip install -r requirements.txt
    > bower install
    
We need to make sure the `virtualenv` we created knows about the new project and where it's located.  First we'll move to the right directory:

    > setvirtualenvproject
    > cdvirtualenv
    > cd bin/
    
Next you need to edit the `postactivate` file in that directory and make it look like the following:

    # This hook is run after this virtualenv is activated.
    export PYTHONPATH=$PYTHONPATH:$(cat $VIRTUAL_ENV/$VIRTUALENVWRAPPER_PROJECT_FILENAME)
    export DJANGO_SETTINGS_MODULE='apps.settings'
    
Then head back to you project and reactivate the `virtualenv` to pull in the changes we made:

    > workon newproject
    
At this point you should be able to start the development server and see (something resembling) the following:

    > django-admin.py runserver
    Validating models...

    0 errors found
    May 08, 2014 - 17:27:37
    Django version 1.6.4, using settings 'apps.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
Now that the server is running, we should initialize the `git` repo.  Stop the server and run:

    > git init
    > git checkout -b develop
    > git add .
    > git commit -m'Initial commit'
    
Create a new repo on GitHub and push the code to it:

    > git remote add origin git@github.com:typecode/newproject.git
    > git push --set-upstream origin develop
    
Congratulations!  There are beers in the fridge.
