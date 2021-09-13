from tkinter import *
from tkinter import ttk

import newspaper
from newspaper import Article
from textblob import TextBlob
import main
import article_analysis
import sqlite3 as lite

ob = main.MostCommonWords()
obj = article_analysis.GUIFunctions()


# summarize(): takes one arguments which is a url from a selected title and returns nothing
# it displays the summarize article from a list of scraped article from google.
# it calls the class article_analysis.py
def summarize(url):
    print("Summarize()", url)
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
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
# It calls article_analysis.py & main.py
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
    elif myCombo.get() == "Summary":
        try:
            summarize(title_and_url_dict.get(news_summary.get()))
        except newspaper.article.ArticleException:
            print("Enter An Article First")


urls, results = obj.search_articles()
news_paper_title = [key['title'] for key in results]

# GUI functionality begins here, This is what displays everything
root = Tk()

root.title("Ham-Let")

label_ticker = Label(root, text="Ticker Symbol", font='Roboto')
label_ticker.pack()
text_ticker = Label(root, text="Ham-let (israel-canada) ltd", font='Roboto')
text_ticker.pack()

summary = Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

options = ["Market Stock", "Data Visualization", "Bar Graph", "Summary"]
txtFile = ['PositiveText.txt', 'NegativeText.txt', 'NeutralText.txt']
title_and_url_dict = dict(zip(news_paper_title, urls))

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

news_summary = ttk.Combobox(root, value=news_paper_title)
news_summary.current(0)
news_summary.bind("<<TextSelected>>", selected)
news_summary.pack()

root.mainloop()
