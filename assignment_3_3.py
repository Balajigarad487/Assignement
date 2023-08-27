def count_case_characters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper_result, lower_result = count_case_characters(sample_string)

print("No. of Upper case characters:", upper_result)
print("No. of Lower case Characters:", lower_result)
