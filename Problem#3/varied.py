'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def process_input(input_string):
    # Split into separate strings
    strings_list = input_string.split()
    # Convert strings to floats
    for x in range(len(strings_list)):
        strings_list[x] = float(strings_list[x])
    # Get max and average
    max_value = max(strings_list)
    average_value = sum(strings_list) / len(strings_list)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
