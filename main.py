
import smtplib
import pandas
import random
import datetime as dt

my_email = "pythoncode1234@gmail.com"
password = "ILOVEYOUALOT"

#Read csv
data = pandas.read_csv("birthdays.csv")

#Get current month and day
now = dt.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
birthday_tuple = (int(month), int(day))

#Create a dictionary and check if their birthday is contained in the dictionary
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
if birthday_tuple in birthday_dict:
    birthday_person = birthday_dict[birthday_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as data_file:
        letter = data_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{letter}")





