def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


a = int(input("Enter first: "))
b = int(input("Enter second: "))
print("GCD:", gcd(a, b))

# This uses Euclid’s Algorithm, running in O(log min(a,b)), 
# far faster than brute force.