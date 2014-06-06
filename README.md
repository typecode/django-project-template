
# How to start a new Django Project
> #### Disclaimer
> I'm assuming that most of the setup has already been done so I won't be going over how to setup Python, `pip`, VirtualBox, or Vagrant for the first time.

Throughout the following instructions I'll be using **`newproject`** as a placeholder for the project we're creating. Please, for all of our sakes, choose a better name.

----------

Start off my making sure all of the prerequisites are up-to-date.  We need Django and Bower to run some of the bootstrapping so they need to be installed globally:

    > pip install -U django
    > npm update -g bower
    
Move to the directory where you keep all of your projects (I use `~/Projects` but I think I've seen some of us using `~/Sites`) and create a new project using the most recent template:

    > cd ~/Projects
    > django-admin.py startproject newproject \
            --template=https://github.com/typecode/django-project-template/archive/develop.zip \
            --name bower.json
    
A new directory `newproject` will be created with the project's directory structure already in place.  Move into the new project and install the default Python:

    > cd newproject
    > bower install
    
We need to create a deploy key for the Vagrant instance to use private Type/Code repos:

    > ssh-keygen -N '' -f salt/roots/app/files/tc-deploy
    
At this point you have a fully-prepped Django project get everything pushed to Github:

    > git init
    > git checkout -b develop
    > git add .
    > git commit -m'Initial commit'
    
Create a new repo on GitHub and push the code to it:

    > git remote add origin git@github.com:typecode/newproject.git
    > git push --set-upstream origin develop
    
Now we can start the Vagrant instance (could take a while):

    > vagrant up

When it's done `ssh` to the Vagrant instance and edit `~/.bashrc` to make sure virtualenvwrapper will work correctly:

    > vagrant ssh
    > echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
    > echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
    > source ~/.bashrc
    
**The next time you start working you can `vagrant ssh` and continue from here.**
    
Now you can activate the `virtualenv`:

    > workon app
    
Interact with the app as usual:

    > django-admin.py syncdb
    ...
    > django-admin.py runserver 0.0.0.0:8000
    Validating models...

    0 errors found
    May 08, 2014 - 17:27:37
    Django version 1.6.4, using settings 'apps.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
Be sure to include `0.0.0.0:8000` with `runserver` so that the app is accessible at [http://localhost:8000] on your host machine (i.e., from Chrome on your Mac).
    
Congratulations!  Hopefully there are beers in the fridge.
