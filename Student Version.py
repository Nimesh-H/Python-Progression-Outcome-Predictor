

def credit_range(credit):
    check = False
    for i in range (0,130,+20): #Range of Credits
        if(credit==i):
            check = True
            break
    return check

print("This Programme Allow Students To Predict Thier Progression Outcome At The End Of Each Academic Year")
decision=input("Please Press Enter To Start The Programme ") #Press enter to start
print("Welcome To The Student Progression Predictor Please Follow The Given Instructions")
while decision=="":
    try:
        pass_credit=input("Enter Number of Credits at Pass: ") #Enter pass credits
        pass_credit=int(pass_credit)
        if(credit_range(pass_credit)==True):
            defer_credit=input("Enter Number of Credits at Defer: ") #Enter defer credits
            try:
                defer_credit=int(defer_credit)
                if(credit_range(defer_credit)==True):
                    fail_credit=input("Enter Number of Credits at Fail: ") #Enter fail credits
                    try:
                        fail_credit=int(fail_credit)
                        if(credit_range(fail_credit)==True):
                            total=pass_credit+defer_credit+fail_credit #Check the total
                            if(total==120):
                                if(pass_credit==120):
                                    print("Progress")
                                elif(pass_credit==100):
                                    print("Progress-module trailer")
                                elif(pass_credit==80):
                                    print("Do not Progress-module retriever")
                                elif(pass_credit==60):
                                    print("Do not progress-module retriever")
                                    
                                elif(pass_credit==40):
                                    if(fail_credit==80):
                                        print("Exclude")
                                    else:
                                        print("Do not Progress-module retriever")
                                elif(pass_credit==20):
                                    if(fail_credit<80):
                                        print("Do not progress-module retriever")
                                    else:
                                        print("Exclude")
                                elif(pass_credit==0):
                                    if(fail_credit<80):
                                        print("Do not progress-module retriever")
                                    else:
                                        print("Exclude")
                            else:
                                print("Total incorrect")
                                print("Make Sure the Total of credits is equal to 120")
                                continue
                        else:
                            print("Range error")
                            print("Make Sure the inputs are in range")
                            continue
                    except:
                        print("Integers required")
                        print("Make Sure to use only integers as inputs")
                        continue
                else:
                    print("Range error")
                    print("Make Sure the inputs are in range")
                    continue
            except:
                print("Integers required")
                print("Make Sure to use only integers as inputs")
                continue
        else:
            print("Range error")
            print("Make Sure the inputs are in range")
            continue
    except:
        print("Integers required")
        print("Make Sure to use only integers as inputs")
        continue
    decision=input("Please Press Enter To try again or type stop to exit ")
    if decision=="stop":
        break
print("Programme is Exiting\tThankyou....")

                   

