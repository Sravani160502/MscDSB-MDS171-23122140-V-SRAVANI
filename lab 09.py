class petstore:
    def __init__(self):
        self.pets = {"Dogs": [], "cats":[], "rabbit":[],"parrot":[]}
    
    
    def storePet(self,type,name,age,amt):
        temp = {"name":name, "Age":age, "Amount":amt}
        self.pets[type].append(temp)

pets = petstore()
print(pets.pets)
pets.storePet('Dogs','abcd',5,12000)
pets.storePet('cats','abcd',6,1200)
pets.storePet('rabbit','xyz',4,20000,)
pets.storePet('parrot','arch',10,1000)

print(pets.pets)

for pet in pets.pets:
    print(pet)
    print(pets.pets[pet])
    for item in pets.pets[pet]:
       print(item)
    print(item['name'])
