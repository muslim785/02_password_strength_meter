
# Password Strength Meter

## Project Overview
The **Password Strength Meter** is a Python-based tool that evaluates the strength of a user's password based on various security criteria. It checks the length, character variety (uppercase, lowercase, digits, special characters), and patterns to assess whether the password is **Weak**, **Moderate**, or **Strong**. The program also provides suggestions on how to improve weak passwords.

## Features
- **Password Evaluation**: Checks password strength based on multiple criteria such as length, character types, and common patterns.
- **User Feedback**: Provides detailed feedback on what needs improvement (e.g., uppercase, lowercase, numbers, special characters).
- **Pattern Detection**: Identifies common password patterns like "12345" and "password".
- **Consecutive Character Check**: Detects repeating or consecutive characters (e.g., "aaaa" or "1234").
- **Interactive Interface**: Allows users to input their password and see immediate results, including suggestions for stronger passwords.

## Requirements
- Python 3.x or later
- Basic text editor or IDE for editing the script (e.g., VS Code, Sublime Text, etc.)

## Installation

### 1. Clone or Download the Project

If you don't have the project on your local machine, you can clone it using `git` (or manually download it).

To clone:
```bash
https://github.com/muslim785/02_password_strength_meter.git
```

Alternatively, if you've downloaded the project as a ZIP file, extract it to your desired folder.

### 2. Install Python (if not installed)

Make sure you have Python 3.x installed. You can check by running:

```bash
python --version
```

If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/).

### 3. Navigate to the Project Folder

In your terminal or command prompt, navigate to the folder where the `Password Strength Meter.py` script is located.

```bash
cd "C:\path\to\your\project-folder"
```

### 4. Run the Script

Now you can run the Python script by using the following command:

```bash
python "Password Strength Meter.py"
```

Or, if you have multiple versions of Python installed, use:

```bash
python3 "Password Strength Meter.py"
```

### 5. Input Your Password

After running the script, you’ll be prompted to enter a password. The program will analyze your password and provide feedback on its strength.

---

## Example Output

```bash
Enter a password to check its strength (or type 'exit' to quit): MyPass123
Password Strength: Moderate
Feedback:
- Your password is moderate. It's better, but can still be improved.
- Include at least one special character (e.g., !@#$%).
- Avoid common patterns like '12345', 'password', etc.

--------------------------------------------------

Enter a password to check its strength (or type 'exit' to quit): letmein
Password Strength: Weak
Feedback:
- Password should be at least 8 characters long.
- Include at least one uppercase letter.
- Include at least one digit.
- Include at least one special character (e.g., !@#$%).
- Avoid common patterns like '12345', 'password', etc.
- Your password is weak. Consider improving it.

--------------------------------------------------
```

---

## Contributing

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or fix.
4. Make changes to the code and test.
5. Commit your changes and push them to your fork.
6. Submit a pull request.

---


