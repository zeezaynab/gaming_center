#MATH QUIZ:
import random
def math_quiz():
 score=0
 choice=input("are you ready to start this game?\n(yes-no)?").lower()
 for i in range(10):
    num1=random.randint(0,11)
    num2=random.randint(0,num1)
    if choice=="yes":
        answer=num1-num2
        ans=int(input(f"what is {num1}-{num2}? "))
        if answer==ans:
           score+=1
        else:
           print(f"uh oh the correct answer was {answer}")
    else:
       print("exiting game.")
       break
 print(f"you have scored {score}/10.")
 if score>8:
    print("sir einstien is that you?")
 if 5<score<8:
    print("a little more practice and you'll be the next big math whiz!")
 if score==5:
    print("if you can pass it,with a little more effort you'll smash it!")
 if score<5:
    print("mate have you not been studying?")

#HARRY POTTER:
def harry_potter():
   score=0
   print("Welcome to the harry potter personality quiz!\nlets get started :D")
   answer1=int(input("\nQ1)which hogwarts house would you like to be sorted into?\n1.Gryffindor\n2.Slytherin\n3.Hufflepuff\n4.Ravenclaw\nEnter your choice :"))
   if answer1==1:
      score+=1
   answer2=int(input("\nQ2)Which magical creature fascinates you the most?\n1.Dragon\n2.Phoenix\n3.Hippogriff\n4.Centaur\nEnter your choice :"))
   if answer2==4:
      score+=1
   answer3=int(input("\nQ3)Which spell would you use the most?\n1.Expelliarmus\n2.Wingardium Leviosa\n3.Avada Kedavra\n4.Accio\nEnter your choice :"))
   if answer3==2:
      score+=1
   answer4=int(input("\nQ4)What's your favorite subject at Hogwarts?\n1.Charms\n2.Potions\n3.Transfiguration\n4.Defense Against the Dark Arts\nEnter your choice :"))
   if answer4==1:
      score+=1
   answer5=int(input("\nQ5)Which magical object would you choose to have?\n1.Invisibility Cloak\n2.Time-Turner\n3.Marauder's Map\n4.Philosopher's Stone\nEnter your choice :"))
   if answer5==3:
      score+=1
   #CHARACTER DETERMINATION:
   if score==5 or score==4:
      print("\nMr Harry teach me a few spells too eh?\n")
   elif score==3:
      print("\nwell hello there miss Hermoine:)\n")
   elif score==2:
      print("\nRon Weasley what on earth are you doing here?!\n")
   elif score==1:
      print("\nyou are Draco Malfoy!\n")
   elif score==0:
      print("\nYou are Neville Longbottom!\n")

#GENERAL KNOWLEDGE QUIZ:
def g_k():
   score=0
   quiz={"question1":{"question":"Which is the largest country in the world?","answer":"Russia"},
         "question2":{"question":"What is the national game of England?","answer":"Cricket"},
         "question3":{"question":"What is the capital of Pakistan?","answer":"Islamabad"},
         "question4":{"question":"What are the people of Spain called?","answer":"Spanish"},
         "question5":{"question":"Who is the captain of the Pakistan cricket team?","answer":"Babar Azam"},
         "question6":{"question":"Where is Pearl Harbour located?","answer":"America"},
         "question7":{"question":"Which is the largest mammal on Earth?","answer":"Whale"}}
   for key,value in quiz.items():
      print(value["question"])
      ans=input("Enter your answer: ").title()
      if ans==value["answer"]:
         score+=1
      elif ans!=value["answer"]:
         print(f"the correct answer was {value['answer']}.")
   print(f"your total score is {score}/7. ")

while True:
   print("\nWelcome to the kids gaming zone:D We hope you have a blast!\n")
   print("Gaming menu: ")
   print("1.Math quiz(test how well you know your subtraction!)")
   print("2.Harry Potter Personality Quiz (Potterheads assemble!)")
   print("3.General knowledge")
   print("4.Exit")
   choice=int(input("enter a your choice(1-4): "))
   if choice==1:
      math_quiz()
   if choice==2:
      harry_potter()
   if choice==3:
      g_k()
   if choice==4:
      print("goodbye.")
      break
      
      