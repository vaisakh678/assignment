hash = {
    "TOI":[3,3,3,3,3,5,6],
    "Hindu":[2.5,2.5,2.5,2.5,2.5,4,4],
    "ET":[4,4,4,4,4,4,10],
    "BM":[1.5,1.5,1.5,1.5,1.5,1.5,1.5],
    "HT":[2,2,2,2,2,4,4]
}

total = {}
for key, val in hash.items():
    total[key] = sum(val)

newspapers = list(total.keys())

limit = 40
limit = int(input("enter the limit: "))

for i in range(len(newspapers)):
    for j in range(i+1, len(newspapers)):
        diff = total[newspapers[i]] + total[newspapers[j]]
        if diff <= limit:
            print(newspapers[i] , newspapers[j])








