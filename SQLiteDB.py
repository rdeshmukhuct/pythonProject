import sqlite3 as lite
import sys

# values = article_analysis.GUIFunctions()
# urls, result = values.search_articles()

# Create the initial connection
# import SQLiteDB

print("The connection is made")
conn = lite.connect('UCTT.db')
c = conn.cursor()


class SQLDb:

    @classmethod
    def create_table_articles(cls):
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
                c.execute("INSERT INTO articles VALUES (:title, :desc, :date, :datetime, :link, :img, :media, :site)",
                          item)
            except Exception as e:
                print("Exception: ", e)

    @classmethod
    def create_table_positive_texts(cls):
        # print("table created positive")
        c.execute("""DROP TABLE IF EXISTS positive_texts""")
        # print("Table dropped")
        #
        c.execute("""CREATE TABLE positive_texts (
                     positive text
          )""")
        # print("Table created")

    def insert_data_positive(self, positive_list):
        self.create_table_positive_texts()
        # print("data inserted")

        for item in positive_list:
            try:
                # print("+ve")
                c.execute("INSERT INTO positive_texts(positive) VALUES(?)", (item,))
            except Exception as e:
                print("failed +ve: ", e)

    @classmethod
    def create_table_negative_texts(cls):
        # print("table created negative")
        c.execute("""DROP TABLE IF EXISTS negative_texts""")
        # print("Table dropped")
        #
        c.execute("""CREATE TABLE negative_texts (
                     negative text
          )""")
        # print("Table created")

    def insert_data_negative(self, negative_list):
        self.create_table_negative_texts()
        # print("data inserted")

        for item in negative_list:

            try:
                # print("inert negative")
                c.execute("INSERT INTO negative_texts(negative) VALUES(?)", (item,))
            except Exception as e:
                print("failed: ", e)

    @classmethod
    def create_table_neutral_texts(cls):
        # print("table created neutral")
        c.execute("""DROP TABLE IF EXISTS neutral_texts""")
        # print("Table dropped")
        #
        c.execute("""CREATE TABLE neutral_texts (
                     neutral text
          )""")

    # print("Table created")

    def insert_data_neutral(self, neutral_list):
        self.create_table_neutral_texts()
        # print("data inserted")

        for item in neutral_list:
            try:
                # print("Neutral inserted")
                c.execute("INSERT INTO neutral_texts(neutral) VALUES(?)", (item,))
            except Exception as e:
                print("failed neutral: ", e)

    @classmethod
    def get_data(cls):

        listTitle = []

        # print("data retrieved")
        c.execute("SELECT * FROM articles  ")
        rows = c.fetchall()
        # print(rows)
        for row in rows:
            listTitle.append(row[2])  # GET ONLY THE TITLE OF THE ARTICLE FROM THE TABLE
        # print(len(rows))  # this will give number of occurrences
        return listTitle

    @classmethod
    def close(cls):
        conn.commit()
        conn.close()


# ob = SQLDb
#
# l = ob.get_data()
# # print(l.pop(0))
#
# count = 0
# count2 = 0
# for i in l:
#     if i is None:
#         l.pop(count)
#         print(i)
#     count += 1
# l.pop(-3)
#
# for i in l:
#     try:
#         if len(i) > 5:
#             l.pop(count2)
#         count2 += 1
#     except:
#         pass
#
# print(l)
#
# swap_time = {"Jan": "1/", "Feb": "2/", "Mar": "3/", "Apr": "4/", "May": "5/", "Jun": "6/", "Jul": "7/", "Aug": "8/", "Sep": "9/",
#              "Oct": "10/", "Nov": "11/", "Dec": "12/"}
#
# oldList = ['Aug 2', 'Apr 5', 'Sep 3', 'Aug 3', 'Apr 8', 'May 3', 'Mar 31', 'Dec 16', 'Aug 2', 'Feb 17', 'May 6',
#            'Mar 9']
# newList = []
#
# for index, data in enumerate(oldList):
#     for key, value in swap_time.items():
#         if key in data:
#             oldList[index] = data.replace(key, swap_time[key])
#
#
# print(oldList)
