""" Return on Investment (ROI) Calculator
Problem Statement: Write a program that calculates the return on investment (ROI) based on the initial investment amount
and the final investment value.
"""


def return_investment(rate, principle, time):
    interest = (rate * principle * time) / 100
    final_investment = principle + interest
    return final_investment


rate = 7.577
principle = 1000
time = 10
print(return_investment(rate, principle, time))
