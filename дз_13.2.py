num1 = int(input())
#print(str(num1))
#print(reversed(str(num1)))

def is_palindrome(num: int) -> bool:
        return str(num) == str(num)[::-1]
print(is_palindrome(num1))