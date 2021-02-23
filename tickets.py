def tickets(people):
    n25 = 0
    n50 = 0
    n100 = 0
    for person in people:
        if person == 25:
            n25 += person
        elif person == 50:
            n50 += person
            n25 -= 25
            if n25 < 0: return "NO"
        elif person == 100:
            n100 += person
            if n50 > 0 and n25 > 0:
                n50 -= 50
                n25 -= 25
            elif n50 == 0 and n25 > 50:
                n25 -= 75
            else:
                return "NO"
    return "YES"
             
            
           




print(tickets([25, 100]))