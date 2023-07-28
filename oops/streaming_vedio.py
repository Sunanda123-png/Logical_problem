"""Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:

BasicPlan	StandardPlan	Premium Plan
✓	✓	✓	can_stream
✓	✓	✓	can_download
✓	✓	✓	has_SD
✓	✓	has_HD
✓	has_UHD
1	2	4	num_of_devices
$8.99	$12.99	$15.99	price
Examples
BasicPlan.has_SD ➞ True

PremiumPlan.has_SD ➞ True

BasicPlan.has_UHD ➞ False

BasicPlan.price ➞ "$8.99"

PremiumPlan.num_of_devices ➞ 4
Try using Inheritance to complete the challenge! If you're unsure what that means,
try checking out the Python class tutorials in the Resources tab.
"""


# class Stream:
#     def __init__(self, plan):
#         self.plan = plan
#
#     def has_sd(self):
#         return True if "sd" in self.plan else False
#
#     def has_uhd(self):
#         return True if "uhd" in self.plan else False
#
#     def price(self):
#         return self.plan[-1]
#
#     def device(self):
#         return self.plan[-2]
#
#
# class BasicPlan(Stream):
#     def __init__(self):
#         super().__init__(["stram", "download", "sd", 1, 8.99])
#
#
# class StandardPlan(Stream):
#     def __init__(self):
#         super().__init__(["stram", "download", "sd", 'hd', 2, 12.99])
#
#
# class PremiumPlan(Stream):
#     def __init__(self):
#         super().__init__(["stram", "download", "sd", "hd", "uhd", 4, 15.99])
#
#
# bp = BasicPlan()
# print(bp.has_sd())
# print(bp.has_uhd())
#
# pp = PremiumPlan()
# print(pp.has_sd())
# print(pp.has_uhd())
# print(pp.device())


class Basic_plan:
    can_stream = True
    can_download = True
    has_sd = True
    has_hd = False
    has_udh = False
    number_device = 1
    price = 8.99


class Standard_plan(Basic_plan):
    has_hd = True
    price = 12.99
    number_device = 2


class Premium_plan(Basic_plan):
    has_udh = True
    price = 15.99
    number_device = 4


bp = Basic_plan()
print(bp.has_sd)
print(bp.has_udh)
