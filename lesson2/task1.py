temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]

for i in temps:
    if i >= 20:
        print(f"{i}: warm")
    elif i <= 10:    
        print(f"{i}: cold")
    else:
        print(f"{i}: med warm")
else:
    print("bye")
    
