n = int(input('Enter student count: '))
k = int(input('Enter apples count: '))
# each student will receive apples
print('Each student recieves ', k // n)
# apples rest
print('Apples rest is ', k % n)
