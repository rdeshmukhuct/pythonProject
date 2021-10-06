import sqlite3 as lite
from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as lite
conn = lite.connect('Month.db')
c = conn.cursor()



class SQLDbModified:
    @classmethod
    def create_january_description(cls):
        c.execute("""DROP TABLE IF EXISTS january_description""")
        c.execute("""CREATE TABLE january_description (
                                         title text,
                                         datetime text,
                                         link text,
                                         positive INTEGER,
                                         negative INTEGER,
                                         polarity Integer
                              )""")
        print("Table created")

    @classmethod
    def create_january_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS january_sentiments""")
        c.execute("""CREATE TABLE january_sentiments (
                                         title text,
                                         datetime text,
                                         positive text,
                                         negative text
                              )""")
        print("Table created")

    @classmethod
    def insert_january_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                                        INSERT INTO 
                                            january_sentiments 
                                        VALUES 
                                            (?, ?, ?,?)
                                    """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_january_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                                    INSERT INTO 
                                        january_description 
                                    VALUES 
                                        (?, ?, ?,?,?,?)
                                """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_january_description(cls):

        c.execute("SELECT * FROM january_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_january_sentiments(cls):
        c.execute("SELECT * FROM january_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

    ###################################################################################################
    @classmethod
    def create_feb_description(cls):
        c.execute("""DROP TABLE IF EXISTS feb_description""")
        c.execute("""CREATE TABLE feb_description (
                                      title text,
                                      datetime text,
                                      link text,
                                      positive INTEGER,
                                      negative INTEGER,
                                      polarity Integer
                           )""")
        print("Table created")

    @classmethod
    def create_feb_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS feb_sentiments""")
        c.execute("""CREATE TABLE feb_sentiments (
                                      title text,
                                      datetime text,
                                      positive text,
                                      negative text
                           )""")
        print("Table created")

    @classmethod
    def insert_feb_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                                     INSERT INTO 
                                         feb_sentiments 
                                     VALUES 
                                         (?, ?, ?,?)
                                 """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_feb_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                                 INSERT INTO 
                                     feb_description 
                                 VALUES 
                                     (?, ?, ?,?,?,?)
                             """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_feb_description(cls):

        c.execute("SELECT * FROM feb_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_feb_sentiments(cls):
        c.execute("SELECT * FROM feb_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

    ###########################################################################################################
    @classmethod
    def create_march_description(cls):
        c.execute("""DROP TABLE IF EXISTS march_description""")
        c.execute("""CREATE TABLE march_description (
                                  title text,
                                  datetime text,
                                  link text,
                                  positive INTEGER,
                                  negative INTEGER,
                                  polarity Integer
                       )""")
        print("Table created")

    @classmethod
    def create_march_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS march_sentiments""")
        c.execute("""CREATE TABLE march_sentiments (
                                  title text,
                                  datetime text,
                                  positive text,
                                  negative text
                       )""")
        print("Table created")

    @classmethod
    def insert_march_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                                 INSERT INTO 
                                     march_sentiments 
                                 VALUES 
                                     (?, ?, ?,?)
                             """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_march_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                             INSERT INTO 
                                 march_description 
                             VALUES 
                                 (?, ?, ?,?,?,?)
                         """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_march_description(cls):

        c.execute("SELECT * FROM march_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_march_sentiments(cls):
        c.execute("SELECT * FROM march_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

    ###########################################################################################################
    @classmethod
    def create_april_description(cls):
        c.execute("""DROP TABLE IF EXISTS april_description""")
        c.execute("""CREATE TABLE april_description (
                               title text,
                               datetime text,
                               link text,
                               positive INTEGER,
                               negative INTEGER,
                               polarity Integer
                    )""")
        print("Table created")

    @classmethod
    def create_april_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS april_sentiments""")
        c.execute("""CREATE TABLE april_sentiments (
                               title text,
                               datetime text,
                               positive text,
                               negative text
                    )""")
        print("Table created")

    @classmethod
    def insert_april_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                              INSERT INTO 
                                  april_sentiments 
                              VALUES 
                                  (?, ?, ?,?)
                          """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_april_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                          INSERT INTO 
                              april_description 
                          VALUES 
                              (?, ?, ?,?,?,?)
                      """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_april_description(cls):

        c.execute("SELECT * FROM april_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_april_sentiments(cls):
        c.execute("SELECT * FROM april_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

    #########################################################################################################
    @classmethod
    def create_may_description(cls):
        c.execute("""DROP TABLE IF EXISTS may_description""")
        c.execute("""CREATE TABLE may_description (
                                  title text,
                                  datetime text,
                                  link text,
                                  positive INTEGER,
                                  negative INTEGER,
                                  polarity Integer
                       )""")
        print("Table created")

    @classmethod
    def create_may_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS may_sentiments""")
        c.execute("""CREATE TABLE may_sentiments (
                                  title text,
                                  datetime text,
                                  positive text,
                                  negative text
                       )""")
        print("Table created")

    @classmethod
    def insert_may_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                                 INSERT INTO 
                                    may_sentiments 
                                 VALUES 
                                     (?, ?, ?,?)
                             """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_may_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                             INSERT INTO 
                                 may_description 
                             VALUES 
                                 (?, ?, ?,?,?,?)
                         """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_may_description(cls):

        c.execute("SELECT * FROM may_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_may_sentiments(cls):
        c.execute("SELECT * FROM may_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

    ###########################################################################################################

    @classmethod
    def create_june_description(cls):
        c.execute("""DROP TABLE IF EXISTS june_description""")
        c.execute("""CREATE TABLE june_description (
                              title text,
                              datetime text,
                              link text,
                              positive INTEGER,
                              negative INTEGER,
                              polarity Integer
                   )""")
        print("Table created")

    @classmethod
    def create_june_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS june_sentiments""")
        c.execute("""CREATE TABLE june_sentiments (
                              title text,
                              datetime text,
                              positive text,
                              negative text
                   )""")
        print("Table created")

    @classmethod
    def insert_june_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                             INSERT INTO 
                                 june_sentiments 
                             VALUES 
                                 (?, ?, ?,?)
                         """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_june_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                         INSERT INTO 
                             june_description 
                         VALUES 
                             (?, ?, ?,?,?,?)
                     """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_june_description(cls):

        c.execute("SELECT * FROM june_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_june_sentiments(cls):
        c.execute("SELECT * FROM june_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])
###########################################################################################################
    @classmethod
    def create_july_description(cls):
        c.execute("""DROP TABLE IF EXISTS july_description""")
        c.execute("""CREATE TABLE july_description (
                           title text,
                           datetime text,
                           link text,
                           positive INTEGER,
                           negative INTEGER,
                           polarity Integer
                )""")
        print("Table created")


    @classmethod
    def create_july_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS july_sentiments""")
        c.execute("""CREATE TABLE july_sentiments (
                           title text,
                           datetime text,
                           positive text,
                           negative text
                )""")
        print("Table created")


    @classmethod
    def insert_july_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                          INSERT INTO 
                              july_sentiments 
                          VALUES 
                              (?, ?, ?,?)
                      """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()


    @classmethod
    def insert_july_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                      INSERT INTO 
                          july_description 
                      VALUES 
                          (?, ?, ?,?,?,?)
                  """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()


    @classmethod
    def get_july_description(cls):

        c.execute("SELECT * FROM july_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))


    @classmethod
    def get_july_sentiments(cls):
        c.execute("SELECT * FROM july_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

#################################################################################################################
    @classmethod
    def create_august_description(cls):
        print("table for month of september  created")
        c.execute("""DROP TABLE IF EXISTS august_description""")
        c.execute("""CREATE TABLE august_description (
                        title text,
                        datetime text,
                        link text,
                        positive INTEGER,
                        negative INTEGER,
                        polarity Integer
             )""")
        print("Table created")

    @classmethod
    def create_august_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS august_sentiments""")
        c.execute("""CREATE TABLE august_sentiments (
                        title text,
                        datetime text,
                        positive text,
                        negative text
             )""")
        print("Table created")

    @classmethod
    def insert_august_sentiments(self, title, date, positive, negative):
        try:
            c.execute("""
                       INSERT INTO 
                           august_sentiments 
                       VALUES 
                           (?, ?, ?,?)
                   """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_august_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                   INSERT INTO 
                       august_description 
                   VALUES 
                       (?, ?, ?,?,?,?)
               """, (title, date, link, positive, negative, polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_august_description(cls):
        c.execute("SELECT * FROM august_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_august_sentiments(cls):
        c.execute("SELECT * FROM august_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])
###############################################################################################################
    @classmethod
    def create_september_description(cls):
        print("table for month of september  created")
        c.execute("""DROP TABLE IF EXISTS september_description""")
        c.execute("""CREATE TABLE september_description (
                     title text,
                     datetime text,
                     link text,
                     positive INTEGER,
                     negative INTEGER,
                     polarity Integer
          )""")
        print("Table created")
    @classmethod
    def create_september_sentiments(cls):
        c.execute("""DROP TABLE IF EXISTS september_sentiments""")
        c.execute("""CREATE TABLE september_sentiments (
                     title text,
                     datetime text,
                     positive text,
                     negative text
          )""")
        print("Table created")

    @classmethod
    def insert_september_sentiments(self, title, date ,positive, negative):
        try:
            c.execute("""
                    INSERT INTO 
                        september_sentiments 
                    VALUES 
                        (?, ?, ?,?)
                """, (title, date, positive, negative))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_september_description(self, title, date, link, positive, negative, polarity):
        try:
            c.execute("""
                INSERT INTO 
                    september_description 
                VALUES 
                    (?, ?, ?,?,?,?)
            """, (title, date, link, positive, negative,polarity))

            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_september_description(cls):
        c.execute("SELECT * FROM september_description  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
                + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_september_sentiments(cls):
        c.execute("SELECT * FROM september_sentiments  ")
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])


    # This method plots the bar graph of a combined year of all the positive and the negative senetences in percentage
    @classmethod
    def combinedBarGraph(cls):
        negative = list()
        positive = list()

        for x in range(9):

            if x == 0:
                month = 'january_description'
            elif x == 1:
                month = 'feb_description'
            elif x == 2:
                month = 'march_description'
            elif x == 3:
                month = 'april_description'
            elif x == 4:
                month = 'may_description'
            elif x == 5:
                month = 'june_description'
            elif x == 6:
                month = 'july_description'
            elif x == 7:
                month = 'august_description'
            elif x == 8:
                month = 'september_description'


            c.execute("SELECT SUM(positive), SUM(negative) FROM '%s' " %month)
            rows = c.fetchall()
            for row in rows:
                # These steps are done for scaling purposes, in terms of percentage, how many are +ve and how many are -ve
                total = row[0] + row[1]
                pos_scale = int((row[0]/total) * 100)
                neg_scale = int((row[1]/total) * 100)
                positive.append(pos_scale)
                negative.append(neg_scale)

        print(positive)
        print(negative)

        X = ['January','February','March','April','May','June','July', 'August','September']


        X_axis = np.arange(len(X))

        plt.bar(X_axis - 0.2, positive, 0.4, label = 'positive')
        plt.bar(X_axis + 0.2, negative, 0.4, label = 'negative')

        plt.xticks(X_axis, X)
        plt.xticks(rotation=20)
        plt.xlabel("Months")
        plt.ylabel("Sentiments (in %)")
        plt.title("Sentiment Analysis of Year 2021")
        for i in range(len(X)):
                plt.text(i, positive[i], positive[i], ha = 'right', color = 'black')
                plt.text(i, negative[i], negative[i], ha = 'left', color = 'black')

        plt.legend()
        plt.show()

    # This method plots a bar graph of the positive and the negative senetnces of all the articles of a month
    @classmethod
    def individualBarGraph(cls,month):

            # Get the sum of all the positive articles and negative articles
            c.execute("SELECT SUM(positive), SUM(negative) FROM '%s' " %month)
            rows = c.fetchall()
            values = list()

            for row in rows:
                values.append(row[0])
                values.append(row[1])

            print(values)
            # Plotting the bar graph
            month = month.replace('_description','')
            X = [month]
            type_of_sentiment = ['Positive', 'Negative']
            data = values
            rects = plt.bar(type_of_sentiment, data, color = ['lightgreen','coral'])
            plt.title("Bar graph for Sentiment Article %s " %month)

            for rect, label in zip(rects, data):
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')
            plt.show()

    # This method gives us the titles of all the articles for a particular month
    @classmethod
    def getArticlesForMonth(cls,month):
        c.execute("SELECT title FROM '%s' " %month)
        rows = c.fetchall()
        titles = list()

        for row in rows:
            titles.append(row[0])

        return titles

    def articleBarGraph(cls, title, month):
        c.execute("SELECT positive, negative FROM %s WHERE title = (?)" %month,(title,))

        rows = c.fetchall()
        values = list()

        for row in rows:
            values.append(row[0])
            values.append(row[1])

            print(values)
            # Plotting the bar graph
            month = month.replace('_description','')
            X = [month]
            type_of_sentiment = ['Positive', 'Negative']
            data = values
            rects = plt.bar(type_of_sentiment, data, color = ['lightgreen','coral'])
            plt.title("%s " %title)

            for rect, label in zip(rects, data):
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')
            plt.show()

    @classmethod
    def getPositiveSentences(cls, title, month):
        c.execute("SELECT positive FROM %s WHERE title = (?)" %month,(title,))
        rows = c.fetchall()

        for row in rows:
            result = row[0]
        return result

    @classmethod
    def getNegativeSentences(cls, title, month):
        c.execute("SELECT negative FROM %s WHERE title = (?)" %month,(title,))
        rows = c.fetchall()

        for row in rows:
            result = row[0]
        return result


    @classmethod
    def close(cls):
        conn.commit()
        conn.close()