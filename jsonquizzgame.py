import requests
import json
import html
import random
end = ""
score_correct = 0
score_incorrect = 0
while end != 'quit':
    category = ['General Knowledge', 'Film','Music','Celebrity']
    difficulty = ['Easy', 'Normal','Hard']
    valid_answer = False
    c = 1
    i = 1
    gg = False
    valid = False
    for j in category:
        print(c, ':', j)
        c += 1
    while gg == False:
        cg = (input('Select category ( type only number) : '))
        try:
            cg = int(cg)
            if cg > 0 and cg < 5:
                d = 1
                for j in difficulty:
                    print(d, ':', j)
                    d += 1
                    gg = True
                while valid == False:
                    ez = (input('Select difficulty ( type only number) : '))
                    try:
                    
                        ez = int(ez)
                        if ez > 0 and ez < 4:
                            valid = True
                        else:
                            print('Invalid answer')
                    except:
                       print('Invalid answer. Pls use number onlyy')
            else:
                print('Invalid answer')
        except:
            print('Invalid answer. Pls use number only')
        
    if cg == 1:
        if ez == 1:
            url = 'https://opentdb.com/api.php?amount=1&category=9&difficulty=easy'
            
        elif ez == 2:
            url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=medium"
            
        elif ez == 3:
            url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=hard"
    elif cg == 2:
        if ez == 1:
            url = 'https://opentdb.com/api.php?amount=1&category=11&difficulty=easy'
            
        elif ez == 2:
            url = "https://opentdb.com/api.php?amount=1&category=11&difficulty=medium"
            
        elif ez == 3:
            url = "https://opentdb.com/api.php?amount=1&category=11&difficulty=hard"
    elif cg == 3:
        if ez == 1:
            url = 'https://opentdb.com/api.php?amount=1&category=12&difficulty=easy'
            
        elif ez == 2:
            url = "https://opentdb.com/api.php?amount=1&category=12&difficulty=medium"
            
        elif ez == 3:
            url = "https://opentdb.com/api.php?amount=1&category=12&difficulty=hard"
    elif cg == 4:
        if ez == 1:
            url = 'https://opentdb.com/api.php?amount=1&category=26&difficulty=easy'
            
        elif ez == 2:
            url = "https://opentdb.com/api.php?amount=1&category=26&difficulty=medium"
            
        elif ez == 3:
            url = "https://opentdb.com/api.php?amount=1&category=26&difficulty=hard"
    try:
        r = requests.get(url)
        if (r.status_code != 200):
            endGame = input("Sorry, there was a problem retrieving the question . Press enter to try again or type 'quit' to quit  the game.")
        else:
            hey = json.loads(r.text)
            question = hey['results'][0]['question']
            correct_answer = hey['results'][0]['correct_answer']
            incorrect_answers = hey['results'][0]['incorrect_answers']
            incorrect_answers.append(correct_answer)
            random.shuffle(incorrect_answers)
            print(html.unescape(question))
            for j in incorrect_answers:
                print(i, ":", html.unescape(j))
                i += 1
            while valid_answer == False:
                user_answer = input("\nType the number of the correct answer: ")
                try:
                    user_answer = int(user_answer)
                    if user_answer > len(incorrect_answers) or user_answer <= 0:
                        print("Invalid Answer")
                    else:
                        valid_answer = True
                except:
                    print("Invalid answer. Use only numbers.")
                    
            user_answer = incorrect_answers[int(user_answer)-1]

            if user_answer == correct_answer:
                print("\nCongratulations! You answered correctly! The correct answer was: " + html.unescape(correct_answer))
                score_correct += 1
            else:
                print("Sorry, " + html.unescape(user_answer) + " is incorrect. The correct answer is: " + html.unescape(correct_answer))
                score_incorrect += 1

            print("\n##########################")
            print("Your score is .........")
            print("Correct answers: " + str(score_correct))
            print("Incorrect answers: " + str(score_incorrect))
            print("##########################")

            end = input("\nPress enter to play again or type 'quit' to quit the game : ").lower()
    except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
            end = input("\nPress enter to play again or type 'quit' to quit the game : ").lower()
            

print("\nThanks for playing")
