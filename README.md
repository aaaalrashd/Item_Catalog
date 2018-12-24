# Item-catalog-project
Item catalog website enable to CRUD with oauth Google login.

## Setup:

* Clone or [download](https://github.com/aaaalrashd/Item_Catalog) the repo: `https://github.com/aaaalrashd/Item_Catalog.git`
* you must have vagrant and virtual machine.
* Install (if necessary): 
  * [Flask](http://flask.pocoo.org/docs/0.11/installation/)
  * [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/intro.html)

## Testing:

1. Open terminal to folder location of cloned repo into vagrant file.
2. write vagrant up.
3. write vagrant ssh.
4. write database_setup.py: `python database_setup.py`
5. write databaseOfFilms.py: `python databaseOfFilms.py`
6. write films.py to start web app: `python films.py` into localhost:5000
