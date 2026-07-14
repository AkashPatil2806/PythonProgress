# 1. Take the raw string input and strip extra spaces
user_input = input("Enter a value: ").strip()

# 2. Check for Boolean (True/False)
if user_input in ["True", "False", "true", "false"]:
    val = user_input == "True"  # Converts string to actual True/False boolean
    print(f"You entered a Boolean! Evaluated type: {type(val)}")

# 3. Check for None
elif user_input == "None" or user_input == "":
    val = None
    print(f"You entered a NoneType! Evaluated type: {type(val)}")

# 4. Check for Integer (digits only)
elif user_input.isdigit():
    val = int(user_input)
    print(f"You entered an Integer! Evaluated type: {type(val)}")

# 5. Check for Float (contains one decimal point and digits)
elif user_input.replace('.', '', 1).isdigit() and '.' in user_input:
    val = float(user_input)
    print(f"You entered a Float! Evaluated type: {type(val)}")

# 6. Default to standard String
else:
    print(f"You entered a String! Evaluated type: {type(user_input)}")