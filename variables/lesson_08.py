# Task 1
# n = int(input("Enter a number: "))
# m = int(input("Enter another number: "))
# print([n//m, ((n//m)+1)][n % m != 0])

# Task 2
# n = int(input())

# p1 = "   _~_   "
# p2 = "  (o o)  "
# p3 = " /  V  \\ "
# p4 = "/(  _  )\\"
# p5 = "  ^^ ^^  "

# print((p1 + "   ") * n)
# print((p2 + "   ") * n)
# print((p3 + "   ") * n)
# print((p4 + "   ") * n)
# print((p5 + "   ") * n)

# Task 3
# lesson = int(input("Enter a lesson number: "))
# start_minute = 9*60
# duration = 45
# break_time = 5*(lesson//2)+15*((lesson-1)//2)
# total_minutes = start_minute + lesson*duration + break_time
# hours = total_minutes // 60
# minutes = total_minutes % 60
# print(f"{hours:02d}:{minutes:02d}")

# Task 4
# x1= int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# a1 = int(input("Enter a1: "))
# b1 = int(input("Enter b1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))

# t1 = x1 * 60 + y1
# r1 = a1 * 60 + b1
# t2 = x2 * 60 + y2

# dt = (t2 - t1 + 24*60) % (24*60)
# dr = dt*2

# r2 = (r1 + dr) % (24*60)
# a2 = r2 // 60   
# b2 = r2 % 60

# print(f"{a2:02d}:{b2:02d}")

# Task 5
# n=float(input("Enter a number: "))
# m = n-int(n)
# m = int(m*10)
# print(m)

# Task 6
# hour = int(input("Enter hours: "))
# minute = int(input("Enter minutes: "))
# second = int(input("Enter seconds: "))
# angle = (hour % 12) * 30 + minute * 0.5 + second * (0.5/60)
# print(f"Angle: {angle} degrees")

# Task 7
# angle = int(input("Enter an angle: "))
# minute = (angle % 30) * 2
# minute_angle = minute/5*30
# print(f"Minute arrow: {minute} minutes")
# print(f"Angle: {minute_angle} degrees")

# Task 8
# n = int(input("Enter a number: "))
# m = int(input("Enter another number: "))
# x = (m*n)//(m-1)
# y = x//m
# print(x, y)

# Task 9
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter a third number: "))
# d = (a//c)*(b//c)
# print(d)

# Task 10
# k= int(input("Enter a amount of strings: "))
# n=int(input("Enter a number of pages: "))
# print([(n//k)+1, n//k][n % k == 0])
# print([n-k, n][n<=k])

# Task 11
# n = int(input("Enter a number: "))
# a = n//500
# b = n%500
# c = b//100
# d = b%100
# e = d//10
# f = d%10
# g = f//5
# h = f%5
# l=h//2
# print(f"500: {a}")
# print(f"100: {c}")
# print(f"10: {e}")
# print(f"5: {g}")
# print(f"2: {l}")

# python variables/lesson_08.py