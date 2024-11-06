def binaryToDecimal():
    num = int(input("Enter a number between 0 and 15: "))
    
   
    if 0 <= num <= 15:
        
        binary_str = format(num, '04b')
        print(binary_str)
    else:
        print("Please enter a number between 0 and 15.")


binaryToDecimal()