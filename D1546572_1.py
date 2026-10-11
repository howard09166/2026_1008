x = int(input())

if x < 0 or x > 15:
    print("輸入錯誤")
else:
    
    b3 = x // 8 % 2
    b2 = x // 4 % 2
    b1 = x // 2 % 2
    b0 = x % 2

    o1 = x // 8
    o0 = x % 8

    if x < 10:
        h = str(x)
    elif x == 10:
        h = "A"
    elif x == 11:
        h = "B"
    elif x == 12:
        h = "C"
    elif x == 13:
        h = "D"
    elif x == 14:
        h = "E"
    else:
        h = "F"

    print(f"二進制={b3}{b2}{b1}{b0}")
    print(f"八進制={o1}{o0}")
    print(f"十六進制={h}")