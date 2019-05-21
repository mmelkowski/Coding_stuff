# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:32:55 2019

@author: mmelkowski
"""

def is_div(nb_test, nb_div):
    if nb_test % nb_div == 0:
        return True
    return False

def FizzBuzzWoof(nb):
    dico_fbw = {0:"*", 3:"Fizz", 5:"Buzz", 7:"Woof"}
    
    # test if the number can be divided
    fbw_div_str = ""
    for elt in sorted(dico_fbw.keys())[1:]:
        if is_div(nb, elt):
            fbw_div_str += dico_fbw[elt]
    
    # test if the number contain values
    fbw_contain_str = ""
    for elt in str(nb):
        elt = int(elt)
        if elt in dico_fbw.keys():
            fbw_contain_str += dico_fbw[elt]
    
    # Add both
    fbw_all = fbw_div_str + fbw_contain_str
    
    # Did the number contain something except the zero?
    fbw_no_star = "".join([elt for elt in fbw_all if elt != "*"])
    
    # if yes
    if fbw_no_star != "":
        return fbw_all
    # If no
    return str(nb).replace("0","*")


if __name__ == "__main__":
    print(10, FizzBuzzWoof(10))
    print(15, FizzBuzzWoof(15))
    print(101, FizzBuzzWoof(101))
    print(30, FizzBuzzWoof(30))
    print(2535, FizzBuzzWoof(2535))
    print(3105, FizzBuzzWoof(3105))
    """
    10 => Buzz*
    15 => FizzBuzzBuzz
    101 => 1*1
    
    30 => FizzBuzzFizz*
    2535 => FizzBuzzBuzzFizzBuzz 
    3105 => FizzBuzzFizz*Buzz
    """