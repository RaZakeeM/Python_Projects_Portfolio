#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Ra-Zakee Muhammad
05/05/2019
CSCI051
This is a program that analyzes various aspects of airbnb data files.
One function returns the pvalue and correlation coefficient for a
provided set of paired numbers from an input data set others create dictionaries
for various aspects of airbnb data and return those dictionaries'''

from scipy.stats.stats import spearmanr
import matplotlib.pyplot as plt


def price_satisfaction_helper(list_of_strings):
    '''
    This function is just a helper function to the price satisfaction function.
    it essentially takes a list of strings with commas contained in each string
    and then returns a list of lists where the sublists are the string seperated
     into element by the commas
    :param list_of_strings: Type: list a list of strings that contain commas
    :return:  Type: list x is a list of lists
    '''
    # This is the initial list that we will later return
    x = []
    # This is a for loop that splits every
    # elemtn of the parameter list into lists of strings,
    # and appends those lists to the return list
    for line in list_of_strings:
        x.append(line.split(','))
    return x



def price_satisfaction(filename):
    '''
    This function takes a csv file and opens it, assigns column tags to
    identify desired elemesnt in each line of the file, cretates a new list
    containing size 2 lists of price and overall satisfaction, it looks at every line of the
    csv file that is partitioned into the correct number of elements, and returns this list of lists
    :param filename: Type: string the name of the file that will be analyzed
    :return: return_list Type: list the list of size 2 lists
    '''
    # This is the 3 lines of code that open, read, and split by comma the first line of file
    f1 = open(filename,'r')
    header = f1.readline()
    h1 = header.split(',')
    # This is a for loop that looks through
    # the spliced elements of the header line
    # to find the indices for reviews, price, and overall satisfaction
    for i in range(len(h1)):
        if h1[i] == 'reviews':
            reviews_index = i
        elif h1[i] == 'price':
            price_index = i
        elif h1[i] == 'overall_satisfaction':
            overall_satisfaction_index =i
    # These three lines of code read the remaining lines in the file
    # line by line, and they are split by commas into a list of lisst
    parts = f1.readlines()
    list_of_lists = price_satisfaction_helper(parts)
    return_list = []
    # This is a for loop that iteratively constructs sublist using price and overall satisfaction
    # and appends that sublist to the list that will be returned
    for elem in list_of_lists:
        # This is the conditional statement that the elem in list of list must pass to be operated one
        if len(elem) == len(h1) and int(elem[reviews_index]) > 0 and elem[overall_satisfaction_index] != '':
            x = [float(elem[price_index]),float(elem[overall_satisfaction_index])]
            return_list.append(x)

    return return_list

def correlation(l):
    '''
    This function takes a list of size 2 lists and divides it into two list
    containing all of one type of sublist elements and another containing the
    other type of sublist elements. it then calls the method spearmanr on the
    two lists and returns a tuple of the correlation coefficient and p-value
    :param l:Type: list this is a list of size 2 sublists
    :return: Type: Tuple this is a tuple of the correlation
    coefficient and p-value resulting from the spearmanr method
    '''
    #These are the initial values for the lists that will be used in the spearman method
    prices = []
    satisfaction = []
    # This for loop iterates through the element in the parameter
    # list of l appending the first sub-element to prices and the second to satisfaction
    for elem in l:
        prices.append(elem[0])
        satisfaction.append(elem[1])
    # This is a call to the spearman method and a tuple of its
    # correlation coefficient and pvalue are returned
    result = spearmanr(prices, satisfaction)
    return (result.correlation,result.pvalue)




def host_listings(filename):
    '''
    This function takes a sting that is the name of a file and opens it reading line by line.
    it fist assigns column identifiers to the host id column and the room id column
    this way if a line in the csv file contains the correct number of commas then
    it will identify the proper number with the host id and room id. then it creates a dictionary
    of host id keys and room id(s) values per host. This dictionary is returned
    :param filename: Type: string this is a string that is the name of a csv file
    :return: Type: dictionary this is a dictionary of hosts where a host's rooms
    are contained in a list that is the value of each host key
    '''
    # This is the 3 lines of code that open, read, and split by comma the first line of file
    f1 = open(filename, 'r')
    header = f1.readline()
    h1 = header.split(',')
    # This is a for loop that looks through
    # the spliced elements of the header line
    # to find the indices for room id and host id
    for i in range(len(h1)):
        if h1[i] == 'host_id':
            host_id_index = i
        if h1[i] == 'room_id':
            room_id_index = i
    # These three lines of code construct a dictionary,
    # read and splice the remaining lines of the file
    d = {}
    parts = f1.readlines()
    list_of_lists = price_satisfaction_helper(parts)
    # This is a for loop either constructs a key and list value in the new dictionary
    # or adds to already present list values for the keys of this dictionary
    for elem in list_of_lists:
        # This conditional decides whether a new key should be constructed
        # or if the list value associated with the key should be appended to
        if int(elem[host_id_index]) not in d.keys():
            d[int(elem[host_id_index])] = ([int(elem[room_id_index])])
        else:
            d[int(elem[host_id_index])].append(int(elem[room_id_index]))
    return d




def nums_listings(dict):
    '''
    This function takes a dictionary of host keys and room(s) list
    values and finds the length of the value list. it constructs a
    new dictionary where the number of listings are the keys and the
    value gets iteratively added to as the function looks through
    the entered dictionary. Then it constructs a list of zeros (length as
    large as the largest key in the new dictionary) and replaces those zeros
    with the number of hosts owning the number of (index) properties from the dictionary.
    it returns the final list after all changes are made.
    :param dict: Type: dictionary this is a dictionary of host id keys and list
    values of the rooms each host owns
    :return: Type: list this is a list that provides the number of hosts per index
    (treated as the number of properties owned)
    '''
    # This is the initial value for the new dictionary of property number and number of owners
    d={}
    # This is a for loop that looks through the keys of the provided dictionary
    # creates keys that are ints of the lengths of the original dictionary's list values
    # and the values to these keys are iteratively added to as opposed to multiple keys of the same value 1
    for key in dict.keys():
        # These are the conditional statements the len(key)
        # must satisfy before being operated on in the dictionary
        if int(len(dict[key])) not in d.keys():
            d[int(len(dict[key]))] = 1
        else:
            d[int(len(dict[key]))] = d[int(len(dict[key]))]+1
    # These 3 lines of code make the keys a list and sort them as they are ints
    # It also constructs a final list that will later be returned
    unsorted_list_of_keys = list(d.keys())
    unsorted_list_of_keys.sort()
    final_list = []
    # This for loop constructs a list of zeros that amount to
    # the largest key from the new dictionary plus 1
    for i in range(unsorted_list_of_keys[-1]+1):
        final_list.append(0)
    # This for loop iterates through the indices in the final list
    # if the index is in the keys of the new dictionary then replace
    # the index's element with the value of the key in dictionary d
    for entry in range(len(final_list)):
        if entry in d.keys():
            final_list[entry] = d[entry]

    return final_list







def date_ordering_helper(filename_list):
    '''
    This takes a list of strings where each string is a name of a airbnb csv file.
    and orders the files in the list by date.
    :param filename_list: Type: list this is just a list of strings
    :return: Type: List this is just the list that was originally
    entered but the files are ordered by date
    '''
    # These are the original values for the dictionary, and 2 lists that will be used
    f1 = {}
    f2 = []
    f3 = []
    # This is a for loop that iterates through the strings of the list that was provided
    # It looks at the date changing it into a concrete integer and assigning it as the
    # value to the file strings in a new dictionary, it simultaneously appends to the list f2
    for f in filename_list:
        z = f[-14:-4]
        z = z.replace('-', '')
        f2.append(int(z))
        f1[f] = int(z)
    # This list of ints is then sorted
    f2.sort()
    # Then this for loop loops through the integers of f2
    # and each time loops through the keys of the dictionary
    # to append the strings of the files (to f3) in the order
    # that their dates appear in the list
    for num in f2:
        for key in f1.keys():
            if f1[key] == num:
                f3.append(key)
    return f3




def room_prices(filename_list,roomtype):
    '''
    This function takes a list of strings each string is the name
    of a file and for each string it opens the file then it assigns
    Room price index and Room type index to various column numbers
    from the 1st line of each file. It then proceeds to read the
    rest of the lines and partitions those lines into a list of lists.
    The function then proceeds to construct and return a dictionary where the keys
    are the Room numbers and the values are Lists of the various prices for the rooms.
    :param filename_list: Type: list list of file name strings
    :param roomtype: Type: string of room type
    :return: type: dictionary dictionary of room id and list of prices
    '''
    # These two lines of code order the list of files by date and construct a neew dictionary
    filename_list = date_ordering_helper(filename_list)
    d = {}
    # This is a for loop that opens each file, reads one line in and splits by commas into a list
    for file in filename_list:
        f1 = open(file, 'r')
        header = f1.readline()
        h1 = header.split(',')
        # This is a for loop that assigns indices to room id, price, and room type
        for i in range(len(h1)):
            # These are conditionals that allow for the variables to take the specific index values
            if h1[i] == 'room_id':
                room = i
            elif h1[i] == 'price':
                price_index = i
            elif h1[i] == 'room_type':
                room_type_index = i
        # These two lines of code read the rest of the
        # lines in the csv file and partition them by comma into list of lists
        parts = f1.readlines()
        list_of_lists = price_satisfaction_helper(parts)
        # This is a for loop that looks through each list of line
        for sperated_line in list_of_lists:
            # This is a conditional to pulls out lines that have more element
            # than necessary and are not for the specified room type
            if len(sperated_line) == len(h1) and sperated_line[room_type_index] == str(roomtype):
                    # These conditionals decide if a keys list value will be generated or added to
                    if int(sperated_line[room]) not in d.keys():
                        d[int(sperated_line[room])] = ([float(sperated_line[price_index])])
                    else:
                        d[int(sperated_line[room])].append(float(sperated_line[price_index]))
    return d

def price_change(dict):
    '''
     This function takes a dictionary iterating through the keys of
     that dictionary And for each key in that dictionary it constructs
     a 3 element tuple where the 1st element is the change in price the
     2nd element is the initial price in the 3rd element is the final price.
     These tuples are the values to the original keys from the 1st dictionary
     in a newly constructed dictionary.  From here a larger list of all changes
     is constructed and sorted from least to greatest and whatever absolute value
     of change is  Greatest, The original key associated with it will have its tuple value returned.
    :param dict: Type: dictionary dictionary of room id and list of prices
    :return: Type: tuple tuple of the greatest price change and corresponding start prices and end price
    '''
    # these are the initial values for the dictionary and list that will be used later
    d={}
    change_s = []
    # this is a for loop that for each key in the dictionary
    # takes the list value and calculates the change and genrates a new entry in our new dictionary
    #using the first dictionary's key and a tuple of change, first and last price
    for key in dict.keys():
        list = dict[key]
        change = (list[-1]-list[0])/list[0]
        d[key] = (change*100,list[0],list[-1])
    # This is a for loop that looks through the keys of our new dictionary
    # each keys vtuple value is associated with the variable room_info
    # that tuple is indexed into and the first element is appended to the changes list
    for room in d.keys():
        room_info = d[room]
        change_s.append(room_info[0])
    # The changes list is sorted by smallest to largets so that we
    # may easily find the most extrem change which will either be
    # at the left or right end of the list after sorting
    change_s.sort()
    # all three of the following conditionals are possible
    # situations comparing the right and left most element in our sorted list
    if abs(change_s[0]) > abs(change_s[-1]):
        # This for loop ike the other 2 searches through the keys of
        # our new dictionary to see if the change element in the tuple
        # is the same as the most extreme change
        for key in d.keys():
            if d[key][0] == change_s[0]:
                return d[key]
    elif abs(change_s[0]) < abs(change_s[-1]):
        for key in d.keys():
            if d[key][0] == change_s[-1]:
                return d[key]
    elif abs(change_s[0]) == abs(change_s[-1]):
        for key in d.keys():
            if d[key][0] == change_s[-1]:
                return d[key]


def main():
    '''
    This function has a list of file names, reads those named files each line by line
    creates a dictionary using host listings, creates a list from that dictionary using
    num listings then constructs a matching lengthed list of the index number in order up to
    the length of the num listings list minus 1. This function then graphs the two lists against
    one another.
    :return: Type: NoneType None
    '''
    # This is a sample list of 3 csv files from 3 very different cities in europe and america
    list_of_files = ['tomslee_airbnb_new_york_0011_2014-05-10.csv',
                     'tomslee_airbnb_barcelona_0114_2015-04-29.csv',
                     'tomslee_airbnb_berlin_0119_2015-07-04.csv']

    # This is a for loop that calls host listings, and nums listings on each of the strings in the list of files
    # it then for each file constructs a new list that will be later filled
    for file in list_of_files:
        dict1 = host_listings(file)
        list1 = nums_listings(dict1)
        num_of_properties =[]
        # This is a for loop that simply generates a list of numbers where the numbers correspond to index
        # the loop is over the length of the num_listings return list
        for i in range(len(list1)):
            num_of_properties.append(i)
        # These 3 lines of code find the name of the line that will be plotted
        name1=file.replace(file[0:15],'')
        name2 = name1.replace(name1[-19:-1],'').strip('_v')
        name3 = name2.replace('_',' ')
        # This simply plots the line using the index list and the list1 list
        plt.plot(num_of_properties,list1, label = name3)
    # These 5 lines of code customize and show the graph of the
    # data sets in the csv files at the top of the main function
    plt.legend()
    plt.ylabel('number of hosts')
    plt.xlabel('number of properties owned per host')
    plt.title('Do hosts typically have multiple listings at the same time?')
    plt.axis([1, 6, 0,9000])
    plt.show()
if __name__ == '__main__':
    main()