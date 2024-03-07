from datetime import datetime


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

while True:
    # Take user input
    user_input = input("Enter your birthday (YYYY-MM-DD): ")

    # Check if the entered data is a valid date
    if is_valid_date(user_input):
        # Print the entered data
        print("Your birthday is:", user_input)

        # Calculate and print user's age
        birth_date = datetime.strptime(user_input, '%Y-%m-%d')
        current_date = datetime.now()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        print("Your age is:", age)

        # Break out of the loop if a valid date is entered
        break
    else:
        print("Invalid date format. Please enter your birthday in YYYY-MM-DD format. Try again.")
