# Imports and setup
import time
import os
import sys
import random

os.system("title Quiz Game By Conner By Trey")
os.system("color F0")  # white on black cmd

global ListCategoriesLeft
global ListCategories
global playercount

ListCategories  = ["Geography", # 1
                   "Music",     # 2
                   "Sports",    # 3
                   "History",   # 4
                   "Movies"]    # 5

# Geography      Questions, Answers and Responses
ListCategoryGeography  = [
                 "Where is the Mariana Trench located?",                                  # Q
                ("pacific ocean","pacific","the pacific ocean",),"The Mariana Trench is located in the Pacific Ocean.", # A&R
                 "What is the world's largest continent?",                                # Q
                ("asia",),"The world's largest continent is Asia.",                       # A&R
                 "What is the smallest country in the world?",                            # Q
                ("vatican city",),"The smallest country in the world is Vatican City."]   # A&R
# Music
ListCategoryMusic  = [
                 "Who had a No.1 hit with Ice Ice Baby?",
                ("vanilla ice",), "The No.1 hit with Ice Ice Baby was by Vanilla Ice.",
                 "Elvis Presely died in 1982? (True/False)",
                ("false","f",), "Elvis Presely died in 1977.",
                 "Finish the lyrics: 'I thought love was only true in _____ _____'?",
                ("fairy tales","fairytales",),"The ending to the verse is 'fairy tales'.",
                 "What popular rapper/music artist has the infamous catch-phrase 'Lets's Go'?",
                ("dababy","da baby",),"Dababy, American rapper has the infamous catch-phrase 'Let's Go'."]
# Sports
ListCategorySports  = [
                 "In order from left to right, the olympic rings are; Blue, Yellow, Green, Black, and Red? (True/False)",
                ("false","f",),"The order goes: Blue, Yellow, Black, Green, Red.",
                 "In bowling, what is the term given for three consecutive strikes?",
                ("turkey",),"The term given for three consecutive strikes is 'Turkey'.",
                 "In rowing, the 'sweeping' technique uses one oar? (True/False)",
                ("true","t",),"In rowing, the 'sweeping' technique uses one oar."]
# History
ListCategoryHistory  = [
                 "Who was the first President of the United States?",
                ("george washington",),"The first President of the United States was George Washington in 1789.",
                 "What year was the Treaty of Waitangi signed: 1920, 1880, or 1840?",
                ("1840","year 1840",),"The Treaty of Waitangi was signed in 1840.",
                 "Abraham Lincon was assassinated by Jeremy Booth? (True/False)",
                ("false","f",),"Abraham Lincon was assassinated by John Booth."]
# Movies
ListCategoryMovies  = [
                 "What year was the movie 'Forrest Gump' released?",
                ("1994",),"Forrest Gump was released in 1994.",
                 "In The Matrix, does Neo take the blue pill or the red pill?",
                ("red","red pill",),"Neo takes the red pill.",
                 "How many Marvel Avengers movies have been released?",
                ("4","four",),"There have been four Avengers movies (as of 2021)."]


# Pause function
def pause(p):
    time.sleep(p)
    #print("PAUSE")



# Questionaire
def Questionaire():
    CategorySection=0
    Category = (globals()["ListCategory"+ListCategoriesLeft[SelectedCategory-1]]).copy()
    for x in range(0,len(Category)//3):
        CategorySection += 1
        for i in range(0,playercount): # loop for all players
            os.system('cls') # clear screen
            print("Category: {}, Question {}".format(ListCategoriesLeft[SelectedCategory-1],CategorySection))
            input("Ready Player {}? [ENTER]".format(i+1)) # ready up
            os.system('cls')
            print("Category: {}, Question {}:".format(ListCategoriesLeft[SelectedCategory-1],CategorySection))
            print(Category[CategorySection*3-3]) # question
            response = input("[Player {}] > ".format(i+1))
            reach = False
            for z in range(0,len(Category[CategorySection*3-2])):
                if response.lower() in (Category[CategorySection*3-2])[z] and (Category[CategorySection*3-2])[z] in response.lower():
                    print("Correct!")
                    globals()["Score"+str(i+1)].append(1)
                    reach=True
                    break
            if reach == False:
                print("Incorrect!")
                globals()["Score"+str(i+1)].append(0)
            print(Category[CategorySection*3-1])
            #pause(p=2.5)


# Category select
def CategorySelect():
    global SelectedCategory
    while True:
        try:
            if len(ListCategoriesLeft) == len(ListCategories):
                print("Select the category to start off with:")
            else:
                print("Select the next category:")
            for i in range(0,len(ListCategoriesLeft)):
                print("{} - {}".format(i+1,ListCategories[i]))
            if len(ListCategoriesLeft) != len(ListCategories):
                print("OR Type END to finish the quiz early")
            print("Type a number corresponding to category and press [ENTER] \nOr type 0 for a random category and press [ENTER]")
            CategorySelectInput = (input())

            if CategorySelectInput.lower() == "end":
                ListCategoriesLeft.clear()
                break
            SelectedCategory = int(CategorySelectInput)

            if SelectedCategory == 0:
                SelectedCategory = random.randint(0,len(ListCategoriesLeft))
                Questionaire()
                ListCategoriesLeft.pop(SelectedCategory-1)
                break

            if SelectedCategory not in range(1,len(ListCategoriesLeft)+1):
                print("Invalid input")
                pause(p=1)
                pass

            else:
                Questionaire()
                ListCategoriesLeft.pop(SelectedCategory-1)
                break

        except:
            print("Error")
            pause(p=1)
        print(ListCategoriesLeft)
        print(ListCategories)

def ScorePrint():
    for i in range(1,playercount+1):
        for x in range(0,globals()["Score"+str(i)]):

            print(sum(globals()["Score"+str(i)]))


# Get player count
while True:
    os.system('cls') # Startup and rules
    print("Welcome to Connor's Quiz!")
    print("="*32)
    print("The rules are simple:"
          "\n - A questionaire category will first be selected and after every category."
          "\n - Players will privately answer a question until everyone has answered."
          "\n - The correct answer will be presented once a player has answered."
          "\n - Questions will cycle until the category is complete."
          "\n - A score for each player will be shown once the quiz is completed or ended."
          "\n   ENJOY!")
    print("="*32)
    pause(p=3)
    input("Press [ENTER] to start ")
    ListCategoriesLeft = ListCategories.copy()          # reset/set categoriesleft list
    while True:                                         # get valid player count
        try:
            os.system('cls')                            # clear cmd
            print("How many players? [1-8]")
            playercount = int(input())
            if playercount not in range(1,9):           # out of range error
                print("sorry, your input was invalid")
            else:
                break
        except:
            print("sorry, your input was invalid")      # error
    if playercount != 1:
        print("Okay! {} players".format(playercount))
    elif playercount == 1:
        print("Okay! {} player".format(playercount))
    for i in range(1,playercount+1):
        globals()["Score"+str(i)] = []
    pause(p=2)

    while True:
        os.system('cls')
        if len(ListCategoriesLeft) == 0:
            print("The quiz has been completed!")
            pause(p=1)
            ScorePrint()
            break
        elif len(ListCategoriesLeft) != 1:
            CategorySelect()
        elif len(ListCategoriesLeft) == 1:
            SelectedCategory = 1
            print("Last category!")
            pause(p=1)
            Questionaire()
            ListCategoriesLeft.pop(0)
    input("\nPress [ENTER] to restart")


# END OF CODE CATCH for testing
input("END OF CODE")
