#!/usr/bin/env python3
import pyfiglet
from pyfiglet import Figlet
"""
Program: Russian Alphabet
Author: Taos Myers
Aid in learning Russian Language
"""
#Adding color to text
TGREEN = '\033[32m' #green text
TWHITE = '\033[37m' #white text
TBLUE = '\033[34m' # blue text
TMAGENTA='\033[35m' #magenta text
TPURP='\033[1;32m' # purple text
TRED='\033[31m' #red text

#banner
custom_fig=Figlet(font='pagga')
cust1_fig=Figlet(font='smblock')
print(custom_fig.renderText("\n \t Russian Alphabet"))
#print("\t \t \t By: Taos Myers")
print("\t \t    For Educational Purposes \n \n")

#guide for coloring characters
#\033[ escape code, this is always the same
#1=style, 1 for normal, e.g. \033[1;32;40m
#32=text color, 32 for bright green
#40m=background color


#program module
module=input(TGREEN + "Enter the number of the module you want to practice: \n \n \t [1] Russian and English Comparison \n \t [2] Who created the Cyrillic Alphabet \n \t [3] Cyrillic Alphabet \n \t [4] Languages Spoken in Soviet Republic \n \t [5] Pronunciation \n \t [6] Cyrilic Alphabet + Pronunciation \n \t [q] Quit  \n>INPUT:$  ")

#############
#Quit progrom
############
if module == 'q':

    if module == 'q':
        print(TMAGENTA + ">>Exiting Program Russian Alphabet")
#else:
#    print(TMAGENTA + ">>Invalid input: Closing Russian Alphabet")


####################
#Russian and English
####################
if module == "1":
    
    sim="a, e, m, T, o, K"
    false="B, H, p, c, y, x"

    #displays number of modules
    print(cust1_fig.renderText( "\n\n\n\n\n\nRussian and English Comparison Module: 7 Questions"))
    
    #initialized variables
    sim="a, e, m, T, o, K"
    false="B, H, p, c, y, x"

    #request input
    sima=input(TBLUE + "What are the six letters similiar in Russian and English? ")
  
    while sima != sim:
         if sima == sim:
             print (TGREEN + "Yes")
         else:
             print(TMAGENTA + "Try again")
             sima=input(TWHITE + "Enter answer: \n \t")

    while sima == sim:
        print(TPURP + "Excellent job! \n")
        break

    falsea=input(TBLUE + "What are the 'false friends' in english? ")    
    while falsea != false:
        print(TMAGENTA + "Try again")
        falsea=input(TWHITE + "Enter answer: \n \t")

    while falsea == false:
        print(TPURP + "Excellent job! \n")
        break

    thirtythre=input("How many characters are in the Russian alphabet? \n")
    if thirtythre == "33":
        print("Correct \n")
    else:
        print("Incorrect. There are 33 charcters")

    const=input("How many consonants are there? \n")
    if const=="20":
        print("Correct \n")
    else:
        print("Incorrect. There are 20 consonants. \n")

    vow=input("How many semi-vowels are there? \n")
    if vow == "1":
        print("Correct \n")
    else: 
        print("Incorrect. There is 1 \n ")

    vowe=input("How many vowels are there? \n")
    if vowe=="10":
        print("Correct \n")
    else:
        print("Incorrect. There are 10 vowels")

    phonetic=input("How many phonetic signs are there? \n")
    if phonetic == "2":
        print("Correct \n")
    else:
        print("Incorrect. There are 2 \n")
######################
#Russian history facts
######################
if module =="2":
    #displays number of modules
    print(cust1_fig.renderText("History: Four Questions"))
    
    cyra=input(TBLUE + "\n\n\n\n\nThe Russian Alphabet is Cryllic? (y/n) ")

    if cyra == "y":
        print(TGREEN + "This is true \n")
    else:
        print(TWHITE + "no \n")

    saints=input("How many holy men invented Russian? ")

    if saints == "2":
        print("Correct \n")
    else:
        print("Wrong, it was two \n")

    saints=input("What were the saints name? ")

    if saints =="Cyril and Methodius":
        print("Correct \n")
    else:
        print("False, their names were Cyril and Methodius \n")

#################            
#Cyrilic alphabet
#################
if module == "3":
    #displays number of modules
    print(cust1_fig.renderText("\n \n\n\n\nCyrilic Alphabet: 2 Questions"))
    
    glago=input("\nWhat was the name of the original alphabet that Cyril and Methodius created? ")

    if glago=="Glagolitic":
        print("Correct \n")
    else:
        print("Incorrect. The alphabet was called Glagolitic \n ")

    evolve=input("When the Cyrllic alphabet evovled from the Glagolitic alphabet, what were the additional influences? ")

    if evolve=="Greek and Hebrew":
        print("Correct \n")
    else:
        print("Incorrect. Greek and Hebrew \n")

########################################
#Languages spoke in the Soviet Republics
########################################
if module == "4":
    #displays number of modules
    print(cust1_fig.renderText("\n\n\n\n\nSoviet Republic: 2 Questions"))
    
    ussr=input("\nDuring the time of the USSR was the Cyrllic alphabet obligatory in all the Soviet Republics? (y/n) ")

    if ussr=="y":
        print("Correct \n")
    else:
        print("Incorrect. It was obligatory in all the Soviet republics during the USSR. \n")

    ubbs=input("In what countries is the Cyrillic alphabet used today aside from Russia with a few minor differences? (Hint: Four Countries) ")

    if (ubbs=="Ukraine, Belarus, Bulgaria, Serbia" or ubbs=="Ukraine, Serbia, Belarus, Bulgaria"):
        print("Correct \n")
    else:
        print("Incorrect. The four countries are: Ukraine, Belarus, Bulgaria, Serbia")

