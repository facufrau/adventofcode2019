# 1-Check first opcode (index 0)
# 2-Check opcode [0]
    # If opcode [0] = 1 take next 3 numbers (index 1,2,3). Sum [1]+[2] and store in [3]
    # If opcode [0] = 2 take next 3 numbers (index 1,2,3). Mult [1]*[2] and store in [3]
    # If opcode [0] = 99 stop
# 3-Jump forward 4 indexes, next opcode = [0 + 4]
# 4-Repeat until finding a [i] = 99

# intcode_test1 = [1,0,0,0,99]
# intcode_test1 = [2,3,0,3,99]
# intcode_test1 = [2,4,4,5,99,0]
# intcode_test1 = [1,1,1,4,99,5,6,0,99]

intcode_test1 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]

# Change the starting values for indexes 1 and 2 
intcode_test1[1] = 12
intcode_test1[2] = 2

for index in range (0, (len(intcode_test1)),4):

    opcode = intcode_test1[index]
    first_number = intcode_test1[intcode_test1[index + 1]]
    second_number = intcode_test1[intcode_test1[index + 2]]
    third_number = intcode_test1[index + 3]

    if (opcode == 1):
        addition = first_number + second_number
        intcode_test1[third_number] = addition
    elif (opcode == 2):
        product = first_number * second_number
        intcode_test1[third_number] = product
    elif (opcode == 99):
        break

print(intcode_test1)
print(intcode_test1[0])


    
