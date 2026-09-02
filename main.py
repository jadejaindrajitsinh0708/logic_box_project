print("wellcome to pattern and range analyzer")
print()

while True :

        print("select an option from below")
        print("1.pattern")
        print("2.range analyzer")
        print("3.exit")

        choice = input("select number :")

        if choice == "1":
            number = int(input("enter the number :"))  
            for i in range(1,number+1):
                for j in range(1,i+1):
                    print("*",end="")
                print()
            print()
            
        elif choice == "2":
            sum=0
            start = int(input("enter a number of rows :"))
            end = int(input("enter a number of rows :"))

            for i in range(start,end+1):
                if i % 2 == 0 :
                    print(f"the number is {i} even")
                else:
                    print(f"the number is {i} odd")
                sum=sum+i
            print(f"sum of number is {sum}")
            print()

          
        elif choice == "3":
            print("exiting the program. goodbye")
            break
        else : 
            print("enter valid input ")