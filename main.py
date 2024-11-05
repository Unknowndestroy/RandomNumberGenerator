import random
import time
import sys
from colorama import Fore, Style, init
init()

# for slow printing
def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

# Function to set the number changing rapidly for 5 seconds (all digits at once)
def rapid_number_animation(target_number, duration=5):
    start_time = time.time()
    length = len(str(target_number))
    while time.time() - start_time < duration:
        # Generate and print a random number with the same number of digits as the target number
        current_display = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        sys.stdout.write("\r" + Fore.CYAN + current_display + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.0001)  # Fast sleep for rapid changing effect
    sys.stdout.write("\r" + Fore.GREEN + str(target_number) + Style.RESET_ALL + "\n\n")  # Display the true number with newline
    sys.stdout.flush()  

# Function to animate digits one by one for numbers with lowwer than 5 digits
def animate_digits_one_by_one(number):
    digits = list(str(number))
    length = len(digits)
    for i in range(length):
        random_digit = str(random.randint(0, 9))  # Start with a random digit
        for _ in range(5000):  # Animate the digit 5 times before showing the real one
            sys.stdout.write("\r" + Fore.CYAN + ''.join(digits[:i]) + random_digit + ''.join(digits[i + 1:]) + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.001)  # Fast sleep for rapid changing effect
            random_digit = str(random.randint(0, 9))  # Change the random digit
        sys.stdout.write("\r" + Fore.GREEN + ''.join(digits[:i]) + digits[i] + ''.join(digits[i + 1:]) + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)  # Small delay after revealing each digit
    print()  # Add a newline

# Main function to generate the random number and handle animation
def generate_random_number(num_digits):
    if num_digits < 1:
        print("Number of digits must be at least 1.")
        return

    # Generate a random number with the specified number of digits
    lower_bound = 10**(num_digits - 1)  # Minimum value for specified number of digits
    upper_bound = 10**num_digits - 1      # Maximum value for specified number of digits
    number = random.randint(lower_bound, upper_bound)

    # Create a colorful msg
    colorful_message = f"{Fore.YELLOW}Generating a random {Fore.CYAN}{num_digits}{Fore.YELLOW}-digit number...{Style.RESET_ALL}"
    slow_print(colorful_message, delay=0.05)

    # If the number has 5 digits or more, animate all digits at once
    if num_digits >= 5:
        rapid_number_animation(number)
    else:
        animate_digits_one_by_one(number)

# Main loop to keep the program running and allow multiple req
while True:
    # Create a colored input
    input_prompt = f"{Fore.MAGENTA}Enter the number of digits for the random number (or 0 to exit): {Style.RESET_ALL}"
    try:
        num_digits = int(input(input_prompt))
        if num_digits == 0:
            print("Exiting the program.")
            break
        generate_random_number(num_digits)
    except ValueError:
        print("Please enter a valid integer.")
