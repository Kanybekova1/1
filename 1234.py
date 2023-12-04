# Set the correct login and password
correct_login = "1234"
correct_password = "5678"

# Initialize attempts counter
attempts = 0

while attempts < 3:
    # Ask user for login and password
    login = input("Enter your login: ")
    password = input("Enter your password: ")

    # Check if login and password are correct
    if login == correct_login and password == correct_password:
        print("Successful login!")
        break  # Stop the loop if login is successful
    else:
        print("Incorrect login or password. Please try again.")
        attempts += 1

# If user exceeds the maximum attempts
if attempts == 3:
    print("You've exceeded the maximum number of attempts.")
    # Optional: Wait for 5 seconds before allowing new attempts
    import time
    time.sleep(5)
