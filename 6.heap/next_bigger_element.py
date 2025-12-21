# Non-Optimized solution as it requires O(n log n)
def next_big_element(array):
    result = [-1] * len(array)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                result[i] = array[j]
                break
    return result

# Optimized Solution using index tracker
def next_big_element_optimized(array):
    unresolved_index_stack = []
    result = [-1] * len(array)
    for current_index in range(len(array)):
        # This is to check if current index value can resolve any unresolved indexes value
        while unresolved_index_stack and array[current_index] > array[unresolved_index_stack[-1]]:
            resolved_index = unresolved_index_stack.pop()
            result[resolved_index] = array[current_index]
        # Add current index to unresolved so that it gets resolved in next iterations
        unresolved_index_stack.append(current_index)

    return result

if __name__ == "__main__":
    input = [1,3,1,2,6,3,2,7]
    # print(next_big_element(input))
    print(next_big_element_optimized(input))