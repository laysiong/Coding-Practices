
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    #it will return the value but you still need to print it.
    # return also is end of a function.
    return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("angela","ANGELA")
# print(formated_string)



# def format_name_v2(f_name, l_name):
#     if f_name == "" or l_name =="":
#         return"You didn't provide  valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} /n {formated_l_name}"

# print(format_name_v2(input("What is your first name? "),input("What is your last name? ")))

def test():
    return 3

math_opt = '+'

sum_value = test()
print(sum_value + 5)