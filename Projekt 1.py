"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jana Balnarová
email: hara007@seznam.cz
"""

TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",

    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",

    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
]


users =  {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

sep = "-" * 40

username = input("Username:")

if username not in users:
    print("Unregistered user, terminating the program.")
    exit()
    
password = input("Password:")
if users[username] == password:
    print(sep)
    print("Hi", username, ", welcome to the app.\nWe have 3 texts to be analyzed.")
    print(sep)
else:
    print("Wrong password, terminating the program.")
    exit()

   
choosen_number = input("Enter a number btw. 1 and 3 to select:")

if not choosen_number.isdigit():
    print("You didn't enter a number, terminating the program.")
    exit()

choosen_number = int(choosen_number)
if not 1 <= choosen_number <= 3:
    print("The entered number has to be btw. 1 and 3, terminating the program.")
    exit()
else:
    print(sep)


choosen_text = TEXTS[choosen_number -1]
splited_text = choosen_text.split()
splited_text_without_marks = [word.strip(",.?!") for word in splited_text]

words_count = []
title_case_words = []
upper_case_words = []
lower_case_words = []
number_count = []

for word in splited_text_without_marks:
    if word.isalpha:
        words_count.append(word)
    if word.istitle():
        title_case_words.append(word)
    if word.isupper():
        upper_case_words.append(word)
    if word.islower():
        lower_case_words.append(word)
    if word.isnumeric():
        number_count.append(word)
number_sum = [int(number) for number in number_count]
  
print("There are", len(words_count), "words in the selected text.")
print("There are", len(title_case_words), "titlecase words.")
print("There are", len(upper_case_words), "uppercase words.")
print("There are", len(lower_case_words), "lowercase words.")
print("There are", len(number_count),"numeric strings.")
print("The sum of all the numbers is", sum(number_sum), ".")

print(sep)
print("LEN|     OCCURENCES     |NR.")
print(sep)

lenghts_of_words = [len(word) for word in splited_text_without_marks]
set_of_lenghts_of_words = set(lenghts_of_words)
number_of_occurrences = []

for number in set_of_lenghts_of_words:
    number_of_occurrences.append(lenghts_of_words.count(number))
longest_word = max(number_of_occurrences)
for num in set_of_lenghts_of_words:
    count_of_spaces = longest_word - lenghts_of_words.count(num)
    print(f"{num:>3}|{"*" * lenghts_of_words.count(num):<20}|{lenghts_of_words.count(num)}")
