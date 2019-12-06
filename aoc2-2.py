# 1-Check first opcode (index 0)
# 2-Check opcode [0]
    # If opcode [0] = 1 take next 3 numbers (index 1,2,3). Sum [1]+[2] and store in [3]
    # If opcode [0] = 2 take next 3 numbers (index 1,2,3). Mult [1]*[2] and store in [3]
    # If opcode [0] = 99 stop
# 3-Jump forward 4 indexes, next opcode = [0 + 4]
# 4-Repeat until finding a [i] = 99
# 5-Guess the 2 numbers in index 1 and 2 that make the index 0 = 19690720

intcode_raw_data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]

program_goal = 19690720

def intcode_program(noun, verb):
    intcode_data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]

    intcode_data[1] = noun
    intcode_data[2] = verb

    for index in range (0, len(intcode_data), 4):
        opcode = intcode_data[index]
        first_number = intcode_data[intcode_data[index + 1]]
        second_number = intcode_data[intcode_data[index + 2]]
        third_number = intcode_data[index + 3]

        if (opcode == 1):
            addition = first_number + second_number
            intcode_data[third_number] = addition
        elif (opcode == 2):
            product = first_number * second_number
            intcode_data[third_number] = product
        elif (opcode == 99):
            break
    return (intcode_data[0])

# test_case = intcode_program(12,2)    

for i in range (0,100):
   for j in range (0,100):
       program_result = intcode_program(i,j)
       if program_result == program_goal:
           goal_noun = i
           goal_verb = j
       else:
           continue

print('The goal noun is... ')
print(goal_noun)
print('The goal verb is...')
print(goal_verb)
output_goal = 100 * goal_noun + goal_verb
print('The output goal is...')
print(output_goal)
