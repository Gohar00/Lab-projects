#imports any library
import validators
import phonenumbers
from phonenumbers import timezone


def email_check(email):

    """This function validates an email."""

    # 1. Returns a boolean variable using a library 'validators'
    valid_email = validators.email(email)

    # 2. Checks valid_email is true or false
    if valid_email:
        return f'The {email} is valid'
    else:
        return f'The {email} is invalid'


def check_website(url):

    """This function validates a website URL."""

    # 1. Returns a boolean variable using a library 'validators'
    valid_url = validators.url(url)

    # 2. Checks valid_url is true or false
    if valid_url:
        return f'The {url} is valid'
    else:
        return f'The {url} is invalid'


def check_date(year, month, day):

    """This function validates a date."""

    # 1. The number of days in all months
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 2. Checks if year is leap year, changes the number of days in February
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[2] = 29

    # 3. Checks the date is true or false
    valid_date = (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
    if valid_date:
        return f'The date is valid'
    else:
        return f'The date is invalid'


def check_number(string):

    """This function validates a number."""

    # 1. Checks is the string numeric or no
    valid_num = (string.isnumeric()) or (string.isdigit())
    if valid_num:
        return f'The {string} is numeric'
    else:
        return f'The {string} is not numeric'


def check_credit_card(card_number):

        """This function validates a credit card number."""

        # 1. Change datatype to list[int]
        card_number = [int(num) for num in card_number]

        # 2. Remove the last digit:
        check_digit = card_number.pop(-1)

        # 3. Reverse the remaining digits:
        card_number.reverse()

        # 4. Double digits at even indices
        card_number = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]

        # 5. Subtract 9 at even indices if digit is over 9
        # (or you can add the digits)
        card_number = [num - 9 if idx % 2 == 0 and num > 9 else num for idx, num in enumerate(card_number)]

        # 6. Add the checkDigit back to the list:
        card_number.append(check_digit)

        # 7. Sum all digits:
        check_sum = sum(card_number)

        # 8. If checksum is divisible by 10, it is valid.
        valid_card = (check_sum % 10 == 0)

        if valid_card:
            return f'The card_number is valid'
        else:
            return f'The card_number is not valid'


def check_phone_number(phone_number):

    """This function validates a phone number."""

    # 1. This function parses the number and get the Country Code and National Number
    phone_number = phonenumbers.parse(phone_number)

    # 2. This function gets the timezone of the phone number
    timezone_number = timezone.time_zones_for_number(phone_number)

    # 3. Checks the phone number is valid or no
    valid_phone_number = phonenumbers.is_valid_number(phone_number)

    if valid_phone_number:
        return f'The number is valid and her timezone is {timezone_number}'
    else:
        return f'The number is not valid'



while True:

    # 1. Gives a question and suggest options
    question_1 = input("What do you want check? \n"
                     "1. Email\n"
                     "2. Website URL\n"
                     "3. Date\n"
                     "4. Number\n"
                     "5. Credit Card Number\n"
                     "6. Mobile Phone Number\n"
                     "Press 1,2,3,4,5 or 6: ")

    if question_1 == '1':
        email = input("Enter your email: ")
        print(email_check(email))
    elif question_1 == '2':
        website = input("Enter your website: ")
        print(check_website(website))
    elif question_1 == '3':
        year = int(input('Please enter the year: '))
        month = int(input('Please enter the month: '))
        day = int(input('Please enter the day: '))
        print(check_date(year, month, day))
    elif question_1 == '4':
        number = input('Enter the number: ')
        print(check_number(number))
    elif question_1 == '5':
        card_number = input('Please enter your card number: ')
        print(check_credit_card(card_number))
    elif question_1 == '6':
        phone_number = input("Enter your number phone: ")
        print(check_phone_number(phone_number))

    # 2. gives second question for continue the operation
    question_2 = input("Do you want finish the operation? y/n : ")
    if question_2 == 'n':
        continue
    elif question_2 == 'y':
        break