grades = [
    ["Alice", 75, 85],
    ["Bob", 80, 90],
    ["Charlie", 70, 65]
]



def convert(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    

results={}
nof_students=len(grades)

for index in range(0,nof_students):

    listx=grades[index]

    name=listx[0]
    midterm=listx[1]
    final=listx[2]

    average=midterm*0.4 + final*0.6

    tgrade=convert(average)

    listz=[midterm,final,average,tgrade]

    results[name]=listz


for name in results:
    print(f"Results Dictionary for {name}: ", results[name])

