import datetime as dt2
import urllib.request
from datetime import datetime as dt

import bs4

FORMAT = "utf8"
ERROR_MSG = 'Invalid command. Please type "help" for list of commands.'
HELP_MSG = 'Your sentence must contain keywords.\nList of keywords:\n
"your" and "name" to receive bots name\n
"time" and "now" to receive current servers time\n
"euro" to receive current exchange rate of 1 euro\n
For showing this list type "help".'


def download():
    """
    Gets current exchange rate from ČNB page
    """
    ratelist = []
    for day in range(7):
        date = dt2.date.today() - dt2.timedelta(days=day)
        date = dt.strftime(date, format="%d.%m.%Y")
        url = f"https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date={date}"
        page = str(urllib.request.urlopen(url).read())
        soup = bs4.BeautifulSoup(page, features="html.parser")
        rate = soup.get_text()

        # finds occurrence of 'euro'
        start = rate.find("euro")

        # cuts string from 'euro' to first occurrence of '\n'
        if len(rate) > start:
            rate = rate[:0] + rate[start::]
        end = rate.find("\\n")
        if len(rate) > end:
            rate = rate[:end]

        # cuts string from last occurrence of '|' to end of string
        start = rate.rfind("|")
        if len(rate) > start:
            rate = rate[start + 1:]

        ratelist.append(": ".join((date, str(rate))))
    return ratelist


rate = download()


def rem_sym(q):
    """
    Removes illegal characters
    """
    return q.strip(".!?:-_|")


def str2list(str):
    """
    Splits string into individual substrings and converts to list
    """
    str = str.lower()
    return list(str.split(" "))


def answer(question):
    time = dt.time(dt.now()).replace(microsecond=0)
    A1 = "My name is ChatBot, nice to meet You."
    A2 = f"Now is {time}."
    A3 = f"Current exchange of EUR to CZK is:\n{rate}."
    keywords_name = ["your", "name"]
    keywords_time = ["now", "time"]
    keywords_rate = ["euro"]
    keyword_help = ["help"]

    keywords_name_found = [keyword for keyword in keywords_name if keyword in question]
    keywords_time_found = [keyword for keyword in keywords_time if keyword in question]
    keywords_rate_found = [keyword for keyword in keywords_rate if keyword in question]
    keyword_help_found = [keyword for keyword in keyword_help if keyword in question]

    ans = []
    if keywords_name_found == keywords_name:
        ans.append(A1)
    if keywords_time_found == keywords_time:
        ans.append(A2)
    if keywords_rate_found == keywords_rate:
        ans.append(A3)
    if keyword_help_found == keyword_help:
        ans.append(HELP_MSG)
    if not ans:
        ans.append(ERROR_MSG)
    return ans


q1 = "What's your name?"
q2 = "What time is now?"
q3 = "What's the exchange rate of euro?"
