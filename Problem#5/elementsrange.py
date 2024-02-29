'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    output_list = []
    output_string = ""
    for x in range(len(input_list)):
        if int(input_list[x]) >= min_val and int(input_list[x]) <= max_val:
            output_list.append(input_list[x])
    for x in range(len(output_list)):
        output_string += str(output_list[x]) + ","
    print(output_string, end='')


if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    bounds_list = user_input.split()
    min_val, max_val = int(bounds_list[0]), int(bounds_list[1])

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
