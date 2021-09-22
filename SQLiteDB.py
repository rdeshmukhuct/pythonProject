import sqlite3 as lite
import sys


# Create the initial connection
print("The connection is made")
conn = lite.connect('UCTT.db')
c = conn.cursor()

class SQLDb:

    # Create a table that will store all the details of the articles like title, desc, links
    def create_table_articles(self):
        # We don't want our table to be added with the same data always so everytime we drop the table and
        # then create a new one
        c.execute("""DROP TABLE IF EXISTS articles""")

        c.execute("""CREATE TABLE articles (
                     title text,
                     desc text,
                     date text,
                     datetime text,
                     link text,
                     img text,
                     media text,
                     site text
          )""")
        print("Article Table created")


    # Insert all the data into our article table
    # article_sentiment will call this method and will pass in url(links)
    # and result is a dictionary which has all the details such as desc, title etc
    def insert_data_articles(self, result, url):
        self.create_table_articles()
        print("data inserted")
        counter = 0
        # url and links are same the only difference is https:/
        # so we just update the link with the url
        for item in result:
            item.update(link=url[counter])
            counter += 1

        for item in result:
            try:
                c.execute("INSERT INTO articles VALUES (:title, :desc, :date, :datetime, :link, :img, :media, :site)", item)
            except Exception as e:
                print(e)
                pass

    # This table is used to store all the positive sentences in our db
    def create_table_positive_texts(self):
        # We don't want our table to be added with the same data always so everytime we drop the table and
        # then create a new one
        c.execute("""DROP TABLE IF EXISTS positive_texts""")

        c.execute("""CREATE TABLE positive_texts (
                     positive text
          )""")
        print("Positive_texts table created")

    # Insert all the data into our positive_texts table
    # positive list contains all the positve sentences
    def insert_data_positive(self,positive_list):
        self.create_table_positive_texts()
        #print("data inserted")

        # Iterate through the positive list and keep adding each positive sentence to our table
        for item in positive_list:
            try:
                c.execute("INSERT INTO positive_texts(positive) VALUES(?)", (item,))
            except Exception as e:
                print(e)
                pass

    # This table is used to store all the negative sentences in our db
    def create_table_negative_texts(self):
        # We don't want our table to be added with the same data always so everytime we drop the table and
        # then create a new one
        c.execute("""DROP TABLE IF EXISTS negative_texts""")

        c.execute("""CREATE TABLE negative_texts (
                     negative text
          )""")
        print("Negative_texts table created")

    # Insert all the data into our negative_texts table
    # negative list contains all the negative sentences
    def insert_data_negative(self, negative_list):
        self.create_table_negative_texts()

        # Iterate through the negative list and keep adding each negative sentence to our table
        for item in negative_list:

            try:
                c.execute("INSERT INTO negative_texts(negative) VALUES(?)", (item,))
            except Exception as e:
                print(e)
                pass

    # This table is used to store all the neutral sentences in our db
    def create_table_neutral_texts(self):
        # We don't want our table to be added with the same data always so everytime we drop the table and
        # then create a new one
        c.execute("""DROP TABLE IF EXISTS neutral_texts""")

        c.execute("""CREATE TABLE neutral_texts (
                     neutral text
          )""")
        print("Neurtal_texts table created")

    # Insert all the data into our neutral_texts table
    # neutral list contains all the neutral sentences
    def insert_data_neutral(self, neutral_list):
        self.create_table_neutral_texts()

        # Iterate through the neutral list and keep adding each negative sentence to our table
        for item in neutral_list:
            try:
                #print("Neutral inserted")
                c.execute("INSERT INTO neutral_texts(neutral) VALUES(?)", (item,))
            except Exception as e:
                print(e)
                pass



    # Testing method just to see if everything is being added to the db properly.
    def get_data(self):
        print("data retrieved")
        c.execute("SELECT * FROM positive_texts ")
        rows = c.fetchall()

        for row in rows:
            print(row)
        print(len(rows))    # this will give number of occurances

    # Commit all the queries and close the connection
    def close(self):
        conn.commit()
        conn.close()