######################
#Russian Pronunciation
######################
if module == "5":

    #displays number of modules
    print(cust1_fig.renderText("Stresses in Russian: 2 Questions"))
    
    stress=input("\nRussian pronunciatoin depends on the stress? (y/n) ")
    if stress == "y":
        print("Correct \n")
    else:
        print("Incorrect. It does depend on the stress \n")

    stressd=input("In words of more than one syllable there is a stressed vowel which is pronounced more strongly than the others. (y/n) ")
    if stressed=="y":
                  print("Correct \n")
    else:
                  print("Incorrect. It is pronounced strongly \n")
    #Add wine example if it is answered in correctly
    
##################
#Cyrilic Alphabet
##################
if module == "6":
    #displays number of modules
    print(cust1_fig.renderText( "\n\n\n\n\nDisplays Cyrilic Alphabet + Pronunciation tips"))


    #cyrillic alphabet with english pronunciation
  
    print("\n \nCyrilic Letter : Pronunciation")
    print("-------------------------------")
   
    cyrillic_translit={
       '   \u0410''\u0430': 'A'' a'"       >>   stressed: 'a' in 'fat'| unstressed: 'a' in about'", 
       '   \u0411''\u0431':'B'' b' "       >>   'b' in 'bit'. Sounds like 'p' at the end of a word", 
       '   \u0412''\u0432': 'V'' v'"       >>   'v'. Sounds like 'f' atthe end of a vowel",
       '   \u0413''\u0433': 'G'' g'"       >>   'g' in 'gate'. Sounds like 'k' at the end of a word",
       '   \u0414''\u0434': 'D'' d'"       >>   'd'. Sounds like 't' at the end of a word",
       '   \u0415''\u0435': 'E'' e'"       >>   stressed: 'ye' in 'yes | unstressed: 'i' in 'bit'",
       '   \u0416''\u0436': 'Zh'' zh'"     >>   'like the 's' in 'pleasure'",
       '   \u0417''\u0437': 'Z'' z'"       >>   'z' in 'zip'. Sounds like 's' at the end of a word",
       '   \u0418''\u0438': 'I'' i'"       >>   like 'ee' in 'eel'",
       '   \u0419''\u0439': 'I'' i'"       >>   like the 'y' in 'boy'",
       '   \u041a''\u043a': 'K'' k'"       >>   'k' as in 'kill'",
       '   \u041b''\u043b': 'L'' l'"       >>   'l' as in 'ball'",
       '   \u041c''\u043c': 'M'' m'"       >>   'm' as in 'man'",
       '   \u041d''\u043d': 'N'' n'"       >>   'n' as in 'new'",
       '   \u041e''\u043e': 'O'' o'"       >>   stressed: 'o' as in 'for' | unstressed: 'a' in 'about'",
       '   \u041f''\u043f': 'P'' p'"       >>   'p' as in 'pen'",
       '   \u0420''\u0440': 'R'' r'"       >>   a rolled 'r'",
       '   \u0421''\u0441': 'S'' s'"       >>   's' as in 'sit'",
       '   \u0422''\u0442': 'T'' t'"       >>   't' as in 'pat'",
       '   \u0423''\u0443': 'U'' u'"       >>   like th e'oo' in 'zoo'",
       '   \u0424''\u0444': 'F'' f'"       >>   'f' as in 'far'",
       '   \u0425''\u0445': 'Kh'' kh'"     >>   like the 'ch' in the German 'ach' or the Scottish 'loch'",
       '   \u0426''\u0446': 'Ts'' ts'"     >>   like the 'ts' in 'hats'",
       '   \u0427''\u0447': 'Ch'' ch'"     >>   like the 'ch' in 'child'",
       '   \u0428''\u0448': 'Sh'' sh'"     >>   'sh' as in 'sheep'",
       '   \u0429''\u0449': 'Shch'' shch'" >>   long 'sch' as in 'borsch'. Try to say 'ee', keep your tongue in the same place, and say 'sh' instead",
       '   \u042a''\u044a': '"''"'"        >>   There is no equivalent in English. Start with 'i' as in 'bit', and then move your tongue lower and backwards",
       '   \u042b''\u044b': 'Y'' y'"       >>   'soft sign'. has no sound of its own. It has the effect of softeningthe preceding consonant",
       '   \u042c''\u044c': "'" "'""       >>   stressed: a hard 'e', like the 'e' in 'when | Unstressed like th e'i' in 'bit'",
       '   \u042d''\u044d': 'E'' e'"       >>   a soft 'u' like the first 'u' in 'usual'",
       '   \u042e''\u044e': 'Iu'' iu'"     >>   a soft 'u' like the first 'u' in 'usual'",
       '   \u042f''\u044f': 'Ia'' ia'"     >>   stressed: 'ya' in 'yak' | unstressed: more like the 'a' in 'about'"}

    for key in cyrillic_translit:
        print(key, ':', cyrillic_translit[key])
    print("\nCharacter Count:", len(cyrillic_translit))
