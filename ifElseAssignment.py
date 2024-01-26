#Author: Elijah Gonzalez
#Purpose: Students input their name and their GPA. If it meets the requirements
#to be on the Dean's list or the Honor Roll list, it tells them. 
#Variable Dictionary:
    #done: intially false, if the boolean is changed to true, the program ends.
    #nameEntry: the name is inputted then displayed, if it inputted as 'ZZZ',
    #the program ends.
    #GPAEntry: the user inputs their GPA. If it within the range of being 
    #within the Honor's Role and Dean's List, it will tell them, otherwise, it
    #will tell you you are not.
    
done = False
while done == False:
    nameEntry = input("Enter the name of the student, or 'ZZZ' to quit: ")
    if nameEntry == ("ZZZ"):
        done = True
    if nameEntry == False:
        GPAEntry = float(input("Enter the GPA of the student: "))
        if GPAEntry >= 3.5 and GPAEntry <=4 :
            print(nameEntry,"is in the Dean's List.")
        elif GPAEntry < 3.5 and GPAEntry >= 3.25:
            print(nameEntry,"is on the Honor Roll.")
        elif GPAEntry < 0 or GPAEntry > 4 :
            print("You must have have inputted something wrong, try again.")
        else:
            print("You are not on the Honor Roll or the Dean's List.")

print("End of application.")
