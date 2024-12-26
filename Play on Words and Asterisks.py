#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Part 1: Individual Letters "C", "A", "T", "D", "O", "G"



# Letter C

def letter_c1():
    '''
    Create a space for the asterisks, and then set a range of space to add in the asterisks.
    First create "rows" with space from 0 to 4 (5 spaces) using a for loop, and inside each "row",
    create "columns" (5). Then constrain the spaces you'd want the asterisks to be in using
    conditionals "ifs, elifs and else". Use "and" / "or" to allocate the space for asterisks.
    For all spaces allocated with asterisks. After every row is filled in, enter a new line.
    Finally return filled in 5 x 5 space with letter (Jupyter notebook uses markdown so needs print)
    '''
    c1_str = "";
    for row in range(0,5):    # 5 spaces from 0 to 4
        for column in range(0,5):    # in each row, there will be 5 spaces from 0 to 4
            if ((column > 0 and column < 5) and (row == 0 or row == 4) or
                 ((row > 0 and row < 4) and (column == 0))):
                c1_str = c1_str+"*"    # combine all the conditionals and enter "*"
            else:
                c1_str = c1_str+" "    # if not a desired location as the conditionals above, blank
        c1_str = c1_str+"\n"    # enter a new line after each row loop
    return print(c1_str, end="")    # return all 5 rows with desired asterisks and prevent from entering new line by adding end=""

letter_c1()



# Letter A

def letter_a1():
    '''
    Create a space for the asterisks, and then set a range of space to add in the asterisks.
    First create "rows" with space from 0 to 4 (5 spaces) using a for loop, and inside each "row",
    create "columns" (5). Then constrain the spaces you'd want the asterisks to be in using
    conditionals "ifs, elifs and else". Use "and" / "or" to allocate the space for asterisks.
    For all spaces allocated with asterisks. After every row is filled in, enter a new line.
    Finally return filled in 5 x 5 space with letter (Jupyter notebook uses markdown so needs print)
    '''
    a1_str = "";
    for row in range(0,5):    # 5 spaces from 0 to 4
        for column in range(0,5):    # in each row, there will be 5 spaces from 0 to 4
            if (((column == 0 or column == 4) and (row > 1 and row < 5)) or
                ((column == 1 or column == 3) and (row > 0 and row < 3)) or
                 ((column == 2 and (row == 0 or row == 2)))):
                a1_str = a1_str+"*"    # combine all the conditionals and enter "*"
            else:
                a1_str = a1_str+" "    # if not a desired location as the conditionals above, blank
        a1_str = a1_str+"\n"    # enter a new line after each row loop
    return print(a1_str, end="")    # return all 5 rows with desired asterisks and prevent from entering new line by adding end=""

letter_a1()



# Letter T

def letter_t1():
    '''
    Create a space for the asterisks, and then set a range of space to add in the asterisks.
    First create "rows" with space from 0 to 4 (5 spaces) using a for loop, and inside each "row",
    create "columns" (5). Then constrain the spaces you'd want the asterisks to be in using
    conditionals "ifs, elifs and else". Use "and" / "or" to allocate the space for asterisks.
    For all spaces allocated with asterisks. After every row is filled in, enter a new line.
    Finally return filled in 5 x 5 space with letter (Jupyter notebook uses markdown so needs print)
    '''
    t1_str = "";
    for row in range(0,5):    # 5 spaces from 0 to 4
        for column in range(0,5):    # in each row, there will be 5 spaces from 0 to 4
            if ((row == 0) or
                ((column == 2  and (row > 0 and row < 5)))):
                t1_str = t1_str+"*"    # combine all the conditionals and enter "*"
            else:
                t1_str = t1_str+" "    # if not a desired location as the conditionals above, blank
        t1_str = t1_str+"\n"    # enter a new line after each row loop
    return print(t1_str, end="")    # return all 5 rows with desired asterisks and prevent from entering new line by adding end=""

letter_t1()



# Letter D

def letter_d1():
    '''
    Create a space for the asterisks, and then set a range of space to add in the asterisks.
    First create "rows" with space from 0 to 4 (5 spaces) using a for loop, and inside each "row",
    create "columns" (5). Then constrain the spaces you'd want the asterisks to be in using
    conditionals "ifs, elifs and else". Use "and" / "or" to allocate the space for asterisks.
    For all spaces allocated with asterisks. After every row is filled in, enter a new line.
    Finally return filled in 5 x 5 space with letter (Jupyter notebook uses markdown so needs print)
    '''
    d1_str = "";
    for row in range(0,5):    # 5 spaces from 0 to 4
        for column in range(0,5):    # in each row, there will be 5 spaces from 0 to 4
            if (((row == 0 or row == 4) and (column >= 0 and column < 4)) or
               ((row > 0 and row < 4) and (column == 0 or column == 4))):
                d1_str = d1_str+"*"    # combine all the conditionals and enter "*"
            else:
                d1_str = d1_str+" "    # if not a desired location as the conditionals above, blank
        d1_str = d1_str+"\n"    # enter a new line after each row loop
    return print(d1_str, end="")    # return all 5 rows with desired asterisks and prevent from entering new line by adding end=""

