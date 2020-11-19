
def show_question(quetions, options):
    result = 0
    for number in range(len(quetions)):
        print(quetions[number]['question'])
        for option in options:
            print(option, quetions[number]['options'][option])
            
        answer = input("Type the option of your answer: ")
        print("")

        if quetions[number]['options'][answer.upper()] == quetions[number]['answer']:
            print("Congratuations your answer is Correct")

            if number < len(quetions)-1:
                wishcontinue = input("Do You wish to continue?  (Y/N)")

            result = result + 1
        else:
            print("Wrong Answer! \n")
            return result

        if wishcontinue[0].lower() != "y":
            print("Thank You for Playing this game! \n")
            return result
        else:
            continue
    
    return result

options = ['A', 'B', 'C', 'D']
quetions = [{'question': 'The International Literacy Day is observed on', 'options': {'A': 'Sep 8', 'B': 'Nov 28', 'C': 'May 2', 'D': 'Sep 22'}, 'answer': 'Sep 8'},
            {'question': 'According to an idiom, shedding tears like which of these animals means to express false sadness or sympathy?', 'options': {'A': 'Geedad', 'B': 'Gharial', 'C': 'Haathi', 'D': 'Billi'}, 'answer': 'Gharial'},
            {'question': 'The festival of Nabanna is celebrated predominatly in', 'options': {'A': 'Andhra Pradesh', 'B': 'Rajasthan', 'C': 'Kamataka', 'D': 'Orissa'}, 'answer': 'Orissa'},
            {'question': 'Onam is the main festival of', 'options': {'A': 'Tamil Nadu', 'B': 'Karnataka', 'C': 'Andhra Pradesh', 'D': 'Kerala'}, 'answer': 'Kerala'},
            {'question': 'The Indian National Calendar is based on', 'options': {'A': 'Christian era', 'B': 'Saka era', 'C': 'Vikram era', 'D': 'Hijii era', }, 'answer': 'Saka era'}
]

name_of_player = input("Please enter your name: ")
print(f"hello {name_of_player} !")
docontinue = input("Do you wish to continue?  (Y/N) \n")

if docontinue[0].lower() == "y":
    print("Your First question is: \n")
    print("Your Result is: ", show_question(quetions, options))
