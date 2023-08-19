# 1から100までの数字を取り出し、3の倍数の場合はFizzを、5の倍数の場合はBuzz、3と5の倍数の場合はFizzBuzzを出力する

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)