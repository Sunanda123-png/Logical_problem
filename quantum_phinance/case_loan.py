from datetime import datetime, timedelta


def calculate_interest(A, z, conditions):
    interest_cond_one =0
    total_interest = 0
    condition_interests = [0] * len(conditions)

    conditions.sort(key=lambda x: x[0])

    for i in range(len(conditions)):
        start_date, end_date, rate = conditions[i]
        overlap_start_date = start_date
        overlap_end_date = end_date
        rate_sum = rate
        if rate > z:
            rate = z
        if len(conditions) > 1:
            for j in range(i + 1, len(conditions)):
                next_start_date, next_end_date, next_rate = conditions[j]

                overlap_start_date = max(overlap_start_date, next_start_date)
                overlap_end_date = min(overlap_end_date, next_end_date)
                rate_sum = rate_sum + next_rate
                day = (overlap_end_date - overlap_start_date).days + 1
                delta = timedelta(days=day)

                if overlap_start_date > overlap_end_date:
                    break

                if rate_sum > z:
                    rate_sum = z

                interest_overlap = A * (rate_sum / 100) * day / 365
                print(rate_sum)

                total_interest = interest_overlap

                if start_date < overlap_start_date and end_date <= overlap_end_date:
                    interest_cond_one = A * (rate / 100) * ((end_date - start_date - delta).days + 1) / 365
                    total_interest += interest_cond_one
                interest_cond_three = A * (next_rate/100) * ((next_end_date - next_start_date - delta).days + 1)/365
                total_interest += interest_cond_three

                overlap_first_rate_charge = (rate / rate_sum) * interest_overlap
                overlap_secound_rate_charge = (next_rate / rate_sum) * interest_overlap
                condition_one_charge = interest_cond_one + overlap_first_rate_charge
                condition_interests[i] += condition_one_charge
                condition_two_charge = overlap_secound_rate_charge + interest_cond_three
                condition_interests[j] += condition_two_charge
        else:
            interest = A * (rate/100) * ((end_date-start_date).days + 1)/365
            total_interest = interest

    return total_interest, condition_interests


# Test case
A = 100
z = 4
conditions = [
              (datetime(2020, 1, 15), datetime(2020, 1, 25), 3),
              (datetime(2020, 1, 18), datetime(2020, 1, 22), 3)
              ]

total_interest, condition_interests = calculate_interest(A, z, conditions)
print(f"Total Interest: {total_interest}")
print(f"Conditional Interest: {condition_interests}")