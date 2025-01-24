def getEDAs(targetsdictionary):
    targetlist = list(targetsdictionary.keys())
    number = len(targetlist)
    edas = {}

    for item in range(0, number, 1):
        threat = targetlist[item]
        properties = targetsdictionary[threat]
        dx2 = (properties[0])**2
        dy2 = (properties[1])**2
        dz2 = (properties[2])**2
        distance = (dx2 + dy2 + dz2)**0.5
        edainmilisec = int(3600000 * distance / properties[3])  # EDA (tahmini erişim süresi) hesaplanır.
        edas[edainmilisec] = threat  # EDA değeri ile hedef adı sözlüğe eklenir.
    return edas  # Sözlük döndürülür.

def getpreferences(edasdictionary):
    preferencelist = []
    edalist = list(edasdictionary.keys())
    sortededas = sorted(edalist)  
    number = len(sortededas)

    for ndx in range(0, number, 1):
        edandx = sortededas[ndx]
        threat = edasdictionary[edandx]  
        additionalist = [threat, edandx] 
        preferencelist = preferencelist + [additionalist]
    return preferencelist

# Main Program
targets = {
    "Amraam": [-150, 100, 5, 2370],
    "Qader": [100, -140, -2, 2130],
    "Harop": [50, -60, 3, 820],
    "Hades": [30, -50, -1, 710],
    "Kinzhal": [-400, -600, 10, 9000],
}

edasvsnames = getEDAs(targets)
preferences = getpreferences(edasvsnames)

print("The Optimal Sequence of Shooting Incoming Threats =", preferences)
