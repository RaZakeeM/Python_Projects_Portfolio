#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''Ra-Zakee Muhammad

02/11/2019

CSCI051P

Monday 10 pm

Assignment 3

This assignment is a calculator program

that takes a user input of a  six

digit number and returns three valid 13 digit numbers

that satisfy the luhn algorithm'''



from random import *

def Breakup(var2):

    ''' This function takes a 12 di67git number and Breakup up the digits.

    Every other digit is doubled and if the double

    is greater than or equal to 10 the digits that make up the double are also separated

    this function returns the sum of all non-double digits with individual digits of double digits.

    : param (string) var2

    : return (integer)

    '''

    # this part of the function breaks up and doubles the individual digits of the users given number concatonated with 6 aditional numbers

    var2=int(var2)

    var3 = str(((var2) // 100000000000))

    var4 = str((2 * ((var2 % 100000000000) // 10000000000)))

    var5 = str(((var2 % 10000000000) // 1000000000))

    var6 = str((2 * ((var2 % 1000000000) // 100000000)))

    var7 = str(((var2 % 100000000) // 10000000))

    var8 = str((2 * ((var2 % 10000000) // 1000000)))

    var9 = str(((var2 % 1000000) // 100000))

    var10 = str((2 * ((var2 % 100000) // 10000)))

    var11 = str(((var2 % 10000) // 1000))

    var12 = str((2 * ((var2 % 1000) // 100)))

    var13 = str(((var2 % 100) // 10))

    var14 = str((2*((var2%10)//1)))

    # because all digits of the inital thirteen digit number are in the ones place, when doubled they can only be in the ten or ones place.

    # this part of the function breaks up doubles and singles into the digits in the ones and tens place

    # remainder find the digits in the tens place after every other digit is doubled in fro m the original number

    v3i = remainder(var3)

    v4i = remainder(var4)

    v5i = remainder(var5)

    v6i = remainder(var6)

    v7i = remainder(var7)

    v8i = remainder(var8)

    v9i = remainder(var9)

    v10i = remainder(var10)

    v11i = remainder(var11)

    v12i = remainder(var12)

    v13i = remainder(var13)

    v14i = remainder(var14)

    # trunk finds the digits in the ones place for all of var3-var14

    v3ii = trunk_division(var3)

    v4ii = trunk_division(var4)

    v5ii = trunk_division(var5)

    v6ii = trunk_division(var6)

    v7ii = trunk_division(var7)

    v8ii = trunk_division(var8)

    v9ii = trunk_division(var9)

    v10ii = trunk_division(var10)

    v11ii = trunk_division(var11)

    v12ii = trunk_division(var12)

    v13ii = trunk_division(var13)

    v14ii = trunk_division(var14)

    # sumvar(i) and sumvar(ii) simple break up the summing process to avoid long ines of code

    sumvari = v3i + v4i + v5i + v6i + v7i + v8i + v9i + v10i + v11i + v12i + v13i+v14i

    sumvarii = v3ii + v4ii + v5ii + v6ii + v7ii + v8ii + v9ii + v10ii + v11ii + v12ii + v13ii+v14ii

    sumvariii = sumvari + sumvarii

    #and we return the sum of sumvar(i) and sumvar(ii)

    return int(sumvariii)



def remainder(number):

    '''This function is simply a modulo function using the number integer

    10 in order to simplify the process and avoid mistakes

    : param integer

    : returns (integer) '''

    return int(number)%10

def trunk_division(number):

    '''this function is a truncated division

    function using the th integer 10.

    the function was created to simplify and avoid mistake

    : param integer

    : returns (integer)'''

    return int(number)//int(10)



def generate(sixdignumber):

    '''This function generates the random 6 digits of

     the thirteen digit credit card number by using

     the functions from the random module. this function also generates the last digit

     using modulo arithmetic and and subtraction there are

     additional conditions in order to avoid additional error

     concatenations that would occur with cases of the Breakup function

     summing to multiples of zero or situations where the last digit must be 8

     : param (str) sixdignumber

     : return (int) thirteen digit number'''

    # this part of the function determines 6 random integers and concatonates them with the user input

    x = randint(0, 9)

    y = randint(0, 9)

    z = randint(0, 9)

    a = randint(0, 9)

    b = randint(0, 9)

    c = randint(0, 9)

    var2 = (str(sixdignumber) + str(x) + str(y) + str(z) + str(a) + str(b) + str(c))

    #this part of the function find ths final integer of the 13 digit number by using the break up function

    last_number = int(10) - int(Breakup(var2))%int(10)

    if last_number==8:

        return int(str(var2) + "8")

    elif last_number==0:

        return int(str(var2)+"0")

    elif Breakup(var2)%10==0:

        return int(str(var2)+"0")

    else:

        return int(str(var2) + str(last_number))



def verify(thirteen_digit_number):

    '''this function is the verification function and

    it takes a 13 digit number and returns true if it satisfies the luhn algoithm

    and false otherwise.

    : param (int) thirteen digit number

    : return (bool)'''

    x=thirteen_digit_number%10

    y=thirteen_digit_number-x

    z=int(y/10)

    w=Breakup(z)

    if int(x)==int(10-w%10):

        return True

    else:

        return False





def main():

    #this function asks for user input and provides 3 possible endings to a user input that satisfy the luhn algorithm

    sixdignumber = str(input("Enter any six digit number whose first digit is not '0'\n\t"))

    print("Here are three possible 13 digit credit card numbers using your number:")

    print(generate(sixdignumber))

    print(generate(sixdignumber))

    print(generate(sixdignumber))





if __name__ == '__main__':

    main()

