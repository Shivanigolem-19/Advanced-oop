num = int(input("Enter a number:"))

length=len(str(num))
sum=0
temp=num

while temp>0:
    digit= temp%10
    sum= sum + digit**length
    temp=temp//10

if sum ==num:
    print("It is an Armstrong")
else:
    print("It is not an Armstrong")