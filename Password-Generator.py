import random
import string
from datetime import datetime

def generate_password(length, input_data):
    """Generate a single password of the specified length using the input data."""
    characters = string.ascii_letters + string.digits + string.punctuation
    meaningful_data = ''.join(input_data)
    
    # Ensure at least one meaningful character is in the password
    password = ''.join(random.choice(meaningful_data + characters) for _ in range(length))
    
    return password

def collect_meaningful_data():
    """Collect meaningful data from the user."""
    names = input("Enter meaningful names (i.e: First/Last names, nickname, pet name, etc): ").split()
    dates_input = input("Enter meaningful dates [DAY.MONTH.YEAR] (i.e: 24.02.2002, 31.03, etc): ").split()
    numbers = input("Enter meaningful numbers (from username, current year, etc): ").split()
    locations = input("Enter meaningful locations (city of birth, residence, etc): ").split()
    misc_words = input("Enter misc words (any word you think might be of help and did not fit above): ").split()

    # Validate dates and convert them to a usable string format
    dates = []
    for date in dates_input:
        try:
            # Try different date formats
            if '.' in date:
                formats = ["%d.%m.%Y", "%d.%m"]
                for fmt in formats:
                    try:
                        parsed_date = datetime.strptime(date, fmt)
                        dates.append(parsed_date.strftime("%d%m%Y"))
                        break
                    except ValueError:
                        continue
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid date format for '{date}'. Skipping this date.")
    
    # Combine all meaningful data
    meaningful_data = names + dates + numbers + locations + misc_words
    
    return meaningful_data

def main():
    """Main function to generate multiple passwords based on user input."""
    try:
        num_passwords = int(input("Enter the number of passwords you want to generate: "))
        length = int(input("Enter the length of each password: "))
        file_name = input("Enter the name of the file to save passwords (with .txt extension): ")

        if num_passwords <= 0 or length <= 0:
            raise ValueError("Both the number of passwords and the length must be positive integers.")
        if not file_name.endswith(".txt"):
            raise ValueError("The file name must end with .txt extension.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

    input_data = collect_meaningful_data()

    with open(file_name, 'w') as file:
        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            password = generate_password(length, input_data)
            print(password)
            file.write(password + '\n')

    print(f"\nPasswords have been saved to {file_name}")

if __name__ == "__main__":
    main()
