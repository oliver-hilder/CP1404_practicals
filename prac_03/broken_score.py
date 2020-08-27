import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(1, 100)
    random_result = determine_result(random_score)
    print(f"A randomly generated result produced a score of {random_score} with a result of {random_result}.")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"



main()