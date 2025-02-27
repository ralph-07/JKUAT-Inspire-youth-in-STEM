# Function to determine the grade based on the score
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 50 <= score <= 59:
        return 'E'
    elif 0 <= score <= 49:
        return 'F'
    else:
        return 'Invalid score'

# Main program
def main():
    try:
        score = int(input("Enter your exam score (0-100): "))
        grade = determine_grade(score)
        print(f"Your grade is: {grade}")
    except ValueError:
        print("Please enter a valid integer between 0 and 100.")

if __name__ == "__main__":
    main()