letter_d1()



# Letter O

def letter_o1():
    '''
    Create a space for the asterisks, and then set a range of space to add in the asterisks.
    First create "rows" with space from 0 to 4 (5 spaces) using a for loop, and inside each "row",
    create "columns" (5). Then constrain the spaces you'd want the asterisks to be in using
    conditionals "ifs, elifs and else". Use "and" / "or" to allocate the space for asterisks.
    For all spaces allocated with asterisks. After every row is filled in, enter a new line.
    Finally return filled in 5 x 5 space with letter (Jupyter notebook uses markdown so needs print)
    '''
    o1_str = "";
    for row in range(0,5):    # 5 spaces from 0 to 4
        for column in range(0,5):    # in each row, there will be 5 spaces from 0 to 4
            if (((row == 0 or row == 4) and (column >= 1 and column < 4)) or
               ((row > 0 and row < 4) and (column == 0 or column == 4))):
                o1_str = o1_str+"*"    # combine all the conditionals and enter "*"
            else:
                o1_str = o1_str+" "    # if not a desired location as the conditionals above, blank
        o1_str = o1_str+"\n"    # enter a new line after each row loop
    return print(o1_str, end="")    # return all 5 rows with desired asterisks and prevent from entering new line by adding end=""

letter_o1()



# Letter G

def letter_g1():
    '''
    Create a space for the asterisks, and then set a range of space to add in the asterisks.
    First create "rows" with space from 0 to 4 (5 spaces) using a for loop, and inside each "row",
    create "columns" (5). Then constrain the spaces you'd want the asterisks to be in using
    conditionals "ifs, elifs and else". Use "and" / "or" to allocate the space for asterisks.
    For all spaces allocated with asterisks. After every row is filled in, enter a new line.
    Finally return filled in 5 x 5 space with letter (Jupyter notebook uses markdown so needs print)
    '''
    g1_str="";
    for row in range(0,5):    # 5 spaces from 0 to 4
        for column in range(0,5):    # in each row, there will be 5 spaces from 0 to 4
            if(((row == 0 or row == 4) and (column > 0 and column < 5)) or
              (row == 1 and column == 0) or
               (row == 2 and (column != 1)) or
               (row == 3 and (column == 0 or column == 4))):
                g1_str = g1_str+"*"    # combine all the conditionals and enter "*"
            else:
                g1_str = g1_str+" "    # if not a desired location as the conditionals above, blank
        g1_str = g1_str + "\n"    # enter a new line after each row loop
    return print(g1_str, end="")    # return all 5 rows with desired asterisks and prevent from entering new line by adding end=""

letter_g1()



# Part 2: Create a Function to Call Individual Letters on One Line



def asterisks(string_input):
    '''
    This function structures the row of a string of letters inputted, so that
    they are in one line. Each allowable letter ("C", "A", "T", "D", "O", "G")
    will be converted into a capital for the purposes of function _main_ later,
    then converted into their own asterisk patterns. To do this, each letter
    calls on modified functions of the individual letters in Part 1. They are
    "modified" because now each individual letter does not have its own 'rows'
    in a new line, however, only columns are permitted. The row is now constrained
    within this primary function to ensure one line output.
    '''
    for row in range(5):    # Structure the patterns to have 5 rows in one line
        for letter in string_input:    # Assign what happens to each 'letter' from the input
            # Each letter will be capitalised for the function _main_() later
            if letter.upper() == "C":
                letter_c(row)    # Call on function letter_c() with variable 'row' from this primary function
            elif letter.upper() == "A":
                letter_a(row)    # Call on function letter_a() with variable 'row' from this primary function
            elif letter.upper() == "T":
                letter_t(row)    # Call on function letter_t() with variable 'row' from this primary function
            elif letter.upper() == "D":
                letter_d(row)    # Call on function letter_d() with variable 'row' from this primary function
            elif letter.upper() == "O":
                letter_o(row)    # Call on function letter_o() with variable 'row' from this primary function
            elif letter.upper() == "G":
                letter_g(row)    # Call on function letter_g() with variable 'row' from this primary function
        print()    # Of course, print each letter in the same row

