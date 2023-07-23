def isPalindrome(num):
    rev = 0
    initNumber = num
    while num > 0:
        r = num % 10
        num = num // 10
        rev = rev * 10 + r

    if rev == initNumber:
        print('Number is Palindrome')
    else:
        print('Not a palindrome')


isPalindrome(1221)
isPalindrome(963)
isPalindrome(333)
