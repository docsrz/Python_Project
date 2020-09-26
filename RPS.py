import random 
print("Rules for RPS Game: \n" +
      "R vs P == P wins!! \n" +
      "R vs S == R Wins!! \n" +
      "P vs S == S Wins!! \n +"
      "P vs P == Equal,Play Again!! \n"
      "R vs R == Equal,Play Again!! \n"
      "S vs S == Equal,Play Again!! \n")
while True:
    print("Enter choice \n 1. R \n 2. P \n 3.S \n")
    choice=int(input("It's your turn: "))
    while choice >3 or choice <1:
        choice=int(input("Enter valid input: "))
        
        if choice==1:
            choice_name='R'
        elif choice==2:
            choice_name='P'
        else:
            choice_name='s'
        print("User choice is:"+ choice_name)
        print("\n Computer's turn.......")
        comp_choice=random.randint(1,3)
        
        while comp_choice==choice: 
            comp_choice=random.randint(1,3)
            
        if comp_choice==1:
            comp_choice_name =='R'
        elif comp_name==2:
            comp_choice_name =='P'
        else:
            comp_choice_name =='S'
        print("comp_choice is:" + comp_choice_name)
        print(choice_name + "vs" + comp_choice_name)
        
        if((choice==1 and comp_choice==2) or
            (choice==2 and comp_choice==1)):
            print("P Wins =>", end = " ")
            result="P"
        elif((choice==1 and comp_choice==3) or
             (choice==3 and comp_choice==1)):
            print("R Wins =>", end=" ")
            result="R"
        elif((choice==2 and comp_choice==3) or
             (choice==3 and comp_choice==2)):
            print("S Wins =>", end=" ")
            result="S"
        else:
            print("The game is tie!!", end=" ")
            
        if result==choice_name:
            print("<==User Wins ==>")
        else:
            print("<==Computer Wins ==>")
            
        print("You wanna play again?")
        ans=input()
        
        if ans =='n' or ans=='N':
            break
            
    print("Hope you enjoyed the game!!")
    
        
            
