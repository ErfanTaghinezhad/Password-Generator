# Password Generator

A simple Python project to generate passwords based on user inputs. This script collects meaningful data from the user, such as names, dates, numbers, locations, and miscellaneous words, and generates passwords using this information. The user can specify the number of passwords to generate and the length of each password. The generated passwords are saved to a specified text file.

## Features

- Collects meaningful data from the user to include in the passwords.
- Allows the user to specify the number of passwords to generate.
- Allows the user to specify the length of each password.
- Saves the generated passwords to a specified text file.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/password-generator.git
    ```

2. Navigate to the project directory:
    ```sh
    cd password-generator
    ```

3. Run the script:
    ```sh
    python Password-Generator.py
    ```

4. Follow the on-screen prompts:
    - Enter meaningful names (e.g., First/Last names, nickname, pet name, etc).
    - Enter meaningful dates in the format [DAY.MONTH.YEAR] (e.g., 24.02.2002, 31.03).
    - Enter meaningful numbers (e.g., from username, current year).
    - Enter meaningful locations (e.g., city of birth, residence).
    - Enter miscellaneous words (any word you think might be of help and did not fit above).
    - Enter the number of passwords you want to generate (positive integer).
    - Enter the length of each password (positive integer).
    - Enter the name of the file to save passwords (must end with .txt extension).

5. The script will generate the specified number of passwords and save them to the specified text file.

## Example

```sh
Enter meaningful names (i.e: First/Last names, nickname, pet name, etc): John Doe
Enter meaningful dates [DAY.MONTH.YEAR] (i.e: 24.02.2002, 31.03, etc): 24.02.2002
Enter meaningful numbers (from username, current year, etc): 2023 1234
Enter meaningful locations (city of birth, residence, etc): NewYork
Enter misc words (any word you think might be of help and did not fit above): password123
Enter the number of passwords you want to generate (positive integer): 5
Enter the length of each password (positive integer): 12
Enter the name of the file to save passwords (with .txt extension): passwords.txt

Generated Passwords:
4Fsa&^Jk2Doe
A@12#pwd!John
D2002K%n$1Pw
N%York&34a12
oP@^#24hn123

Passwords have been saved to passwords.txt
