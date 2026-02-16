def is_palindrome(n: int) -> bool:
    original = n
    reverse = 0

    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n //= 10

    return original == reverse


num = int(input("Enter number: "))
print("Palindrome" if is_palindrome(num) else "Not Palindrome")
