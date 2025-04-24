import re

def password_strength(password):
    # Initialize the strength score and feedback list
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%).")
    
    # Check for common patterns (e.g., "12345", "password")
    common_patterns = ['12345', 'password', 'qwerty', 'letmein']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        feedback.append("Avoid common patterns like '12345', 'password', etc.")

    # Check for consecutive characters (e.g., "abcd", "1111")
    if re.search(r'(.)\1\1', password):  # checks for three consecutive repeating characters
        score -= 1
        feedback.append("Avoid consecutive characters or numbers like 'aaa', '111', etc.")
    
    # Evaluate the strength based on the score
    if score <= 2:
        strength = "Weak"
        feedback.append("Your password is weak. Consider improving it.")
    elif score == 3 or score == 4:
        strength = "Moderate"
        feedback.append("Your password is moderate. It's better, but can still be improved.")
    else:
        strength = "Strong"
        feedback.append("Your password is strong! Keep it up.")

    return strength, feedback

def main():
    print("Welcome to the Password Strength Meter!")
    
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("Exiting the program. Stay secure!")
            break
        
        strength, feedback = password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
