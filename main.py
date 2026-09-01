print("**wellcome to pattern and range analyzer**")

while True :

        print("**wellcome**")
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
         
            
        elif choice == "2":
            sum=0
            start = int(input("enter a number of rows :"))
            end = int(input("enter a number of rows :"))

            for i in range(start,end):
                if i % 2 == 0 :
                    print(f"even number {i}")
                else:
                    print(f"odd number {i}")
                sum=sum+i
            print(f"sum of number is {sum}")

          
        elif choice == "3":
            print("exit")
            break
        else : 
            print("enter valid input ")