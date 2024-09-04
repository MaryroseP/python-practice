# Phone number converter

# adds or removes Philippine country code from a number that was entered

running = True

def length_check(unprocessed_number):
    if len(unprocessed_number) > 16 or len(unprocessed_number) < 11:
        print("Input invalid, try again.")
        return False
    elif len(unprocessed_number) == 0:
        print("Please enter your number")
        return False
    else:
        return unprocessed_number

def without_country_code(unprocessed_number):
    if len(unprocessed_number) == 11:
        to_country_code = unprocessed_number[1:11] # takes remaining 10 digits, remember string slicing
        processed_number = "+63" + to_country_code
    else:
        return False
    return processed_number

def with_country_code(unprocessed_number):
    no_code = ''
    for i in range(len(unprocessed_number)):
        if unprocessed_number[i] in ('-', '+'): # if it is TRUE that - and + are located in unprocessed_number
            continue
        if unprocessed_number[i].isdigit():
            no_code += unprocessed_number[i]
    if no_code:
        processed_number = "0"+ no_code[2:]
    else:
        return False
    return processed_number

    

while running:
    unprocessed_number = input("What is your phone number? \nPlease remove all spaces :")
    valid_number = length_check(unprocessed_number) # valid_number variable is a boolean value

    if valid_number:
        test1 = without_country_code(unprocessed_number)
        if test1:
            print(f"This is your number with the Philippine Country Code: {test1}")
            running = False
        elif not test1:
            break
        test2 = with_country_code(unprocessed_number)
        if test2:
            print(f"This is your number without the Philippine Country Code: {test2}")
            running = False
        elif not test1:
            break
    else:
        print("Sorry, invalid. Try again.")
        unprocessed_number