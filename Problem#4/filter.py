'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def process_and_print(input_string):
    # Split into separate strings
    list_of_strings = input_string.split()

    # Convert strings to integers and filter out negative values
    input_data = []
    for x in range(len(list_of_strings)):
        if int(list_of_strings[x]) < 0:
            input_data.append(int(list_of_strings[x]))

    # Sort integers in reverse order
    input_data.sort(reverse=True)
    sorted_data = input_data
    # Print sorted integers
    output = ""
    for x in range(len(sorted_data)):
        output = str(output) + str(sorted_data[x]) + " "
    print(output, end='')

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)