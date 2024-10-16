name = input("Input your name: ")
sec = input ("Input your Section: ")

print ("Hello "+name+"!"+" Your section is "+sec)





prelims = float(input("Preliminary Period Grade: "))
if prelims > 100 or prelims < 40:
    print ("Grade input must be between the range of 40 - 100")
else:
    mid = float(input("Midterm Period Grade: "))
    if mid > 100 or mid < 40:
        print ("Grade input must be between the range of 40 - 100")
    else:
        fin = float(input("Final Period Grade: "))
        if fin > 100 or fin < 40:
            print ("Grade input must be between the range of 40 - 100")
        else:
            finalgrd=round(prelims*0.3333+mid*0.3333+fin*0.3333)
     

            if finalgrd <= 100 and finalgrd >= 99:
                print ("Final Grade:"+str(finalgrd)+" GPA: 1.00")

            elif finalgrd <= 98 and finalgrd >= 96:
                print("Final Grade:"+str(finalgrd)+" GPA: 1.25")
    
            elif finalgrd <= 95 and finalgrd >= 93:
                print("Final Grade:"+str(finalgrd)+" GPA: 1.50")

            elif finalgrd <= 92 and finalgrd >= 90:
                print("Final Grade:"+str(finalgrd)+" GPA: 1.75")
    
            elif finalgrd <= 89 and finalgrd >= 87:
                 print("Final Grade:"+str(finalgrd)+" GPA: 2.00")
     
            elif finalgrd <= 86 and finalgrd >= 84:
                print("Final Grade:"+str(finalgrd)+" GPA: 2.25")

            elif finalgrd <= 83 and finalgrd >= 81:
                print("Final Grade:"+str(finalgrd)+" GPA: 2.50")
     
            elif finalgrd <= 80 and finalgrd >= 78:
                print("Final Grade:"+str(finalgrd)+" GPA: 2.75")
     
            elif finalgrd == 77 and finalgrd >= 75:
                print("Final Grade:"+str(finalgrd)+" GPA: 3.00")
     
            elif finalgrd < 75:
                 print("Final Grade:"+str(finalgrd)+" GPA: 5.00")
     
            else:
                print("Syntax Error")