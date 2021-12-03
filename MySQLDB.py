

import mysql.connector

conn = mysql.connector.connect(user='Admin', password='UCT123@!',
                              host='10.0.0.186',
                              database='overview')
c = conn.cursor()


class MYSQLDb:

    @classmethod
    def create_table_articles(cls):
        print("table created")
        c.execute("DROP TABLE IF EXISTS articles")
        print("Table dropped")
        sql = "CREATE TABLE articles (title VARCHAR(255),descr VARCHAR(255),date VARCHAR(255), datetime DATE,link MEDIUMTEXT,media MEDIUMTEXT,img VARCHAR(255), site VARCHAR(255))"
        print(sql)
        try:
            c.execute(sql)
        except Exception as e:
            print(e)

        print("Table created")

    def insert_data_articles(self, result, url):
        self.create_table_articles()
        print("data inserted")
        counter = 0
        # url and links are same the only difference is https:/
        # so we just update the link with the url
        for item in result:
            item.update(link=url[counter])
            #item.update(datetime="Not Available")


            counter += 1

        for item in result:
            print(list(item.values()))
            item = list(item.values())
            try:
                mySql_insert_query = "INSERT INTO articles (title, descr, date, datetime,link,media,img,site) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
                c.execute(mySql_insert_query, (item))
            except Exception as e:
                print("Exception: ", e)

    @classmethod
    def create_table_positive_texts(cls):
        c.execute("DROP TABLE IF EXISTS positive_texts")
        sql = "CREATE TABLE positive_texts ( positive LONGTEXT)"
        try:
            c.execute(sql)
        except Exception as e:
            print(e)

        #print("Table created")

    def insert_data_positive(self, positive_list):
        self.create_table_positive_texts()
        #print("data inserted")

        for item in positive_list:
            try:
                insert_sql_query = "INSERT INTO positive_texts(positive) VALUES(%s)"
                c.execute(insert_sql_query, (item,))
            except Exception as e:
                print("failed +ve: ", e)

    @classmethod
    def create_table_negative_texts(cls):
        c.execute("DROP TABLE IF EXISTS negative_texts")
        sql = "CREATE TABLE negative_texts ( negative LONGTEXT)"
        try:
            c.execute(sql)
        except Exception as e:
            print(e)

    def insert_data_negative(self, negative_list):
        self.create_table_negative_texts()
       # print("data inserted")

        for item in negative_list:

            try:
                insert_sql_query = "INSERT INTO negative_texts(negative) VALUES(%s)"
                c.execute(insert_sql_query, (item,))
            except Exception as e:
                print("failed +ve: ", e)

    @classmethod
    def create_table_neutral_texts(cls):
        c.execute("DROP TABLE IF EXISTS neutral_texts")
        sql = "CREATE TABLE neutral_texts ( neutral LONGTEXT)"
        try:
            c.execute(sql)
        except Exception as e:
            print(e)

    def insert_data_neutral(self, neutral_list):
        self.create_table_neutral_texts()
       # print("data inserted")

        for item in neutral_list:
            try:
                insert_sql_query = "INSERT INTO neutral_texts(neutral) VALUES(%s)"
                c.execute(insert_sql_query, (item,))
            except Exception as e:
                print("failed +ve: ", e)
    @classmethod
    def getPositiveTexts(cls):
        sql = "SELECT * FROM positive_texts "
        c.execute(sql)
        rows = c.fetchall()
        return rows

    @classmethod
    def getNegativeTexts(cls):
        sql = "SELECT * FROM negative_texts "
        c.execute(sql)
        rows = c.fetchall()
        return rows

    @classmethod
    def getNeutralTexts(cls):
        sql = "SELECT * FROM neutral_texts "
        c.execute(sql)
        rows = c.fetchall()
        return rows



    @classmethod
    def get_data(cls):

        listTitle = []

       # print("data retrieved")

        c.execute("SELECT * FROM articles  ")
        rows = c.fetchall()

        for row in rows:
            listTitle.append(row[0])  # GET ONLY THE TITLE OF THE ARTICLE FROM THE TABLE
        print(len(rows))  # this will give number of occurrences
        return listTitle

    @classmethod
    def close(cls):
        conn.commit()
        conn.close()
