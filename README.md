# cs162_database

GitHub: https://github.com/mariaeduardatc/cs162_database

### Project Structure
`/databases` contains the DB models
`/faker_data` contains the scripts for inserting faker data into the DBs
`create.py` initializes the DB and its tables
`extensions.py` contains the extensions used on the code (such as session)
`insert_data` contains the calls for inserting fake data into the tables
`queries.py` contain the queries for the assignment
`query_data` runs the queries



These are the recommended commands for macOS:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create_data.py
python3 insert_data.py
python3 query_data.py
```

To run the test, do:
```
python3 -m unittest discover tests
```


### Usage of AI tools
I used ChatGPT to help me understand errors and debug the code.

### HC Appendix
"#variables": When I was building my database tables in SQLAlchemy, it was crucial to take into account the types of variables and their connections. I had to specify the data type for each column, such as integer, text, boolean, or date. Additionally, I had to consider the relationships between the variables to ensure that the database satisfied the second normal form and when writing foreign key relationships. The primary keys were designated as independent variables that all other variables in the same table depended on, while foreign keys represented dependencies across different tables.
