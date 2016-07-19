for x in range(0, 5):
    s = input()
    if '1' in s:
        print(abs(2-x)+abs(2-s.index('1')//2))
        break

