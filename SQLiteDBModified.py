import sqlite3 as lite

conn = lite.connect('Month.db')
c = conn.cursor()


class SQLDbModified:
    # Done
    @classmethod
    def create_month_description(cls, month_sentiment):
        value_pass = 'DROP TABLE IF EXISTS "{}" '.format(month_sentiment)
        c.execute(value_pass)
        c.execute("""CREATE TABLE "{}" (
                                         title text,
                                         datetime text,
                                         link text,
                                         positive INTEGER,
                                         negative INTEGER,
                                         polarity Integer
                              )""".format(month_sentiment))
        print("Table created")

    # Done
    @classmethod
    def create_month_sentiments(cls, month_sentiment):
        value_pass = 'DROP TABLE IF EXISTS "{}" '.format(month_sentiment)
        c.execute(value_pass)
        c.execute("""CREATE TABLE "{}" (
                                             title text,
                                             datetime text,
                                             positive text,
                                             negative text
                                  )""".format(month_sentiment))
        print("Table created")

    @classmethod
    def insert_month_sentiments(self, month_sentiment, title, date, positive, negative):
        value = """INSERT INTO "{}" VALUES ("{}", "{}", "{}", "{}")""".format(month_sentiment, title, date, positive, negative)
        try:
            c.execute(value)
            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def insert_month_description(self, month_sentiment, title, date, link, positive, negative, polarity):
        value = """INSERT INTO "{}" VALUES ("{}", "{}", "{}", "{}")""".format(month_sentiment, title, date, link, positive, negative, polarity)
        try:
            c.execute(value)
            conn.commit()
        except Exception as e:
            print("failed +ve: ", e)
        conn.commit()

    @classmethod
    def get_month_description(cls, month_sentiment):
        value_pass = 'SELECT * FROM "{}" '.format(month_sentiment)
        c.execute(value_pass)
        rows = c.fetchall()

        for row in rows:
            print("Title:" + row[0])
            # "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + str(row[3]) + " \t Negative:" + str(row[4])
            # + "\t Polarity Score : " + str(row[5]))

    @classmethod
    def get_month_sentiments(cls, month_sentiment):
        value_pass = 'SELECT * FROM "{}" '.format(month_sentiment)
        c.execute(value_pass)
        rows = c.fetchall()

        for row in rows:
            print(
                "Title:" + row[0] + "\t Date: " + row[1] + "\t Positive: " + row[2] + " \t Negative:" + row[3])

    @classmethod
    def close(cls):
        conn.commit()
        conn.close()


ob = SQLDbModified
# ob.create_month_description()
ob.get_month_description("february_sentiments")
ob.get_month_sentiments("february_sentiments")
