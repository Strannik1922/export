# export
How to Extract Tables from PDF using Python

## Converting csv files to SQL using Python demo project

### Using Pandas

This is a simple project to demonstrate the use of Python Anaconda or Pandas for parsing or extracting csv files and converting it into SQL language.

### Getting started

```bash
git clone git@github.com:Strannik1922/Posts.git
```

```bash
cd Posts/
python -m pip install --upgrade pip
python -m venv venv
source venv/Scripts/activate
```

```bash
cd Posts/
pip install -r requirements.txt
```

### Some details for the script in main.py

Get tabula-py. If you don’t have it already, install Java. There are several possible reasons, but tabula-py is just a wrapper of [tabula-java](https://github.com/tabulapdf/tabula-java), make sure you’ve installed Java, and you can use java command on your terminal. Many issue reporters forget to set PATH for java command.

You can use options argument as follows. The format is the same as CLI of tabula-java. You can import public interfaces such as read_pdf() or convert_into().

`Example` read_pdf(file_path, options="--columns 10.1,20.2,30.3")

`function` tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')

To save our df as a CSV file.

`function` df.to_csv(path_or_buf="my_data")

### Some details for the script in csv_to_sql.py

`function`: makeFileIntoSQL(file, nameoftable, sqlengine)

`Usage`   : converts csv files into SQL files

`Example` : makeFileIntoSQL('first_table.csv', 'firstdata', disk_engine) 

``##  augdata is the name of the table in the SQL, you can rename this to whatever you like. This would affect the SQL queries.``

**From pandas library**

`function`: pandas.read_sql_query('SELECT * FROM firstdata', create_engine('sqlite:///name.db'))

`Usage`   : make SQL query and save the results into a variable

`Example` : df = pd.read_sql_query('SELECT * FROM firstdata', disk_engine)
