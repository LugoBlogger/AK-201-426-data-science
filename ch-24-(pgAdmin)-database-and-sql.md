
The following tutorial is copied from
- [(Codemy.com, 2020) - Intro To PostgreSQL Databases With PgAdmin For Beginners - Full Course](https://www.youtube.com/watch?v=Dd2ej-QKrWY)
- [(Web Dev Simplified, 2019) - Learn SQL In 60 Minutes](https://www.youtube.com/watch?v=p3qvj9hO_Bo)

In this tutorial we do not install PostgreSQL and pgAdmin separately, but we   
install them in one package

### Install PostgreSQL (+ pgAdmin)
1. Visit PostgreSQL Downloads: https://www.postgresql.org/download/
2. Select "Windows"
3. In "Interactive installer by EDB", click "Donwload the installer", and
   select the latest version 

4. Run the installation file: "postgresql-16.3-1-windows-x64.exe"
5. In the step "Select Components", unselect "Stack Builder"
6. Set password (for the purpose of this course, we use a simple password)  
   - Password: 12345
7. Remember the default port: 5432, and    
   Database Superuser: postgres


### Technical terms in database
A database is a collection of tables and with some additional functionality    
how to operate those tables.

Important term in a table of a database.
- record = row
- field = column
- serial = a sequence of number
- character varying = VARCHAR

### Preparing database
1. Open pgAdmin 4 
2. In "Browser" explorer, click "Servers" > "PostgreSQL" > "Databases" > "postgres".  
   If it asks a password, enter your password in the installation.

3. Create a database, by right clicking on "Databases" in the "Browser" explorer,
   and select "Create" > "Database..."

4. Set the "Database" field as the name of your database. In this example
   we set "myDB". After that, click "Save". And the new database with a name
   "myDB" will pop up in the "Browser" explorer alongside "postgres" database.
  
5. [Optional] Click "myDB" > "Schemas" > "Tables".

### pgAdmin settings
- To set the font size of Query Tool

### SQL commands
To enter query tool, right click on table name, and select "Query Tool".

To update the change, right click on "Schemas" or "Tables" and select    
"Refresh"

To run a single line, select the text and click "Execute Script" icon (play   
button) or press F5 key

1. Create, alter and delete table
   ```sql
   CREATE TABLE test (
     test_column INT
   );

   ALTER TABLE test
     ADD another_column VARCHAR(255);

   DROP TABLE test;
   ```


### Easter eggs: SQL in Excel
1. Run the following commands in terminal
   ```sh
   pip install xlwings
   xlwings addin install
   ```

2. See the example in `week-15-sql/bands-albums.xlsx` 
   and .gif demo in `week-15-sql/sql-in-excel-demo.gif` (adopted from [(GeeksforGeeks, 2023) - How to Use SQL Statements in MS Excel?](https://www.geeksforgeeks.org/how-to-use-sql-statements-in-ms-excel/))