import math

targets = {
    "Amraam": [-150, 100, 5, 2370],
    "Qader": [100, -140, -2, 2130],
    "Harop": [50, -60, 3, 820],
    "Hades": [30, -50, -1, 710],
    "Kinzhal": [-400, -600, 10, 9000],
}


def calculateEDA(x,y,z):
    return math.sqrt(x**2 + y**2 + z**2)

def calculateAll(targets):
    eda_list=[]
    for missile,data in targets.items():
        x,y,z,speed=data
        distance=calculateEDA(x,y,z)
        time=int(3600000*distance/speed)
        eda_list.append((missile,time))
    return eda_list

def sortlist(eda_list):
    return sorted(eda_list,key=lambda x:x[1])


def main():
    eda_list=calculateAll(targets)
    sort_list=sortlist(eda_list)

    for missile,eda in sort_list:
        print(f"{missile}:{eda}")

if __name__=="__main__":
    main()