def calendar(m):
    month = ["january","febuary","march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
    for i in range(0, len(month)):
        if m == month[i]:
            return i + 1

    return m + " is not a month"  

    
   
print(calendar("january"))