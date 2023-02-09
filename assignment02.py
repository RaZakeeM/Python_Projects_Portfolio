'''Ra-Zakee Muhammad
02/03/2019
CSCI051P
Monday 10 am
Assignment 2'''

#This first question is a true or false question.
def true_false_question():
    Your_answer = int(input("Pomona college is named after the city Pomona, California. Enter either 1 for true or 0 for false\n\t"))
    if Your_answer == int(1):
        print("You are correct!")
        return True
    else:
        print("Sorry it's true!")
        print("Pomona college was originally located in Pomona, CA.")
        print("It was named Pomona College")
        return False
#This question is a multiple choice question that uses numbers.
def multiple_choice_question():
    Your_answer = input("How many letters are in Pomona? enter a letter a-e" + "\n" + "a) 1\n" + "b) 3\n" + "c) 4\n" + "d) 5\n" + "e) 6\n"+"\t")
    if Your_answer == str("e"):
        print("You are correct!")
        return True
    else:
        print("sorry the correct answer is e.")
        print("There are six letters in the name Pomona.")
        return False
#This question is a numeric response question.
def numeric_response_question():
    Your_answer = int(input("What is the number of Pomona college? Enter the integer you think is the number of pomona college\n\t"))
    if Your_answer == int(47):
        print("You are correct you are a true sage hen!")
        return True
    else:
        print("You are an imposter sagehen! The answer is 47!")
        return False
#This is a numeric response question
def question_4():
    Your_answer = int(input("How many undergraduate institutions are in the Claremont consortium? Enter the integer you think is the number of undergrad institutions in Claremont\n\t"))
    if Your_answer == int(5):
        print("five is the correct answer. Great job")
        return True
    else:
        print("Sorry the correct answer is 5 undergraduate colleges.")
        return False
#This is a true false question
def question_5():
    Your_answer = int(input("Pomona College is the greatest undergraduate institution in the country. Please enter either 1 for true or 0 for false\n\t"))
    if Your_answer == int(1):
        print("You are correct!\nWe are the GREATEST!")
        return True
    else:
        print("Sorry the correct answer is 1 for true.")
        print("We are the  GREATEST and that's all there is to that!")
        return False
#This is the main function and it has many purposes as it is composed of all question functions.
#In addition to composing all question functions together,
# this function translates all the boolean values stored in each of the previous functions into integers and adds all these values together.
# Then there is a conditional expression at the end of this function that prints specific strings dependent on the total score of the player.
# 4 or 5 give one message, 3 gives another, and 2, 1, or 0 give another message
def main():
    # TODO: fill in this function
    username = input("Whats your name\n")
    print("Hello, " + username)
    print("This is a little quiz about Claremont and Pomona college.")
    print("You might get the chance to prove you are a superstar of a Claremont student!")
    print("Of course that's only if you can answer these 5 questions!")
    print("Question 1:")
    Q1 = int(true_false_question())
    print("Question 2:")
    Q2 = int(multiple_choice_question())
    print("Question 3:")
    Q3 = int(numeric_response_question())
    print("Question 4:")
    Q4 = int(question_4())
    print("Question 5:")
    Q5 = int(question_5())
    Your_Score = Q1+Q2+Q3+Q4+Q5
    print("Your final score is...\n" + str(Your_Score)+"/5")
    if int(Your_Score) < 3 :
       print("Im sorry you didn't quite kill the quiz but you will always be welcome here at Pomona college!")
    elif int(Your_Score) == 3 :
        print("Not too shabby, but there is always more to learn about Pomona and the Claremont colleges!")
    else:
        print("You must be a super-student from Pomona college because you know so much")

if __name__ == "__main__":
    main()
'''The main function is called here and this is the point from which the program begins'''