def process_list(input_list):
    if len(input_list) % 10 != 0:
      raise ValueError("The list must be a multiple of 10 in length.")

    return [num for i, num in enumerate(input_list) if (i+1) % 2 != 0 and (i+1) % 3 != 0]

try:
    input_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_list = process_list(input_list)
    print("Input List:", input_list)
    print("Modified List:", result_list)

except ValueError as e:
    print(e)
