amt=int(input("Enter the amount  "))
N100=amt//100
N50=(amt%100)//50
N10=((amt%100)%50)//10
N5=(((amt%100)%50)%10)//5
print("Number of 100 rupees notes are ",N100)
print("Number of 50 rupees notes are ",N50)
print("Number of 10 rupees notes are ",N10)
print("Number of 5 rupees notes are ",N5)
