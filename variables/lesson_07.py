# Task 1
# fifth_number = input("Enter the fifth number: ")
# first_number = (int(fifth_number[-1]))+ int(fifth_number[0])+ int(fifth_number[2])
# second_number = int(fifth_number[1])+ int(fifth_number[-2])
# print(str(first_number) + str(second_number))

# Taskn 2
# n = input("Enter a number: ")
# n = int(n)
# if n % 2 == 0:
#     n = n+2
# else:
#     n = n+1
# print(n)

# Task 3
# n = int(input())
# h = (n // 3600) % 24
# m = (n % 3600) // 60
# s = n % 60
# print(f"{h}:{m:02d}:{s:02d}")

# Task 4
# h1 = int(input("Enter the hour of the first time: "))
# m1 = int(input("Enter the minute of the first time: "))
# s1 = int(input("Enter the second of the first time: "))
# h2 = int(input("Enter the hour of the second time: "))
# m2 = int(input("Enter the minute of the second time: "))
# s2 = int(input("Enter the second of the second time: "))
# total_seconds1 = h1 * 3600 + m1 * 60 + s1
# total_seconds2 = h2 * 3600 + m2 * 60 + s2
# difference = total_seconds2 - total_seconds1
# h_diff = (difference % (24 * 3600)) // 3600
# m_diff = (difference % 3600) // 60
# s_diff = difference % 60
# print(abs(difference))
# print(f"Difference: {h_diff} hours, {m_diff} minutes, {s_diff} seconds")

# Task 5
# h = int(input("Enter a height: "))
# a = 3
# b = 2
# d = ((h-a)/(a-b))+1
# print(d)

# Task 6
# n = int(input("Enter a number: "))
# n = format(n, '04d')
# d = n[::-1]
# print(int(n == d))

# Task 7
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c= (a+b+abs(a-b))//2
# d = (a+b-abs(a-b))//2
# print("Min:",d)
# print("Max:",c)

# Task 8
# a= int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print(["NO", "YES"][a % b == 0])

# Task 9
# n = int(input("Enter a number: "))
# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
# print(a + b + c + d)

# Task 10
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# max_ab = (a + b + abs(a - b)) // 2
# min_ab = (a + b - abs(a - b)) // 2
# max_abc = (max_ab + c + abs(max_ab - c)) // 2
# min_abc = (min_ab + c - abs(min_ab - c)) // 2
# mid = a + b + c - max_abc - min_abc
# print(min_abc, mid, max_abc)



# python variables/lesson_07.py