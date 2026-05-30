def format_name():
    f_name=input("what is your first name??\n").title()
    l_name=input("what is your last name??\n").title()
    print(f"you first name is{f_name}")
    print(f"your last name is {l_name}")
    return {f_name + l_name}
format_name()