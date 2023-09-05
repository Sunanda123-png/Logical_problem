"""
Simple Interest Calculator
Problem Statement: Write a program that calculates the simple interest earned on a loan or investment based on the principal
amount, interest rate, and time period.
"""


def simple_interest(rate, principle, time):
    interest = (rate * principle * time) / 100
    return interest

rate = 7.57
principle = 1000
time = 10
print(simple_interest(rate, principle, time))
