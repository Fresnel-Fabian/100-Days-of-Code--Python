import smtplib
import datetime as dt 
from random import choice

MY_EMAIL = "fresnelfabian@gmail.com"
PASSWORD = "tkhvnitfycxxeiij"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = choice(all_quotes)
        msg = f"Subject:Quote\n\n{quote}"
    print(msg)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="frenelfabian@gmail.com",
                            msg=msg)
        print("success")
        