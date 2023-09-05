def calculate_interest_rate(A, z, conditions):
    rate_sum = 0
    start_day_lst = []
    end_day_lst = []
    rate_lst = []
    interest_condition_one = 0
    interest_condition_two = 0
    interest_condition_three = 0
    condition_interests = []
    condition_one = 0
    condition_two = 0
    condition_three = 0
    condition_one_charge = 0
    condition_two_charge = 0

    for condition in conditions:
        start_day, end_day, rate = condition
        start_day_lst.append(start_day)
        end_day_lst.append(end_day)
    overlap_start_day = max(start_day_lst)
    overlap_end_day = min(end_day_lst)
    max_end_day = max(end_day_lst)
    days = (overlap_end_day - overlap_start_day) + 1

    for cond in conditions:
        start_day, end_day, rate = cond
        rate_lst.append(rate)
        if overlap_start_day and overlap_end_day:
            rate_sum = sum(rate_lst)
        if rate_sum > z:
            rate_sum = z
        if rate > z:
            rate = z

        if start_day < overlap_start_day and end_day <= overlap_end_day:
            interest_condition_one = A * (rate / 100) * (end_day - start_day - days + 1) / 365
            condition_one = rate / rate_sum * interest_condition_one
        elif overlap_start_day and overlap_end_day:
            interest_condition_two = A * (rate_sum / 100) * days / 365
            condition_two = rate / rate_sum * interest_condition_two
        if max_end_day > overlap_end_day:
            if start_day >= overlap_start_day:
                interest_condition_three = A * (rate / 100) * (end_day - start_day - days + 1) / 365
                print(interest_condition_three)
                condition_three = rate / rate_sum * interest_condition_three

        if len(conditions) > 1:
            condition_one_charge = condition_one + rate / rate_sum * condition_two
            condition_two_charge = rate / rate_sum * condition_two + condition_three
    condition_interests.append(condition_one_charge)
    condition_interests.append(condition_two_charge)

    total_interest = float(interest_condition_one) + float(interest_condition_two) + float(interest_condition_three)

    return f"total interest:- {total_interest}, conditional interest:- {condition_interests}"


A = 100
z = 4
conditions = [(10, 20, 2), (15, 25, 3)]
# conditions = [(10, 20, 2), (21, 30, 3)]
# conditions = [(10, 20, 7), (15, 25, 6)]
# conditions = [(10, 20, 2)]
# conditions = [(10, 20, 7)]
# conditions = [(10, 20, 2), (15, 25, 6), (21, 31, 6)]
print(calculate_interest_rate(A, z, conditions))
