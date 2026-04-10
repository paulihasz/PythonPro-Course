def desc_temp(degrees):
    if degrees >= 20:
        return 'warm'
    elif degrees <= 10:    
        return 'cold'
    else:
        return 'med warm'
   
   
temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
    
for i in temps:
    print(f"{i}: {desc_temp(i)}")