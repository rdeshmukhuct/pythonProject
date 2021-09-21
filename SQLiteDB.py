import sqlite3 as lite
import sys


# values = article_analysis.GUIFunctions()
# urls, result = values.search_articles()

# Create the initial connection
print("The connection is made")
conn = lite.connect('UCTT.db')
c = conn.cursor()



class SQLDb:

    def create_table_articles(self):
        print("table created")
        c.execute("""DROP TABLE IF EXISTS articles""")
        print("Table dropped")
        #
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
        print("Table created")



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
            except:
                pass

    def create_table_positive_texts(self):
        print("table created positive")
        c.execute("""DROP TABLE IF EXISTS positive_texts""")
        print("Table dropped")
        #
        c.execute("""CREATE TABLE positive_texts (
                     positive text
          )""")
        print("Table created")

    def insert_data_positive(self,positive_list):
        self.create_table_positive_texts()
        print("data inserted")


        for item in positive_list:
            try:
                print("+ve")
                c.execute("INSERT INTO positive_texts(positive) VALUES(?)", (item,))
            except:
                print("failed +ve")
                pass

    def create_table_negative_texts(self):
        print("table created negative")
        c.execute("""DROP TABLE IF EXISTS negative_texts""")
        print("Table dropped")
        #
        c.execute("""CREATE TABLE negative_texts (
                     negative text
          )""")
        print("Table created")

    def insert_data_negative(self, negative_list):
        self.create_table_negative_texts()
        print("data inserted")

        for item in negative_list:

            try:
                print("inert negative")
                c.execute("INSERT INTO negative_texts(negative) VALUES(?)", (item,))
            except:
                print("failed")
                pass

    def create_table_neutral_texts(self):
        print("table created neutral")
        c.execute("""DROP TABLE IF EXISTS neutral_texts""")
        print("Table dropped")
        #
        c.execute("""CREATE TABLE neutral_texts (
                     neutral text
          )""")
        print("Table created")

    def insert_data_neutral(self, neutral_list):
        self.create_table_neutral_texts()
        print("data inserted")

        for item in neutral_list:
            try:
                print("Neutral inserted")
                c.execute("INSERT INTO neutral_texts(neutral) VALUES(?)", (item,))
            except:
                print("failed neutral")
                pass




    def get_data(self):
        print("data retrieved")
        c.execute("SELECT * FROM positive_texts ")
        rows = c.fetchall()

        for row in rows:
            print(row)
        print(len(rows))    # this will give number of occurances

    def close(self):
        conn.commit()
        conn.close()




