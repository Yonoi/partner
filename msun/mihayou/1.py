import math
while True:
    try:
        x0, y0, r = list(map(int, input().strip().split(' ')))
    except:
        break
    distance = sqrt(x0 ** 2 + y0 ** 2)
    perimeter = 2 * math.acos(-1) * r 
    if distance <= r:
        print("mihoyo is eaten by slime!")
    else:
        degree = math.degrees(math.asin(r / distance))
        ans = perimeter * degree * 360      
        print(round(ans, 2))  
