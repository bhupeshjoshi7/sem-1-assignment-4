import random
for i in range(1,11):
    a = random.randint(1,10)
    b = random.randint(1,10)
    res = a*b
    print("Question",i,":",a,"x",b) 
    resin = int(input("Enter your answer :"))
    
    if resin==res:
        print("Right!")
        
    else :
        print("Wrong", "The right ans is",res) 
         