"""
Date: 12 january 2021
Author: Sanam kandar
Project: Password generator
"""
import random

user = input("Enter your name: ")
upper_case = 'ABCDEFGHIJKLMNOPQRSTRUVXYZ'
lower_case = 'abcdefghijklmnopqrstuvxyz'
number = '1234567890'
symbol = '!@#$%*&'

password_sequence = upper_case+lower_case+number+symbol
password_length = 16


def password_generator(sequence, length):
    generated = random.sample(sequence, length)
    password = ""
    for element in generated:
        password += element

    print(f"{user} your password is {password}.")
    return None


password_generator(password_sequence, password_length)