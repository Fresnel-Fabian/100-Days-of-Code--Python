##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random
import datetime as dt

MY_EMAIL = "fresnelfabian@gmail.com"
PASSWORD = "tkhvnitfycxxeiij"
PLACEHOLDER = "[NAME]"
# 1. Update the birthdays.csv
birthday_list = pd.read_csv("birthdays.csv")
birthday_dict = birthday_list.to_dict(orient="index")

# 2. Check if today matches a birthday in the birthdays.csv
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day
for key in birthday_dict:
    if (birthday_dict[key]["month"]) == current_month and (birthday_dict[_]["day"]) == current_day:
        name = birthday_dict[key]["name"]
        email = birthday_dict[key]["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
        random_letter = f"letter_{random.randint(1, 3)}.txt"
        with open(f"letter_templates/{random_letter}") as letter_file:
            letter = letter_file.read()
            sent_letter = letter.replace(PLACEHOLDER, name)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy"
                                                        f" Birthday\n\n{sent_letter}")
            print("success")
