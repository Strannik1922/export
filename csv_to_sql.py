import pandas as pd
from sqlalchemy import create_engine # create an in-memory SQL database


class CSVtoSQL:
    def __init__(self):
        pass

    def makeFileIntoSQL(self, filename, sqlName, sqlEngine):
        chunksize = 20000
        j = 0
        index_start = 1
        for df in pd.read_csv(filename, chunksize=chunksize, iterator=True, encoding='utf-8'):
            df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
            df.index += index_start
            df.to_sql(sqlName, sqlEngine, if_exists='append') #change to if_exists='replace' if you don't want to replace the database file
            index_start = df.index[-1] + 1


if __name__ == "__main__":
    #Create sqlite engine
    disk_engine = create_engine('sqlite:///awesome.db')

    #Start class
    cs = CSVtoSQL()

    #Converting files into SQL tables
    cs.makeFileIntoSQL('first_table.csv', 'firstdata', disk_engine)
    cs.makeFileIntoSQL('second_table.csv', 'secondata', disk_engine)

    #Examples of SQL queries
    df = pd.read_sql_query('SELECT * FROM firstdata', disk_engine)
    print ("This is data from first_table.csv")
    print (df)
    print ("")

    df_second = pd.read_sql_query('SELECT * FROM secondata', disk_engine)
    print ("This is data from second_table.csv")
    print (df_second)
    print ("")
