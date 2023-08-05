# SQLiteHandler
## Overview
The purpose of this library is to use an SQLite3 database without needing to know SQL. It offers the following functions, listed below:
- Existence
- Create
- RunCommand
- Connect
- CreateTable
- add
- readAll
- ColumnNames
- columnsDistinct
- find

## Descriptions 
### Class Description
The class has two optional arguments and three Class variables. The Arguments are described below. The three variables are as follow:

* defaultDBName ("database.db") : Name of the database used when a database name is not passed to other methods;
* dbPath (""): Path to folder/directory that the database is/will be created in;
* defaultTable ("Material"): Name for the table in the database table is not passed to other methods;

### Class Methods
```python
__init__(self, db_loc='', name='database.db')
```

Class initialization, ```db_loc``` is the path the database will be accessed or created. **It will automatically create a database in this folder**. The argument name is the name of the created database.

#### Connect
```python
def Connect(self, command, *args, save=False, **kwargs)
```

All methods are passed through this function. It handles opening and closing the database, as well as returning any output the passed argument might have. The ````*args```` and ````**kwargs```` are passed through to the selected function (command argument).

        :param command: function
        :param args: passed function's arguments
        :param save: saves alterations made to database
        :param kwargs: passed function's keyword arguments
        :return: passed functions return or Error String

        example:
        Connect(self.RunCommand, ```SQL_command_string```, save=True)
       
#### RunCommand
```python
@staticmethod
    def RunCommand(c, inputs, *args)
```

Like most function this method should be run trough the Connect method. It is the basic method that executes any _SQL_ command.

        :param c: SQLite curser
        :param inputs: SQL command
        :return: bool, depending if error found

#### Existence        
```python
def Existence(self, path=None)
```

Checks the existence of a SQL database at path/directory. If a path is not set it will default to class variable dbPath.

        :param path: (str) path to check for sqlite3 databases
        :return: (list(str)) or None if path is invalid

#### Create        
```python
def Create(self, path='', name=None)
```

Connects to a database in path, default is active file, named database.db. If Database does not exist it will be created.

        :param path: (str) database folder's path, must be set according to OS
        :param name: (str) database name
        :return: True if database connection is valid
                    str if database connection Failed

#### CreateTable
```python
def CreateTable(self, c, table=None, cols=None, types=None, adds=None)
```

Creates and sets up a table.

        :param c: SQLite curser
        :param table: (str) Name for the table
        :param cols: list(str) for name of columns
        :param types: list(str) informs SQL data type for columns
        :param adds: additional parameters

        example:
```python
        print(db.Connect(db.CreateTable, "Material",
                   ["id", 'hyperlink', 'level', 'subject'],
                   ["integer", 'text', 'text', 'text'],
                   ["NOT NULL"]))
```

#### add
```python
add(self, table=None, data=None)
```

Adds a row of data to database. All data must be in a dictionary. If table is not passed it will default to class variable defaultTable.

        :param table: (str) name of table
        :param data: (dict) dictionary with column_name : value
        :return: bool or error string

        example:
```python
        db.add("Material", {"id": 2,
                              "hyperlink": "www.google.com",
                              "level": "C2",
                              "subject": "simple Present"})
```

#### readAll
```python
readAll(self, table=None, limit=None, offset=None)
```

Reads All data from a table. **Caution** this command calls the method Connect which uses fetchall from the sqlite library so a limit might be needed depending on the application.
If table, limit and offset are not set when calling this method they will default to class variable defaultTable, no limit, no offset.

	:param table: (str) table name
        :param limit: (int) limits the number of results
        :param offset: (int) offsets the position sql starts listing
        :return: tuple of row in table

        example:
```python
 print(db.readAll("Material"))
```

#### columnNames
```python
columnNames(self, table=None)
```

Gets the name for each column in table
        :param table: (str) table name
        :return: list(str)

        example:
```python
        print(db.columnNames())
```

#### columnsDistinct
```python
columnsDistinct(self, col="", table=None)
```

Gets all distinct values within a single column, *id est* the values do not repeat.
        :param col: (str) column name
        :param table: (str) table name
        :return: tuple of (str)

        example:
```python
        db.columnsDistinct("Material", "id")
```

#### find
```python
find(self, values=None, table=None, selection='*', 
     operation='AND', limit=None, offset=None, count=False)
```

Find rows with multiple values and or columns. When count is true the function only returns the number of columns that satisfied the search and **not** the rows themselves.

        :param values: Dict{column: list(Values)}
        :param table: (str) table in SQL database
        :param operation: (str) SQL operation (AND, OR, ...) for columns
        :param selection: (str) SQL select statement
        :param limit: (int) limits the number of results
        :param offset: (int) offsets the position sql starts listing
        :param count: (bool) set command to count row count according to other inputs

        Example:
```python
        db.find(values={'Column_1': [1, 2, 3], 'Column_2': ["C2"]})
```
        SQLite command generated by this command is:
```sql
        SELECT * FROM TABLE_NAME WHERE Column_1 IN (?, ?, ?) AND Column_2 IN (?)
```
  
# Example
```python
from sqlitehandler import DatabaseSQLite

# this command will automatically try to connect to a SQL database.
# should it fail to connect it will create one with the default values
# in the folder containing the script.

db = DatabaseSQLite()

print(db.Existence(), "this should be a list containing one element called 'database.db'")

print("Now lets add a table and columns to it as well")
db.Connect(db.CreateTable, "Material",
                   ["id", 'hyperlink', 'level', 'subject'],
                   ["integer", 'text', 'text', 'text'],
                   ["NOT NULL"])

print(db.columnNames(), "\nthis should be the same list as shown above in the example code.")

print("\n\nNow lets generate some random entries to fill out the database")
from random import  randint, sample
a = ["simple present", "Present Continuous", "Simple Past", "Past Continuous", "Present Perfect",
       "Present Perfect Continuous", "Simple Future"]
for i in range(1):
    j = db.add("Material", {"id": i,
                        "hyperlink": "www.google.com",
                        'level': f'{sample(["A", "B", "C"],1)[0]}{randint(1,2)}',
                        "subject": f"{sample(a, 1)[0]}"})

print("now lets get the distinct values in the column 'level'")
print(db.columnsDistinct(col="level", table=None), "this results in a mix of A,B,C and 1,2.")

print("Now lets get the first ten rows in our database")
results = db.readAll("Material", limit=10)
for index, result in enumerate(results):
    print(f"{index}. {result}")


print("\n\nNow lets get ten rows in our database skipping the first 10")
results = db.readAll("Material", limit=10, offset=10)
for index, result in enumerate(results):
    print(f"{index}. {result}")

print("\n\nNow lets get do a parametric search on out database")

print("first lets count how many results we will get")
print(f"we have {db.find(values={'level': ['A1', 'A2'], 'subject': ['Simple Past']}, count=True)} entries")

results = db.find(values={'level': ["A1", "A2"], 'subject': ['Simple Past']})
for index, result in enumerate(results):
    print(f"{index}. {result}")
```
