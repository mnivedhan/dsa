def feasible(time_array, readers_count, time_limit):
    time_taken = readers_used = 0
    for time in time_array:
        if time_taken + time > time_limit:
            readers_used += 1
            time_taken = 0
        time_taken += time

    if time_taken != 0:
        readers_used += 1

    return readers_used <= readers_count


def minimal_time_to_read(newspaper_read_times, no_of_readers):
    min_possible_time = max(newspaper_read_times)
    max_possible_time = sum(newspaper_read_times)

    result = -1

    left = min_possible_time
    right = max_possible_time

    while left < right:
        mid = (left + right) // 2
        if feasible(newspaper_read_times, no_of_readers, mid):
            result = mid
            right = mid
        else:
            left = mid + 1

    return result

if __name__ == '__main__':
    newspaper_read_times = [7,2,5,10,8]
    no_of_readers = 2
    print(minimal_time_to_read(newspaper_read_times, no_of_readers))
