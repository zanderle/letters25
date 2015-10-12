# Letters to My 25-Year-Old Self Website

This is a Django powered website for the Letters project. A collection of letters filled with the dreams, fears, and 
revelations of incredible people around the world. A project that asks the question
> "If you could tell your 25-year-old self anything at all, what would you say?"

## Setting up the site locally

Start by cloning the git project

```bash
$ git clone git@github.com:zanderle/letters25.git
```

Before installing the requirements, make sure you have Python libq header files installed (we will need it for
Pillow and psycopg2) and install bower.

```bash
$ apt-get install python-dev libpq-dev
$ npm install -g bower
```

After that install the requirements (preferably in [virtual enviornment](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
and the frontend packages.

```bash
$ pip install -r requirements.txt
$ bower install
```

Create `local_settings.py` in the same directory as `settings.py`. Use `local_settings.py.example` to do it. You will 
need to compile the less files that `PIPELINE_CSS` expects. The easiest way to do this depends on what tools you use. 
If you are going to edit the stylesheets, you should have it set to recompile automatically.


Now, you only need to create and migrate the database (you should use PostgreSQL, but you could probably get away with 
SQLite), and you're ready to get started

```bash
$ ./manage.py migrate
$ ./manage.py runserver
```
