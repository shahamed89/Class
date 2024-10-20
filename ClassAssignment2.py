class assginment2():
    def subfields():
        lists=["Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Neural Language Processing"]
        print("Sub-fields in AI are:")
        for x in lists:
            print(x)
    def OddEven():
        num=int(input("Enter the Number:"))
        if((num%2==0)):
            print("The Given Number is Even")
        else:
            print("The Given Number is Odd")
    def Elegible():
        Name=input("Enter the Name:")
        Gender=input("Ente the Gender:")
        Age=int(input("Enter the Age:"))
        if(Gender.lower()in("male","m")):
            if(Age>=21):
                print("Your are Elegible for Marriage")
            else:
                print("Not Elegible for Marriage")
        elif(Gender.lower()in("female","f")):
            if(Age>=18):
                print("Your are Elegible for Marriage")
            else:
                print("Not Elegible for Marriage") 
        else:
            print("Input data wrong")
    def percentage():
        S1= 98
        print("Subject1 =",S1)
        S2= 87
        print("Subject2 =",S2)
        S3= 95
        print("Subject3 =",S3)
        S4= 95
        print("Subject4 =",S4)
        S5= 93
        print("Subject5 =",S5)
        add=S1+S2+S3+S4+S5
        print("Total Amount:",add)
        per=add/5
        print("Percentage:",per)
    def triangle():
        Height=32
        print("Height:",Height)
        Breadth=34
        print("Breadth:",Breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area Triangle:",(Height*Breadth)/2)
        H1=2
        print("Height1:",H1)
        H2=4
        print("Height2:",H2)
        Br=4
        print("Breadth:",Br)
        print("Perimeter formula: Height1+Height2+Breadth")
        x=H1+H2+Br
        print("Perimeter of Triangle:",x)
    