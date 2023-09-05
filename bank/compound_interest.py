"""Compound Interest Calculator
Problem Statement: Write a program that calculates the compound interest earned on an investment based on the principal
amount, interest rate, and time period.
"""


def compound_interest(principle_amount, rate, time_period, n):
    amount = principle_amount * (1 + rate / n) ** (n * time_period)
    interest = amount - principle_amount
    return interest

rate = 7.57
principle = 1
time = 10
frequent_compound = 10
print(compound_interest(rate,principle,time,frequent_compound))
