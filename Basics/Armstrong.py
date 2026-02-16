num = int(input("Enter a number: "))

sum = 0
temp = num
digits = len(str(num))   # count number of digits

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
