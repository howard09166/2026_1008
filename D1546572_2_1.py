A = int(input())
B = int(input())

if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("輸入錯誤")
else:
    # OR：至少一個是 1
    if A == 1 or B == 1:
        or_result = 1
    else:
        or_result = 0

    # AND：兩個都是 1
    if A == 1 and B == 1:
        and_result = 1
    else:
        and_result = 0

    # XOR：兩個不同
    if A != B:
        xor_result = 1
    else:
        xor_result = 0

    print(f"OR={or_result}")
    print(f"AND={and_result}")
    print(f"XOR={xor_result}")