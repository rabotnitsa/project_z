# initializing color variables
TGREEN = '\033[32m'  # green text
TWHITE = '\033[37m'  # white text
TBLUE = '\033[34m'  # blue text
TMAGENTA = '\033[35m'  # magenta text
TPURP = '\033[1;32m'  # purple text
TRED = '\033[31m'  # red text


# defining russian and english similarities
def rus_and_eng():
    # initialize variables
    similar = "a, e, m, T, o, K"
    false = "B, H, p, c, y, x"

    # Request Input from User
    similar_a = input(TBLUE + "What are the six letters similar in Russian and English? ")
    # Control Flow
    while similar_a != similar:
        if similar_a == similar:
            print(TGREEN + "Yes")
        else:
            print(TMAGENTA + "Try again")
            sima = input(TWHITE + "Enter answer: \n \t")
    while similar_a == similar:
        print(TPURP + "Excellent job! \n")
        break

    # Request Input from User
    false_friends = input(TBLUE + "What are the 'false friends' in english? ")
    # Control Flow
    while false_friends != false:
        print(TMAGENTA + "Try again")
        false_friends = input(TWHITE + "Enter answer: \n \t")
    while false_friends == false:
        print(TPURP + "Excellent job! \n")
        break

    # Request Input from User
    thirtythree = input("How many characters are in the Russian alphabet? \n")
    # Control Flow
    if thirtythree == "33":
        print("Correct \n")
    else:
        print("Incorrect. There are 33 characters")
    const = input("How many consonants are there? \n")
    # Control Flow
    if const == "20":
        print("Correct \n")
    else:
        print("Incorrect. There are 20 consonants. \n")

    # Request Input from User
    vow = input("How many semi-vowels are there? \n")
    # Control Flow
    if vow == "1":
        print("Correct \n")
    else:
        print("Incorrect. There is 1 \n ")

    # Request Input from User
    vowe = input("How many vowels are there? \n")
    # Control Flow
    if vowe == "10":
        print("Correct \n")
    else:
        print("Incorrect. There are 10 vowels")

    # Request Input from User
    phonetic = input("How many phonetic signs are there? \n")
    # Control Flow
    if phonetic == "2":
        print("Correct \n")
    else:
        print("Incorrect. There are 2 \n")


# defining russian history
def rus_hist():
    # Request Input from User
    cyra = input(TBLUE + "\nThe Russian Alphabet is Cyrillic? (y/n) ")
    # Control Flow
    if cyra == "y":
        print(TGREEN + "This is true \n")
    else:
        print(TWHITE + "no \n")

    # Request Input from User
    saints = input("How many holy men invented Russian? ")
    # Control Flow
    if saints == "2":
        print("Correct \n")
    else:
        print("Wrong, it was two \n")

    # Request Input from User
    saints = input("What were the saints name? ")
    # Control Flow
    if saints == "Cyril and Methodius":
        print("Correct \n")
    else:
        print("False, their names were Cyril and Methodius \n")


# defining the Cyrillic alphabet history
def cyrillic_alphabet():
    # Request Input from User
    glago = input("\nWhat was the name of the original alphabet that Cyril and Methodius created? ")
    # Control Flow
    if glago == "Glagolitic":
        print("Correct \n")
    else:
        print("Incorrect. The alphabet was called Glagolitic \n ")

    # Request Input From User
    evolve = input(
        "When the Cyrillic alphabet evolved from the Glagolitic alphabet, what were the additional influences? ")
    # Control Flow
    if evolve == "Greek and Hebrew":
        print("Correct \n")
    else:
        print("Incorrect. Greek and Hebrew \n")


# defining languages spoken in the soviet republic
def sov_rep():
    # Request Input from User
    ussr = input(
        "\nDuring the time of the USSR was the Cyrillic alphabet obligatory in all the Soviet Republics? (y/n) ")
    # Control Flow
    if ussr == "y":
        print("Correct \n")
    else:
        print("Incorrect. It was obligatory in all the Soviet republics during the USSR. \n")

    # Request Input From User
    ubbs = input("In what countries is the Cyrillic alphabet used today aside from Russia? (Hint: Four Countries) ")
    # Control Flow
    if (ubbs == "Ukraine, Belarus, Bulgaria, Serbia" or ubbs == "Ukraine, Serbia, Belarus, Bulgaria"):
        print("Correct \n")
    else:
        print("Incorrect. The four countries are: Ukraine, Belarus, Bulgaria, Serbia")


# defining Russian Pronunciation
def rus_pron():
    # Request Input from User
    stress = input("\nRussian pronunciation depends on the stress? (y/n) ")
    # Control Flow
    if stress == "y":
        print("Correct \n")
    else:
        print("Incorrect. It does depend on the stress \n")

    # Request Input from user
    stressd = input(
        "Are words of more than one syllable, the vowel stressed? (y/n) ")
    # Control Flow
    if stressd == "y":
        print("Correct \n")
    else:
        print("Incorrect. It is pronounced strongly \n")


#defining the output of Cyrillic letters for learning
def cyrillic_letters():
    print("\nCyrillic Letter : Pronunciation")
    print("-------------------------------")
    cyrillic_translit = {
        '   \u0410''\u0430': 'A'' a'"       >>   stressed: 'a' in 'fat'| unstressed: 'a' in about'",
        '   \u0411''\u0431': 'B'' b' "       >>   'b' in 'bit'. Sounds like 'p' at the end of a word",
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


if __name__ == '__main__':
    module = input(
        TGREEN + "Enter the number of the module you want to practice: \n \n \t [1] Russian and English Comparison \n \t [2] Who created the Cyrillic Alphabet \n \t [3] Cyrillic Alphabet \n \t [4] Languages Spoken in Soviet Republic \n \t [5] Pronunciation \n \t [6] Cyrilic Alphabet + Pronunciation \n \t [q] Quit  \n>INPUT:$  ")
    if module == 'q':
        exit()
    elif module == '1':
        rus_and_eng()
    elif module == '2':
        rus_hist()
    elif module == '3':
        cyrillic_alphabet()
    elif module == '4':
        sov_rep()
    elif module == '5':
        rus_pron()
    elif module == '6':
        cyrillic_letters()
