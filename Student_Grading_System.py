def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Student Grading System!")
    try:
        score = float(input("Please enter the student's score (0-100): "))
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        
        grade = calculate_grade(score)
        print(f"The student's grade is: {grade}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()