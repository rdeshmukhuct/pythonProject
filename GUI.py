import sqlite3
from tkinter import *
from tkinter import ttk

import newspaper
from newspaper import Article
from textblob import TextBlob

import SQLiteDB
import word_frequency
import article_analysis
import sqlite3 as lite

ob = word_frequency.MostCommonWords()  # MUST RENAME THESE OBJECTS TO BETTER REPRESENT THEIR FUNCTIONALITY
obj = article_analysis.GUIFunctions()

conn = sqlite3.connect('UCTT.db')
c = conn.cursor()

objs = SQLiteDB.SQLDb()


# summarize(): takes one arguments which is a url from a selected title and returns nothing
# it displays the summarize article from a list of scraped article from google.
# it calls the class article_analysis.py
def summarize(url):
    article = Article(url)
    article.download()

    try:
        article.parse()
        article.nlp()
    except Exception as e:
        print("<>", e)  # DEBUGGING PURPOSES

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)
    summary.config(state='disabled')
    summary.option_clear()

    # analysis = TextBlob(article.text)


# selected(): takes one argument in the form of <class 'tkinter.Event'> and returns nothing.
# selected(): allows for the user to create a user event when the GUI is running.
# When the drop down-menu is display this function executes and depending on what the user
# enter will trigger an action to Display. For example a pie chart or a bar Graph of the top ten words
# in a article that has been pre-parsed. It calls two separate classes,
# It calls article_analysis.py & word_frequency.py
def selected(event):
    print(type(event))
    if myCombo.get() == "Data Visualization":
        values = obj.read_lines()
        obj.pie_chart(values)
    elif myCombo.get() == "Bar Graph":
        ob.enter_file(textFile.get())
        ob.stopwords()
    elif myCombo.get() == "Market Stock":
        obj.visualize()


# GET QUERY from user
def query():
    conn = sqlite3.connect('UCTT.db')  # This will be removed its redundant to have due to the other other global object
    c = conn.cursor()

    title_article = news_summary.get()  # Saves the title the user clicked into val

    sql_command = "SELECT *, oid FROM articles WHERE title =?"
    c.execute(sql_command, [title_article])  # Passes string sql command and value from button

    records = c.fetchall()
    # re = records

    print_records = ''  # Creates an empty string to save Print info about query

    # For loop is just to print out the current record that will be passed into
    # GUI.summarize()
    for record in records:
        print_records += str(record[0]) + " >" + str(record[2]) + "\n"

    summarize(record[4]) # passes the url from the clicked title into summarize()

    query_label = Label(root, text=print_records) # Displays the info on the GUI
    query_label.pack()

    conn.commit()
    conn.close()


# GUI functionality begins here, This is what displays everything
root = Tk()

root.title("Title")

label_ticker = Label(root, text="Ticker Symbol", font='Roboto')
label_ticker.pack()
text_ticker = Label(root, text="Ultra Clean Tech", font='Roboto')
text_ticker.pack()

summary = Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

options = ["Market Stock", "Data Visualization", "Bar Graph"]
txtFile = ['PositiveText.txt', 'NegativeText.txt', 'NeutralText.txt']
# title_and_url_dict = dict(zip(news_paper_title, urls))  # Zips together news paper title as key and urls as values

clicked = StringVar()
clicked.set("Options")

label_options = Label(root, text="Menu", font=('Roboto', 10))
label_options.pack()

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", selected)
myCombo.pack()

label_info = Label(root, text="Sentiment Files", font=('Roboto', 10))
label_info.pack()

textFile = ttk.Combobox(root, value=txtFile)
textFile.current(0)
textFile.bind("<<TextSelected>>", ob.enter_file)
textFile.pack()

label_news = Label(root, text="Select Articles", font=('Roboto', 10))
label_news.pack()

news_summary = ttk.Combobox(root, value=objs.get_data())
news_summary.current(0)
news_summary.bind("<<TextSelected>>", selected)
news_summary.pack()

# create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.pack()

root.mainloop()
