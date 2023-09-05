import math

"""
Problem: Present Value Calculation
Description: Write a function that calculates the present value of a future cash flow based on a discount rate.
Solution: Implement a function that uses the present value formula: PV = FV / (1 + r)^n, where PV is the present value,
FV is the future value, r is the discount rate, and n is the number of periods.
"""


class Valuation:
    def __init__(self, discount_rate, future_value, number_periods):
        self.rate = discount_rate
        self.fv = future_value
        self.n = number_periods

    def present_valuation(self):
        pv = self.fv / (1 + (self.rate / 100)) ** self.n
        return pv

    def present_valuation_with_future_compound(self):
        pv = self.fv / math.exp(self.rate/100 * self.n)
        return pv


"""
Use Case: Calculate the present value of a future cash flow with a discount rate of 5% and a single period. 
Question: What is the present value of $10,000 to be received after 1 year with a discount rate of 5%?
"""
present_value = Valuation(5, 10000, 1)
present = present_value.present_valuation()
print(f'present value of future cash flow :- {present}')

"""Use Case: Calculate the present value of a future cash flow with a discount rate of 8% and multiple periods. 
Question: What is the present value of $5,000 to be received annually for 3 years with a discount rate of 8%?
"""
present_value = Valuation(8, 5000, 3)
present = present_value.present_valuation()
print(f'present value of future cash flow :- {present}')

"""
Use Case: Calculate the present value of a future cash flow with a discount rate of 3.5% and continuous compounding. 
Question: What is the present value of $50,000 to be received after 5 years with continuous compounding and a discount 
rate of 3.5%?
"""
present_value = Valuation(3.5, 50000, 5)
present = present_value.present_valuation_with_future_compound()
print(f'present value of future cash flow :- {present}')

