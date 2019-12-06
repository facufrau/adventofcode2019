# Find how many different passwords exists
# Rules:
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Input range 372037-905157
import time

start_time = time.time()

start_value = 372037
end_value = 905157

passwords_list = []
total_passwords = 0

# First function for checking the duplicates
def find_doubles(pswrd):
    has_double = False
    list1 = list(str(pswrd))
    
    for i in range (0,5):
        if (list1[i] == list1[i+1]):
            if(i<=3):
                if(list1[i+1]!=list1[i+2]):
                    if(i>=1):
                        if(list1[i]!=list1[i-1]):
                            has_double = True
                    else:
                        has_double = True
            else:
                if(list1[i] != list1[i-1]):
                    has_double = True
    return has_double

# Second function for checking second condition (the digits never decrease)
def find_increasing(pswrd):
    is_increasing = True
    list2 = list(str(pswrd))
    
    for i in range (0,5):
        if (list2[i]>list2[i+1]):
            is_increasing = False
            break
            
    return is_increasing
        
    
for i in range (start_value, end_value + 1):
    if find_doubles(i) and find_increasing(i):
        passwords_list.append(i)
        total_passwords = total_passwords + 1

print('TOTAL PASSWORDS =  ' + str(total_passwords))

end_time = time.time()
total_time = end_time - start_time
print('TOTAL TIME =  ' + str(total_time) + ' SECONDS')
