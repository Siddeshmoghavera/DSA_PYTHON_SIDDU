def reverse_number(n: int) -> int:
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev


num = int(input("Enter number: "))
print("Reversed:", reverse_number(num))


#with slicing 
# num = input("Enter a number: ")

# reverse = num[::-1]   # reverse the number

# if num == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")
