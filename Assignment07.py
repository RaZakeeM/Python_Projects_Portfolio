'''Ra-Zakee Muhammad
CSCI051P
03/15/2019
Assignment 07
This is a program that introduces us to two students and compares their favorite animals
If their favorite animals are the same then an expression is printed that '''


from random import*

class Student:


    FAVORITE_ANIMAL = ("horse","giraffe","whale","tiger","mouse", "dolphin", "lion", "zebra")


    def __init__(self,name,birthday,favorite_animal,poss_pronoun = "their", subje_pronoun = "they",happy=True):
        '''This is our init function that translates parameters of class student into terms of self
        :param name: name of the student type string
        :param birthday: birthday of the student type string
        :param favorite_animal: favorite animal of the student type string
        :param poss_pronoun: possessive pronoun of the student by default "their" type string
        :param subje_pronoun : subjective pronoun of the student by default "they" type string
        :param happy: the condition of the student Type Bool
        :return: none, NoneType'''
        self.name = name
        self.b_day = birthday
        self.animal = favorite_animal
        self.sex = poss_pronoun
        self.who = subje_pronoun
        self.feel = happy




    def get_name(self):
        '''This obtains the name of the name attribute of the student
        :return self.name: name of student type string'''
        return self.name




    def get_birthday(self):
        '''This obtains the birthday attribute of the student
        :return self.b_day: birthday of the student type string'''
        return self.b_day




    def get_favorite_animal(self):
        '''This obtains the favorite animal attribute of the student
        :return self.animal: favorite animal of the student type string'''
        return self.animal




    def get_poss_pronoun(self):
        '''This obtains the possesive pronoun of the student
        :return self.sex: possessive pronoun of the student type string '''
        return self.sex




    def get_subjective_pronoun(self):
        '''This obtains the subjective pronoun of the student
        :return self.who: subjective pronoun of the student type string'''
        return self.who




    def get_feel(self):
        '''This obtains the feel attribute of the student
        :return self.feel: state of being of the student either happy or not so good type string'''
        #This is a conditional that changes the value of the feel parameter into happy or not so good as strings
        if self.feel == True:
            self.feel = "Happy!"
        else:
            self.feel = "Not so good."
        return self.feel





    def change_favorite_animal(self, times = 1, animal_color = "orange"):
        '''This changes the favorite animal attribute of a student randomly
        :return none NoneType'''
        # This is the random aspaect of the function that randomised i times

        for i in range(times):

            # it also takes into account the length of the tuple
            # at the top of the program for numeric randomization

            animal_index = randint(0,len(self.FAVORITE_ANIMAL)-1)
            self.animal = ("an " + animal_color + " " + self.FAVORITE_ANIMAL[animal_index])





    def change_feel(self):
        '''This changes the feel attribute of the student randomly
        :return none NoneType'''
        self.feel = bool(randint(0,1))
        #This is a conditional that again translates the boolean values of the feel attribute into strings
        if self.feel == True:
            self.feel = "Happy!"
        else:
            self.feel = "Not so good."





    def __str__(self):
        '''This is our string function defined such that all attributes are returned if a student object is printed
        :return all attributes in sentence type string'''
        return("This is " + self.name + " " + self.sex + " birthday is " + self.b_day + "\n"
               + self.sex + " favorite animal is " + self.animal
               + "\n Today " + self.who + " is " + str(self.feel))




def main():
    '''This is the main function that defines to objects of student class it
    shows the various attributes and redefines them again
    :return none NoneType
    '''


    student_one = Student("Michael", "02/25/2000", "cat", "his", "he")
    student_two = Student("Julia", "06/21/2000", "bear", "her", "she", False)


    #This is a for loop that tells the function to repeat all fucntionality twice
    for d in range(1,3):


        # This is the set of print statement that will be repeated twice
        print("\nThis is time " + str(d) + " that we compare the students")


        # This is the methods used to alter the animal and feeling of the student 1
        student_one.change_favorite_animal(2,"green")
        student_one.change_feel()
        print(str(student_one.get_name()) + "!")
        print(str(student_one))


        # This is the methods used to alter the animal and feeling of the student 2
        student_two.change_favorite_animal()
        student_two.change_feel()


        print(str(student_two.get_name()) + "!")
        print(str(student_two))
        # this is a conditional that prints
        # a statement if the two students have the same favorite animale
        if student_one.get_favorite_animal() == student_two.get_favorite_animal():
            print ( 40*"*")
            print ("They have the same favorite animal Today!")



if __name__ == '__main__':
    main()
