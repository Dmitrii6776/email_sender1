import smtplib
import datetime
import random
import pandas

my_email = 'put your email hear'
password = 'put your password'

now = datetime.datetime.now()
now_month = now.month
now_day = now.day
now_time = now.hour

data_frame = pandas.read_csv('birthdays.csv')
data_dict = data_frame.to_dict(orient='records')


def check_birth_day():
    for i in range(len(data_dict)):
        if data_dict[i]['month'] == now_month and data_dict[i]['day'] == now_day:
            name = data_dict[i]["name"]
            email = data_dict[i]['email']
    send_letter(name, email)


def correct_letter(name):
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as letter:
        letter_list = letter.read()
        letter_list = letter_list.replace('[NAME]', name)
        return letter_list


def send_letter(name, email):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f'Subject:Hello {name}.\n\n{correct_letter(name)}')


check_birth_day()