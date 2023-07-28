import os
import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "fresnelfabian@gmail.com"
EMAIL_PASSWORD = os.environ["PASSWORD"]


response = requests.get("https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0B3BS9BRW/ref=sr_1_2?keywords=13"
                        "-inch+macbook+air+apple+m2+chip+8-core+cpu+and+8-core+gpu+8gb%2F256gb&sr=8-2",
                        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                                               "like Gecko) Chrome/114.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
price = int(soup.find(name="span", class_="a-price-whole").getText().replace(",", "").replace(".", ""))
print(price)
if price <= 134990:
    message = f"Apple 2022 MacBook Air Laptop with M2 chip: 34.46 cm (13.6-inch) Liquid Retina Display, 8GB RAM, " \
              f"512GB SSD Storage, Backlit Keyboard, 1080p FaceTime HD Camera. Works with iPhone/iPad; Silver \n" \
              f"price is {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="fresnelprince@gmail.com", msg=f"Subject:Amazon Price Alert!"
                                                                                     f"\n\n{message}\n".encode("utf-8"))
        print("success")