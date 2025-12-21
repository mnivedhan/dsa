import math


def feasible(pile_of_bananas, total_hours_given, min_number_of_bananas_per_hour):
    carry_over = 0
    hours_used = 0

    for bananas in pile_of_bananas:
        hours_used += math.ceil(bananas/min_number_of_bananas_per_hour)

    return hours_used <= total_hours_given

def minimum_time_to_eat(pile_of_bananas, total_hours_given):

    left = min(pile_of_bananas)
    right = max(pile_of_bananas)
    result = -1

    while left < right:
        min_number_of_bananas_per_hour = (left + right) // 2
        if feasible(pile_of_bananas, total_hours_given, min_number_of_bananas_per_hour):
            result = min_number_of_bananas_per_hour
            right = min_number_of_bananas_per_hour
        else:
            left = min_number_of_bananas_per_hour + 1

    return  result

if __name__ == '__main__':
    pile_of_bananas = [3,6,7,11]
    total_hours_given = 8
    print(minimum_time_to_eat(pile_of_bananas, total_hours_given))
