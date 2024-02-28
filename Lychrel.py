def reverse(num):
    # Reverses the digits of a number
    rev = 0
    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    return rev

def isPalindrome(num):
    # Checks if a number is a palindrome
    return num == reverse(num)

def findLychrel(number, max_iterations=2400):
    for i in range(max_iterations):
        number = number + reverse(number)
        if isPalindrome(number):
            return i + 1, number
    return max_iterations, number

if __name__ == "__main__":
    try:
        input_number = int(input("Enter a natural number: "))
        iterations, palindrome = findLychrel(input_number)
        
        print(f"Input number: {input_number}")
        print(f"Is Lychrel: {iterations == 240}")
        print(f"Iterations needed: {iterations}")
        print(f"Palindrome number (if found): {palindrome}")
        print(f"Last number reached: {palindrome}")
    except ValueError:
        print("Please enter a valid natural number.")