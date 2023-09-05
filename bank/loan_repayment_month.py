"""Loan Payoff Time Calculator
Problem Statement: Write a program that calculates the time it takes to pay off a loan based on the loan amount, interest
rate, and monthly payment.
"""


def loan_repayment_month(amount, interest_rate, monthly_payment):
    month = 0
    while amount > 0:
        interest = amount * (interest_rate / 12) / 100
        print(interest)
        amount += interest - monthly_payment
        print(amount)
        month += 1
        return month


amount = 1000
rate = 5
monthly = 10
loan_pay = loan_repayment_month(amount, rate, monthly)
print(loan_pay)
print(loan_pay // 12)
print(loan_pay % 12)
