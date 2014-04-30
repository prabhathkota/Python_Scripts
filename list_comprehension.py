input_arr = [2, 3, 4]
output_arr = [2*i for i in input_arr if i > 2]
print(output_arr)

input_arr = ['Mother Teresa', 'Abraham Lincoln', 'Nelson Mandela']
output_arr = ['Dear...' + i  for i in input_arr if len(i) > 5]
print(output_arr)