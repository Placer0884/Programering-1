# step 1
beatles = []
print("Step 1:", beatles)
#Skapar listan och skriver ut printar denna
# step 2
beatles.append("John")
beatles.append("Paul")
beatles.append("George")
#Lägger till de tre första medlemmarna i bandet
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("Please add the rest of the members to the list: "))

print("Step 3:", beatles)
#lägger till ytterligare två medlemmar i bandet
# step 4
for i in range(2):
    del beatles[-1]
#Tar bort de två sista medlemmarna i listan
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)
#lägger till Ringo Starr i listan
# testing list legth
print("The Fab", len(beatles))
