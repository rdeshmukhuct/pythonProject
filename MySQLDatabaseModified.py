import sqlite3 as lite
from calendar import month

from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as lite
import mysql.connector

conn = mysql.connector.connect(user='Admin', password='UCT123@!',
                              host='10.0.0.185',
                              database='uctt')
c = conn.cursor()



class MySQLDbModified:

    # Done
    @classmethod
    def create_month_description(cls, month_sentiment):
        try:
            sql = "CREATE TABLE " + month_sentiment + """ (
               title VARCHAR(300),
               datetime VARCHAR(100),
               link MEDIUMTEXT,
               positive INT,
               negative INT,
               polarity FLOAT
            )"""
            c.execute(sql)
            print(sql)
        except Exception as e:
            print(e);


    # Done
    @classmethod
    def create_month_sentiments(cls, month_sentiment):
        print("The month sentiment is ", month_sentiment)
        try:
            sql = "CREATE TABLE " + month_sentiment + """ (
                           title VARCHAR(300),
                           datetime VARCHAR(100),
                           positive LONGTEXT,
                           negative LONGTEXT
                        )"""
            c.execute(sql)
            print(sql)
            print("Table created")
        except Exception as e:
            print(e)

    @classmethod
    def insert_month_sentiments(self, month_sentiment, title, date, positive, negative):
        print("Sentiment", month_sentiment)
        try:
           print(title)
           values = (title,date,positive,negative)
           mySql_insert_query = "INSERT INTO " + month_sentiment + """ (title, datetime, positive, negative) 
                                          VALUES (%s, %s, %s, %s) """

           c.execute(mySql_insert_query, values)
           print(mySql_insert_query)

        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_month_description(self, month_sentiment, title, date, link, positive, negative, polarity):
        print("description" , month_sentiment)
        try:
            values = (title, date, link, positive, negative, polarity)
            mySql_insert_query = "INSERT INTO " + month_sentiment + """ (title, datetime, link ,positive, negative, polarity) 
                                                     VALUES (%s, %s, %s, %s, %s, %s) """

            c.execute(mySql_insert_query, values)
            print(mySql_insert_query)
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

        # Done

    @classmethod
    def create_description(cls):
        try:
            print("Here is create")
            sql = "CREATE TABLE combined (title VARCHAR(300),datetime DATE,link MEDIUMTEXT," \
                  "positive INT,negative INT,polarity FLOAT) "
            c.execute(sql)
        except Exception as e:
            print(e);

    @classmethod
    def insert_description(self, title, date, link, positive, negative, polarity):
        try:
            print("Trying the insert")
            values = (title, date, link, positive, negative, polarity)
            mySql_insert_query = "INSERT INTO combined (title, datetime, link ,positive, negative, polarity) VALUES (%s, %s, %s, %s, %s, %s) "

            c.execute(mySql_insert_query, values)
            print(mySql_insert_query)
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_month_description(cls, month_sentiment):
        print("Hello from get_month_description")
        value_pass = "SELECT * FROM " + month_sentiment
        c.execute(value_pass)
        rows = c.fetchall()
        print(len(rows))


        for row in rows:
            print("Title:" + row[0])
            # "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
            # + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_month_sentiments(cls, month_sentiment):
        print("Hello from get_month_sentiment")
        value_pass = "SELECT * FROM " + month_sentiment
        c.execute(value_pass)
        rows = c.fetchall()
        print(len(rows))

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1]  +" \t Positive:" + row[2]+ " \t Negative:" + row[3])

    @classmethod
    def getPositiveSentences(cls, title, month):

        mySql_query = "SELECT positive FROM " + month + " WHERE title = %s "
        c.execute(mySql_query, (title,))

        rows = c.fetchall()

        for row in rows:
            result = row[0]
            print(result)
        return result

    @classmethod
    def getNegativeSentences(cls, title, month):
        mySql_query = "SELECT negative FROM " + month + " WHERE title = %s "
        c.execute(mySql_query, (title,))
        rows = c.fetchall()

        for row in rows:
            result = row[0]
        return result


    @classmethod
    def close(cls):
        conn.commit()
        conn.close()

    # This method plots the bar graph of a combined year of all the positive and the negative senetences in percentage
    @classmethod
    def combinedBarGraph(cls):
        print("Hello from combined bar graphs")
        #negative = list()
        #positive = list()
        polarity_list = list()

        for x in range(10):

            if x == 0:
                month = 'january_description'
            elif x == 1:
                month = 'february_description'
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
            elif x == 9:
                month = 'october_description'

            #sql = "SELECT SUM(positive), SUM(negative) FROM " + month
            sql = "SELECT AVG(polarity) FROM " + month

            c.execute(sql)
            rows = c.fetchall()
            for row in rows:
                # These steps are done for scaling purposes, in terms of percentage, how many are +ve and how many are -ve
                #total = row[0] + row[1]
                #pos_scale = int((row[0]/total) * 100)
                #neg_scale = int((row[1]/total) * 100)
                #positive.append(pos_scale)
                #negative.append(neg_scale)
                polarity_list.append(row)

        #print(positive)
        #print(negative)

        X = ['January','February','March','April','May','June','July', 'August','September','October']
        print(polarity_list)


        #X_axis = np.arange(len(X))

       # plt.bar(X_axis - 0.2, positive, 0.4, label = 'positive')
        #plt.bar(X_axis + 0.2, negative, 0.4, label = 'negative')

        #plt.xticks(X_axis, X)
        #plt.xticks(rotation=20)
       # plt.xlabel("Months")
        #plt.ylabel("Sentiments (in %)")
        #plt.title("Sentiment Analysis of Year 2021")
        #for i in range(len(X)):
               # plt.text(i, positive[i], positive[i], ha = 'right', color = 'black')
               # plt.text(i, negative[i], negative[i], ha = 'left', color = 'black')

        #plt.legend()
        #plt.show()


        plt.plot(X, polarity_list, color='green', marker='o')
       # plt.plot(X, negative, color='red', marker='o')
        plt.title('Average polarity score over the year')
        plt.xlabel('Month')
        plt.xticks(rotation=20)
        plt.ylabel('Average Polarity Score ')
        plt.show()

    # This method plots a bar graph of the positive and the negative senetnces of all the articles of a month
    @classmethod
    def individualBarGraph(cls,month):
            print("Hello from individual bar graph")

            # Get the sum of all the positive articles and negative articles
            sql = "SELECT SUM(positive), SUM(negative) FROM " + month
            c.execute(sql)
            rows = c.fetchall()
            values = list()

            for row in rows:
                values.append(int(row[0]))
                values.append(int(row[1]))

            print(values)
            # Plotting the bar graph
            month = month.replace('_description','')
            X = [month]
            type_of_sentiment = ['Positive', 'Negative']
            data = values
            rects = plt.bar(type_of_sentiment, data, color = ['lightgreen','coral'])
            plt.title("Bar graph for Sentiment Articles %s " %month)

            for rect, label in zip(rects, data):
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')
            plt.show()

    # This method gives us the titles of all the articles for a particular month
    @classmethod
    def getArticlesForMonth(cls,month):
        print("Hello from get articles for month")
        print("The month is ", month)
        sql = "SELECT title FROM " + month
        c.execute(sql)
        rows = c.fetchall()
        titles = list()

        for row in rows:
            titles.append(row[0])

        return titles

    def articleBarGraph(cls, title, month):
        print("Hello from article bar graph")
        try:
            print(title)
            print(month)
            mySql_query = "SELECT positive, negative FROM " + month + " WHERE title = %s "
            c.execute(mySql_query,(title,))

        except Exception as e:
            print(e)

        rows = c.fetchall()
        values = list()
        print(len(rows))

        for row in rows:
            values.append(int(row[0]))
            values.append(int(row[1]))

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

ob = MySQLDbModified
ob.get_month_description("january_description")
#ob.create_month_description("january_description")
#ob.create_month_sentiments("january_sentiments")
