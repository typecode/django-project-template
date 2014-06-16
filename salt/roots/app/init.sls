

build-essential:
    pkg:
        - installed

# python and pip packages
python-dev:
    pkg:
        - installed

python-pip:
    pkg:
        - installed

        - require:
            - pkg: build-essential
            - pkg: python-dev

virtualenv:
    pip:
        - installed

        - require:
            - pkg: python-pip

virtualenvwrapper:
    pip:
        - installed

        - require:
            - pip: virtualenv

# postgres dev
libpq-dev:
    pkg:
        - installed

# node and npm packages
nodejs:
    pkg:
        - installed

nodejs-legacy:
    pkg:
        - installed

        - require:
            - pkg: nodejs

npm:
    pkg:
        - installed

        - require:
            - pkg: nodejs

bower:
    npm:
        - installed

        - require:
            - pkg: npm

less:
    npm:
        - installed

        - require:
            - pkg: npm
            
yuglify:
    npm:
        - installed

        - require:
            - pkg: npm

# ssh config needs the tc-deploy key to pull private repos
/home/vagrant/.ssh/config:
    file:
        - managed

        - user: vagrant
        - group: vagrant
        - mode: 0600
        - source: salt://app/files/config

/home/vagrant/.ssh/tc-deploy:
    file:
        - managed

        - user: vagrant
        - group: vagrant
        - mode: 0600
        - source: salt://app/files/tc-deploy

/home/vagrant/.ssh/tc-deploy.pub:
    file:
        - managed

        - user: vagrant
        - group: vagrant
        - mode: 0600
        - source: salt://app/files/tc-deploy.pub

/home/vagrant/.virtualenvs/app:
    virtualenv:
        - managed

        - user: vagrant
        - requirements: /vagrant/requirements.txt

        - require:
            - pip: virtualenv
            - pkg: libpq-dev
            - file: /home/vagrant/.ssh/config
            - file: /home/vagrant/.ssh/tc-deploy
            - file: /home/vagrant/.ssh/tc-deploy.pub

/home/vagrant/.virtualenvs/app/.project:
    file:
        - managed

        - user: vagrant
        - group: vagrant
        - mode: 0644
        - source: salt://app/files/project

        - require:
            - virtualenv: /home/vagrant/.virtualenvs/app

/home/vagrant/.virtualenvs/app/bin/postactivate:
    file:
        - managed

        - user: vagrant
        - group: vagrant
        - mode: 0755
        - source: salt://app/files/postactivate

        - require:
            - virtualenv: /home/vagrant/.virtualenvs/app

django_db_user:
    postgres_user:
        - present

        - name: django
        - password: django
        - runas: postgres
        - createdb: True

        - watch:
            - pkg: postgresql

django_db:
    postgres_database:
        - present

        - name: django
        - owner: django
        - runas: postgres

        - require:
            - postgres_user: django
