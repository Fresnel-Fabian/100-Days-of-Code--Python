import smtplib
import datetime as dt


MY_EMAIL = "fresnelfabian@gmail.com"
PASSWORD = "tkhvnitfycxxeiij"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="pisama1567@fsouda.com",
                        msg="Subject:My first smtp mail\n\nDay 32 hohoooooooo")



now = dt.datetime.now()
print(now)
year = now.year
print(year)
month = now.month
print(month)

date_of_birth = dt.datetime(year=2001, month=5, day=5)
print(date_of_birth)
print(now.date())
new_date = date_of_birth + dt.timedelta(days=730)
print(new_date)