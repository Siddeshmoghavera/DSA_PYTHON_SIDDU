def count_digits(n: int) -> int:
    if n == 0:
        return 1

    count = 0
    while n:
        n //= 10
        count += 1
    return count


num = int(input("Enter number: "))
print("Digits:", count_digits(num))
