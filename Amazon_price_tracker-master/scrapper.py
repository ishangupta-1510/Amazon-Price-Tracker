import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the base url
URL = 'https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1624987878&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQ1NNMVJGNVRYNjUwJmVuY3J5cHRlZElkPUEwNjgxMDM1VUhYNkxURUdQQU5JJmVuY3J5cHRlZEFkSWQ9QTAzMjQ0MDAxRldNOFJGVVZYRkFTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

# set the headers and user string
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}


def check_price():

    # fetch the HTML of the page
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # get the price and product title
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text().replace(
        ',', '').replace('₹', '').replace(' ', '').strip()

    # converting the obtained string to float
    converted_price = float(price[0:5])

    # ouput the price and the product title
    print(converted_price)
    print(title.strip())

    # check if the price dropped
    if(converted_price > 75000):
        send_mail()


def send_mail():
    # setting connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # encryption
    server.starttls()
    server.ehlo()
    server.login('siddharth007gandhi@gmail.com', 'ftgxhwqmefgidpqw')

    # the connection is set

    # make the content for the mail
    subject = 'The price has dropped!!'
    body = 'The link to the item is https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1624987878&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQ1NNMVJGNVRYNjUwJmVuY3J5cHRlZElkPUEwNjgxMDM1VUhYNkxURUdQQU5JJmVuY3J5cHRlZEFkSWQ9QTAzMjQ0MDAxRldNOFJGVVZYRkFTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg = f"Subject: {subject}\n\n{body}"

    # sending the mail
    server.sendmail(
        'siddharth007gandhi@gmail.com',
        'siddharth007gandhi@gmail.com',
        msg
    )

    print('sent the email !!')

    server.quit()


# call the price checking function once per 24 hrs or 1 day
while(True):
    check_price()
    time.sleep(60*60*24)
