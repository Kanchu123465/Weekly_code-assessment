import string
import smtplib
import re
name=input("Enter the name:")
email=input("Enter the email:")
regex='^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
valid=re.match(regex,email)
if valid:
    ALPHABET = string.ascii_uppercase

FOOD_WITH_PRICES = [
    ("Tea", 20),
    ("Coffee",   20),
    ("Masala Dosa", 50),
    ("Email Bill or view Bill",0)
]

def print_stilish_menu(food_with_prices):
    
    for (index, (food, price)) in enumerate(food_with_prices):
        print("""\
| {letter}\tThe "{food}"      | $ {price}  |
------------------------------------------
""".format(letter=ALPHABET[index], food=food, price=price))

print_stilish_menu(FOOD_WITH_PRICES)
total = 0
while(True):
    print("Total:", total)
    x = input("Select a letter or 'done': ")
    if x in ALPHABET[:len(FOOD_WITH_PRICES)]:
        total += FOOD_WITH_PRICES[ALPHABET.index(x)][1]
    elif x=='D':
        print("You spent {}".format(total))
        message=str(total)
        print(message)
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("kanchu954@gmail.com", "Kanchu@8+")
        connection.sendmail("kanchu954@gmail.com", "kanchanagoudar123@gmail.com", msg)
        print("email has successfully sent")
        connection.quit()
    elif x == 'done':
        break

    else:
        print("Invalid Input")
else:
    print("invalid email")
