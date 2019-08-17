import requests
from bs4 import BeautifulSoup
import smtplib
from config import email_password, email_username

URL = 'https://www.amazon.it/Xiaomi-Smartphone-Snapdragon-fotocamera-batteria/dp/B07SJG88JH/ref=sr_1_5?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=LS0CKS90OTHV&keywords=xiaomi&qid=1566032982&s=gateway&sprefix=xiaomi%2Caps%2C221&sr=8-5'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}


def checkprice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find("span", id="price_inside_buybox").get_text()
    converted_price = float((price.strip()[0:5].replace(',', '.')))

    if converted_price < 300:
        send_mail()
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_username, email_password)

    subject = 'Hey! The Price fell down'
    body = 'Check the Amazon link: ' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "giovanni.melongo@gmail.com",
        email_username,
        msg
    )
    print('Hey, email has been sent!')

    server.quit()


checkprice()
