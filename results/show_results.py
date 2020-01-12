import flask
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    firstname = Col('firstname')
    surname = Col('surname')
    group = Col('group')
    tests_percentage = Col('tests_percentage')

# Get some objects
class Item(object):
    def __init__(self, firstname, surname, group, tests_percentage):
        self.firstname = firstname
        self.surname = surname
        self.group = group
        self.tests_percentage = tests_percentage

# Or, equivalently, some dicts
items = [dict(firstname='firstname1', surname='surname2', group='group1', tests_percentage='75'),
        dict(firstname='firstname2', surname='surname2', group='group2', tests_percentage='33'),
        dict(firstname='firstname3', surname='surname3', group='group3', tests_percentage='21')
         ]

# Or, more likely, load items from your database with something like
# items = ItemModel.query.all()

# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template