#LEVEL 1

#1.Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
numero = len(it_companies)
print(numero)

#2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)

#3.Insert multiple IT companies at once to the set it_companies
it_companies.update(["Imstagram", "Meta", "Whats App"])
print("After adding multiple companies:", it_companies)

#4.Remove one of the companies from the set it_companies
it_companies.remove("IBM")
print("After removing IBM:", it_companies)

#5.What is the difference between remove and discard
#La diferencia de remove. si busco una variabre que no esta en una lista me va a dar error
#La dferencia de discard: si busco algo que no esta en una lista me da error
