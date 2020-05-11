def three_number_sum(array, targetSum):
    array.sort()
    triplates = []
    new =[]
    for i in range(len(array) - 2):
        left_index = i + 1
        right_index = len(array) - 1
        while left_index < right_index:
            sum = array[i] + array[left_index] + array[right_index]
            if sum == targetSum:
                triplates.append(array[i])
                triplates.append(array[left_index])
                triplates.append(array[right_index])
                left_index += 1
                right_index -= 1
            elif sum < targetSum:
                left_index += 1
            elif sum > targetSum:
                right_index -= 1
    new.append(triplates)
    return new


sample_input_array = [12, 3, 1, 2, -6, 5, -8, 6]
sample_sum = 0
result = three_number_sum(sample_input_array, sample_sum)
print("The sets of triplates are: ", result)
