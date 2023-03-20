exp = [2200, 2350, 2600, 2130, 2190]
print("In feb this much extra was spent compared to jan:", exp[1]-exp[0])
print("Total amount in first quarter", exp[0]+exp[1]+exp[2])
print("Did I spent 2000$ in any month?", 2000 in exp)
exp.append(1980)
print("adding june month expenditure", exp)
exp[3] = exp[3] - 200
print("Expenses after $200 in April:",exp)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
#len(heros)
print("The length of heoos",len(heros))
heros.append('black panther')
print("The sixth hero is", heros)
heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print("heros", heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)