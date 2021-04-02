'''
Program: Russian Language
Educational aid in learning Russian
'''

#initializing dict
# Common traits with English and Russian
rus_eng_questions = {
    "What are the six letters similar in Russian and English?\n":"a, e, m, T, o, K",
    "What are the false friends in english?\n":"B, H, p, c, y, x",
    "How many characters are in the Russian alphabet?\n":"33",
    "How many consonants are there? \n":"20",
    "How many semi-vowels are there? \n":"1",
    "How many vowels are there? \n":"10",
    "How many phonetic signs are there? \n":"2"
    }

# Russian semantics questions
rus_hist_questions={
    "Is the Russian alphabet is Cyrillic?(y/n) \n" : "y",
    "How many holy men invented the Russian language?\n": "2",
    "What were the saints name?\n": "Cyril and Methodius"
    }

# Russian language history
cyr_alpha_questions={
    "What was the name of the original alphabet that Cyril and Methodius created?\n":"Glagolitic",
    "When the Cyrillic alphabet evolved from the Glagolitic alphabet, what were the additional influence?":"Greek and Hebrew"
    }

# Russian pronunciation
rus_pron_questions={
    "Russian pronunciation depends on the stress? (y/n)\n":"y",
    "Are words of more than one syllable, the vowel stressed? (y/n)\n ":"y"
    }

# Soviet Republic questions
sov_rep_questions={
    "During the time of the USSR was the Cyrillic alphabet obligatory in all the Soviet Republics? (y/n)\n ":"y",
    "In what countries is the Cyrillic alphabet used today aside from Russia? (Hint: Four Countries)\n ":"Ukraine, Serbia, Belarus, Bulgaria"
    }

# looping through sov_rep_questiosn dict
def sov_rep():
    for sov_rep_question, answer in sov_rep_questions.items():
        user_answer = input(sov_rep_question)
        if user_answer == answer:
            print("Correct!")
        else:
            print("No, the answer is {}".format(answer))

# looping through rus_pron_questions dict
def rus_pron():
    for rus_pron_question, answer in rus_pron_questions.items():
        user_answer = input(rus_pron_question)
        if user_answer == answer:
            print("Correct!")
        else:
            print("No, the answer is {}".format(answer))

#looping through cyr_alpha_questios dict
def cyrillic_alphabet():
    for cyr_alpha_question, answer in cyr_alpha_questions.items():
        user_answer = input(cyr_alpha_question)
        if user_answer == answer:
            print("Correct!")
        else:
            print("No, the answer is {}".format(answer))

#looping through russian_lang_questions dict
def rus_hist():
    for rus_hist_question, answer in rus_hist_questions.items():
        user_answer = input(rus_hist_question)
        if user_answer == answer:
            print("Correct!")
        else:
            print("No, the answer is {}".format(answer))

#looping through rus_eng_questions dict
def rus_and_eng():
	for rus_eng_question, answer in rus_eng_questions.items():
		user_answer = input(rus_eng_question)
		if user_answer == answer:
			print("Correct!")
		else:
			print("No, the answer is {}".format(answer))

# defining the Cyrillic Alphabet
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
    module = input("Enter module to number practice: \n \n \t [1] Russian and English Comparison \n \t [2] Who created the Cyrillic Alphabet \n \t [3] Cyrillic Alphabet \n \t [4] Languages Spoken in Soviet Republic \n \t [5] Pronunciation \n \t [6] Cyrilic Alphabet + Pronunciation \n \t [q] Quit  \n>INPUT:$  ")
    if module == "1":
        rus_and_eng()
    elif module == "2":
        cyrillic_alphabet()
    elif module == "3":
        rus_pron()
    elif module == "4":
        sov_rep()
    elif module == "5":
        rus_hist()
    elif module == "6":
        cyrillic_letters()
    elif module == "q":
        exit()