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

    @classmethod
    def close(cls):
        conn.commit()
        conn.close()

