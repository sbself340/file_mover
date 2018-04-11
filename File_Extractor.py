# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:18:20 2018

@author: BSelf
"""

import os
import pandas as pd
import shutil

def remove_trailing_slash(destination):
    if destination[-1] == '\\':
        destination = destination[:-2]
        destination = remove_trailing_slash
    return destination
        

def locations():
    parent = str(input("Address to Parent Folder: "))
    destination = str(input("Address to Destination Folder:"))
    
#    parent = r'C:\Users\BSelf\Desktop\EQT Scripts'
#    destination = r'C:\Users\BSelf\Desktop\EQT Scripts'
    return parent, destination

def choices():
    option1_text = '1 - Control by excel'
    option2_text = '2 - Contains unique value or values'
    header_text = 'Please choose one of the following:'
    choice = str(input('{}\n{}\n{}\n-----'.format(header_text,
                       option1_text,
                       option2_text)))
    if choice not in ['1', '2']:
        print('Please input a "1" or a "2" and press enter')
        choice = choices()
    return choice

def move_or_copy():
    string = str(input('If you would like to move the documents, '
                 'please type "move"\n'
                 'if you would like to copy the documents, please type "copy"'
                 '\n-----'))
    if string not in ['move', 'copy']:
        print('Please input either "move" or "copy"')
        string = move_or_copy()
    return string

def key_list():
    keylist = []
    keys = str(input("Please list characters key files contain. "
                     "If more than one, seperate by a comma then a space: "))
    if(", " in keys):
        iterations = keys.count(", ")
        iterations = iterations + 1
        for i in range(iterations):
            if("," in keys):
                num = keys.find(",")
                keylist.append(keys[:num])
                num = num + 2
                keys = str(keys[num:])
            else:
                keylist.append(keys[:num])
            
    else:
        keylist.append(keys)    
    if keys == '':
        print('You must imput at least one value.')
        keylist = key_list()
    return keylist

def find_docs(parent):
    oripathsburn = []
    for root, dirs, files in os.walk(parent):
        oripathsburn.append(root)    
    name = []
    fullname = []
    loc = []
    for i in range(len(oripathsburn)):
        os.chdir(oripathsburn[i])
        list2 = os.listdir()
        for j in range(len(list2)):
            string = list2[j]
            if('.' in string[-5:]):
                name.append(list2[j])
                leg = str(oripathsburn[i] + '\\' + list2[j])
                fullname.append(leg)
                loc.append(oripathsburn[i])
    return name, fullname, loc

def docs_to_move(name, fullname, loc, keys):
    movelist = []
    movename = []
    for j in range(len(keys)):
        for i in range(len(fullname)):
            if str(keys[j]).upper() in name[i].upper():
                movelist.append(fullname[i])
                movename.append(name[i])
    return movelist, movename
   
def rename_for_destination(movename, destination):
    for name in movename:
        name = str('{}\\{}'.format(destination,name))
    return movename

def move_docs(movename, move_list):
    for destinname, name in movename, move_list:
        shutil.move(destinname, name)

def copy_docs(movename, move_list):
    for destinname, name in movename, move_list:
        shutil.copy(destinname, name)

def no_excel(parent, destination):
    move_copy = move_or_copy()
#    move_copy = 'copy'
    keys = key_list()
    name, fullname, loc = find_docs(parent)
    move_list, movename = docs_to_move(name, fullname, loc, keys)
    movename = rename_for_destination(movename, destination)
    if move_copy == 'move':
        move_docs(movename, move_list)
    if move_copy == 'copy':
        copy_docs(movename, move_list)
    print(keys)
    





def main():
    choice = choices()
#    choice = '2'
#    print(choice)
    if choice == '2':
        parent, destination = locations()
        no_excel(parent, destination)
#    print(choice)

if __name__ == '__main__':
    main()