from datetime import datetime


def calculate_interest_rate(A, z, conditions):
    rate_sum = 0
    start_date_lst = []
    end_date_lst = []
    rate_lst = []
    condition_interests = []
    conditions = [(datetime.strptime(start_date, "%d-%b-%y"), datetime.strptime(end_date, "%d-%b-%y"), rate) for
                  start_date, end_date, rate in conditions]

    for condition in conditions:
        start_date, end_date, rate = condition
        # start_date = datetime.strptime(start_date, "%d-%b-%y")
        # end_date = datetime.strptime(end_date, "%d-%b-%y")
        start_date_lst.append(start_date)
        end_date_lst.append(end_date)
        rate_lst.append(rate)

    overlap_start_date = max(start_date_lst)
    overlap_end_date = min(end_date_lst)
    max_end_date = max(end_date_lst)
    days = (overlap_end_date - overlap_start_date).days + 1
    rate_sum = sum(rate_lst)

    for i, cond in enumerate(conditions):
        start_date, end_date, rate = cond

        if rate_sum > z:
            rate_sum = z

        interest_condition = A * (rate / 100) * days / 365
        condition_charge = rate / rate_sum * interest_condition

        if i < len(conditions) - 1:
            next_start_date, next_end_date, next_rate = conditions[i + 1]

            if next_start_date < overlap_end_date:
                overlap_end_date = min(next_end_date, overlap_end_date)
            else:
                condition_interests.append(condition_charge)
                overlap_start_date = next_start_date
                overlap_end_date = min(next_end_date, max_end_date)
                days = (overlap_end_date - overlap_start_date).days + 1
                rate_sum += rate_lst[i]

        condition_interests.append(condition_charge)

    total_interest = sum(float(interest_condition) for interest_condition in condition_interests)

    return f"total interest: {total_interest}, conditional interest: {condition_interests}"


# Test case
conditions = [("10-Jan-20", "20-Jan-20", 2), ("15-Jan-20", "25-Jan-20", 3)]
A = 100
z = 4
result = calculate_interest_rate(A, z, conditions)
print(result)
# def calculate_interest_rate(A, z, conditions):
#     total_interest = 0
#     conditional_interests = []
#
#     for i, (start_day, end_day, rate) in enumerate(conditions):
#         overlap_start = max(start_day, conditions[i - 1][0] if i > 0 else start_day)
#         overlap_end = min(end_day, conditions[i + 1][1] if i < len(conditions) - 1 else end_day)
#         days_in_overlap = max(0, overlap_end - overlap_start + 1)
#
#         interest = A * (rate / 100) * days_in_overlap / 365
#
#         if rate > z:
#             rate = z
#
#         total_interest += interest
#
#         if i < len(conditions) - 1:
#             condition_interest = (rate / z) * interest
#             conditional_interests.append(condition_interest)
#
#     return f"total interest: {total_interest}, conditional interest: {conditional_interests}"
#
# conditions = [("10-Jan-20", "20-Jan-20", 2), ("15-Jan-20", "25-Jan-20", 3)]
# A = 100
# z = 4
# result = calculate_interest_rate(A, z, conditions)