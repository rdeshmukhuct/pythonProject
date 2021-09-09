from tkinter import *
from tkinter import ttk
from newspaper import Article
from textblob import TextBlob
import main
import article_analysis
import sqlite3 as lite

ob = main.MostCommonWords()
obj = article_analysis.GUIFunctions()


# summarize(): takes zero arguments and returns nothing
# it displays the summarize article from a list of scraped article from google.
# it calls the class article_analysis.py
def summarize():
    first_article_in_list = obj.search_articles()
    article = Article(first_article_in_list[0], fetch_images=False)

    article.download()
    try:
        article.parse()
        article.nlp()
    except:
        pass

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)
    summary.config(state='disabled')

    analysis = TextBlob(article.text)


# selected(): takes one argument in the form of <class 'tkinter.Event'> and returns nothing.
# selected(): allows for the user to create a user event when the GUI is running.
# When the drop down-menu is display this function executes and depending on what the user
# enter will trigger an action to Display. For example a pie chart or a bar Graph of the top ten words
# in a article that has been pre-parsed. It calls two separate classes,
# It calls article_analysis.py & main.py
def selected(event):
    print(type(event))
    if myCombo.get() == "Pie Chart":
        values = obj.read_lines()
        obj.pie_chart(values)
    elif myCombo.get() == "Bar Graph":
        ob.enter_file(textFile.get())
        ob.stopwords()
    elif myCombo.get() == "Market Stock":
        obj.visualize()
    elif myCombo.get() == "Summary":
        summarize()


root = Tk()

root.title("Stock Market version 10")

label_ticker = Label(root, text="Ticker Symbol", font='Roboto')
label_ticker.pack()
text_ticker = Label(root, text="Ultra Clean Technology(UCTT)", font='Roboto')
text_ticker.pack()

summary = Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

options = ["Market Stock", "Pie Chart", "Bar Graph", "Summary"]
txtFile = ['PositiveText.txt', 'NegativeText.txt', 'NeutralText.txt']

clicked = StringVar()
clicked.set("Options")

label_options = Label(root, text="Options", font='Roboto')
label_options.pack()

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", selected)
myCombo.pack()

label_info = Label(root, text="Articles", font='Roboto')
label_info.pack()

textFile = ttk.Combobox(root, value=txtFile)
textFile.current(0)
textFile.bind("<<TextSelected>>", ob.enter_file)
textFile.pack()

root.mainloop()
