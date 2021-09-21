import sqlite3 as lite
import sys
import article_analysis
import article_sentiment

values = article_analysis.GUIFunctions()
urls, result = values.search_articles()

counter = 0
# url and links are same the only difference is https:/
# so we just update the link with the url
for item in result:
    item.update(link=urls[counter])
    counter += 1

# v = [item for item in result]
# print(v)
# i = 0
# for it in result:
#     it.update(url=urls[i])
#     i+=1
#     print(it)

# had to change the name of the db as for some reason test.db giving wierd errors
conn = lite.connect('UCTT.db')
c = conn.cursor()

# We don't want our table to be added with the same data always so everytime we drop the table and
# then create a new one
c.execute("""DROP TABLE IF EXISTS test""")
#
c.execute("""CREATE TABLE test (
             title text,
             desc text,
             date text,
             datetime text,
             link text,
             img text,
             media text,
             site text
  )""")

# user1 = {'title': 'Why Ultra Clean Holdings Is The Semiconductor Stock To Own',
#          'desc': 'bookmark_border',
#          'date': 'Aug 30',
#          'datetime': 'nan',
#          'link': 'news.google.com/./articles/CAIiEM7xF7pe9MktDUQYBWho_dgqFggEKg0IACoGCAowkqEGMJBZMOniuwY?hl=en-US&gl=US&ceid=US%3Aen',
#          'img': 'https://lh3.googleusercontent.com/proxy/0UcVzsqDIHV1bRJW9bCb1GyKOPcme8kvbIxRxU66lTD-Js7SslJNriqFuGpo8jUg0NFFWdCjsM9vS9uyqfzss5k3u869sIEE4QeMKobIu3MbIrB12cVMkJw-r-N3bI8UE68IzzFGmFfcM-u4RgdNMfAE0vV9I6kN7zHziQ=s0-w100-h100-p-df',
#          'media': None,
#          'site': 'Seeking Alpha'
#          'url': }
#
#
for item in result:
    try:
        c.execute("INSERT INTO test VALUES (:title, :desc, :date, :datetime, :link, :img, :media, :site)", item)
    except:
        pass
# #
# #
# #
c.execute("SELECT * FROM test ")

#
#
rows = c.fetchall()
for row in rows:
    print(row)
print(len(rows))


# print(c.fetchone())

conn.commit()

conn.close()