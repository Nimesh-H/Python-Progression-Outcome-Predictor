def credit_range(credit):       #def for credit range
    check = False
    for i in range (0,130,+20): #Range of Credits
        if(credit==i):
            check = True
            break
    return check

count=0
progress=0
trailing=0
retriever=0
excluded=0
Pass_credit=0

print("This Programme Allow Staff To Predict student's Progression Outcome At The End Of Each Academic Year")
pass_credit=input("Please Press Enter To Start ") #Press enter to start
print("Welcome To The Staff Version of Student Progression Predictor Please Follow The Given Instructions")
print("If you want to creat the Histrogram of taken data Please Enter q in the enter number of credits at pass input")
while(pass_credit!="q"):
    try:
        pass_credit=input("Enter Number of Credits at Pass: ") #enter pass credits
        pass_credit=int(pass_credit)
        if(credit_range(pass_credit)==True):
            defer_credit=input("Enter Number of Credits at Defer: ") #enter defer credits
            try:
                defer_credit=int(defer_credit)
                if(credit_range(defer_credit)==True):
                    fail_credit=input("Enter Number of Credits at Fail: ") #enter fail credits
                    try:
                        fail_credit=int(fail_credit)
                        if(credit_range(fail_credit)==True):
                            total=pass_credit+defer_credit+fail_credit #check the total
                            if(total==120):
                                count+=1
                                if(pass_credit==120):
                                    print("Progress")
                                    progress+=1
                                elif(pass_credit==100):
                                    print("Progress-module trailer")
                                    trailing+=1
                                elif(pass_credit==80):
                                    print("Do not Progress-module retriever")
                                    retriever+=1
                                elif(pass_credit==60):
                                    print("Do not progress-module retriever")
                                    retriever+=1
                                elif(pass_credit==40):
                                    if(fail_credit==80):
                                        print("Exclude")
                                        excluded+=1
                                    else:
                                        print("Do not Progress-module retriever")
                                        retriever+=1
                                elif(pass_credit==20):
                                    if(fail_credit<80):
                                        print("Do not progress-module retriever")
                                        retriever+=1
                                    else:
                                        print("Exclude")
                                        excluded+=1
                                elif(pass_credit==0):
                                    if(fail_credit<80):
                                        print("Do not progress-module retriever")
                                        retriever+=1
                                    else:
                                        print("Exclude")
                                        excluded+=1
                            else:
                                print("Total incorrect")
                                print("Make Sure the Total of credits is equal to 120")
                                print("prograamme is running Please Try Again")   
                        else:
                            print("Range error")
                            print("Make Sure the inputs are in range")
                            print("prograamme is running Please Try Again")   
                    except:
                        print("Integers required")
                        print("Make Sure to use only integers as inputs")
                        print("prograamme is running Please Try Again")   
                else:
                    print("Range error")
                    print("Make Sure the inputs are in range")
                    print("prograamme is running Please Try Again")   
            except:
                print("Integers required")
                print("Make Sure to use only integers as inputs")
                print("prograamme is running Please Try Again")   
        else:
            print("Range error")
            print("Make Sure the inputs are in range")
            print("prograamme is running Please Try Again")   
    except:
        if(pass_credit!="q"):
            print("Integers required")
            print("Make Sure to use only integers as inputs")
            print("prograamme is running Please Try Again")   
                           
else:
    print("Histrogram is Generating.....")
    print()
    print()
    print()
    print("Progress \t{}: {} ". format(progress,( "*"*progress)))
    print("Trailing \t{}: {} ". format(trailing,( "*"*trailing)))
    print("Retriever \t{}: {} ". format(retriever,( "*"*retriever)))
    print("Exclude \t{}: {} ". format(excluded,( "*"*excluded)))
    print()
    print(count,"outcomes in total")
print()
print("Programme is Exiting\tThankyou....")
                

                    