'''
The functions below are modified versions of the Part 1 functions.
These are the essentially the same functions, however, we remove
using the initial 'for row in range(5):' in the beginning, but
instead we call on the rows from the asterisk(string_input) row in range(5).
This allow each asterisk letters to be created within the same row.
Another modification of the function is to NOT use final line of
the original functions 'c_str = c_str + "\n"' as this will add a new line.
'''

def letter_c(row):    # This is similar to the function in Part 1
    c_str = "";    # Do not need include row in range(5) as it was constrained in the primary function asterisk(string_input)
    for column in range(5):
        if ((column > 0 and column < 5) and (row == 0 or row == 4) or
             ((row > 0 and row < 4) and (column == 0))):
            c_str = c_str+"*"
        else:
            c_str = c_str+" "
    return print(c_str, end="")    # End="" to continue next letter on the same line

def letter_a(row):    # This is similar to the function in Part 1
    a_str = "";    # Do not need include row in range(5) as it was constrained in the primary function asterisk(string_input)
    for column in range(5):
        if (((column == 0 or column == 4) and (row > 1 and row < 5)) or
            ((column == 1 or column == 3) and (row > 0 and row < 3)) or
            ((column == 2 and (row == 0 or row == 2)))):
            a_str = a_str+"*"
        else:
            a_str = a_str+" "
    return print(a_str, end="")    # End="" to continue next letter on the same line

def letter_t(row):    # This is similar to the function in Part 1
    t_str = "";    # Do not need include row in range(5) as it was constrained in the primary function asterisk(string_input)
    for column in range(5):
        if ((row == 0) or
            ((column == 2  and (row > 0 and row < 5)))):
            t_str = t_str+"*"
        else:
            t_str = t_str+" "
    return print(t_str, end="")    # End="" to continue next letter on the same line

def letter_d(row):    # This is similar to the function in Part 1
    d_str = "";    # Do not need include row in range(5) as it was constrained in the primary function asterisk(string_input)
    for column in range(5):
        if (((row == 0 or row == 4) and (column >= 0 and column < 4)) or
           ((row > 0 and row < 4) and (column == 0 or column == 4))):
            d_str = d_str+"*"
        else:
            d_str = d_str+" "
    return print(d_str, end="")    # End="" to continue next letter on the same line

def letter_o(row):    # This is similar to the function in Part 1
    o_str = "";    # Do not need include row in range(5) as it was constrained in the primary function asterisk(string_input)
    for column in range(5):
        if (((row == 0 or row == 4) and (column >= 1 and column < 4)) or
           ((row > 0 and row < 4) and (column == 0 or column == 4))):
            o_str = o_str+"*"
        else:
            o_str = o_str+" "
    return print(o_str, end="")    # End="" to continue next letter on the same line

def letter_g(row):    # This is similar to the function in Part 1
    g_str="";    # Do not need include row in range(5) as it was constrained in the primary function asterisk(string_input)
    for column in range(5):
        if(((row == 0 or row == 4) and (column > 0 and column < 5)) or
          (row == 1 and column == 0) or
           (row == 2 and (column != 1)) or
           (row == 3 and (column == 0 or column == 4))):
            g_str = g_str+"*"
        else:
            g_str = g_str+" "
    return print(g_str, end="")    # End="" to continue next letter on the same line



# Part 3: User Input Validation
# Call on this function _main_() to allow users to enter the input which will generate asterisks, satisfying all the requirements needed.



def _main_():
    '''
    This is a trick I learned from CSC 6001 using the 'set' method in Python. First, determine what
    input are "allowable" by setting only the six letters required. So this removes all possibilities
    of other types of input (integers, floats, etc.). Ensure that the letters inputted are "upper-cased"
    using .upper() method. The while loop reiterates so that users can keep on repeating entering inputs.
    If the input is anything other than C, A, T, D, O, G, then notify users that the input is not allowed.
    If input satisfies the set criteria, then the function calls on the asterisk(string_input) function.
    Finally, when input is "END" with either small or capital letters (case insensitive) then the loop
    breaks and ends user input.
    '''
    input_allowed = {"C","A","T","D","O","G"}
    while True:
        string_input = input(str("Enter string: "))    # User input will keep repeat while True
        string_input = string_input.upper()    # Upper case all letters to connect to asterisk(string_input) function
        if set(string_input) <= input_allowed:
            asterisks(string_input)    # when input is a part of the set allowed, then call on asterisk function
        elif string_input == "END":    # when input is 'end', then break the while loop and ends user input
            break
        else:    # for other types of input, notify users that their input is not allowed, and go back to entering input
            print("Input is not allowed. Use only letters: 'C', 'A' ,'T' ,'D' ,'O' , or 'G'.")

