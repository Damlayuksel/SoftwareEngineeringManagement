
grades={"Ali":[70,80],"Ayşe":[90,100]}


results={}

def convert(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"
    

for names,scores in grades.items():
    midterm=scores[0]
    final=scores[1]
    average=0.4* midterm + 0.6* final
    tgrade=convert(average)
    outputlist=[midterm,final,tgrade,average]

    results[names]=outputlist

print(results)