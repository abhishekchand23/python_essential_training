# while loop 

secret = "ac"
pw = ''

while pw != secret:
    pw = input("What is the secret word ")

# for loop
animals = ('deer', 'lion', 'tiger', 'rhino')

for pet in animals:
    print(pet)

# while additional controls

secret = "ac"
pw = ''
count =0
max_attempts = 5
auth = False

while pw != secret:
    count+=1
    if count > max_attempts: break
    if count == 3: continue 
    pw = input(f"{count}. What is the secret word ({max_attempts-count + 1} Attempt/s left) ")
else:
    auth = True
print('Authorized' if auth else "Max Attempt reached, Calling the FBI...")


# for additonal controls
# continue skips the condition of the loop
# break exits the loop
animals = ('deer', 'lion', 'tiger', 'rhino')

for pet in animals:
    if pet == "lion": continue
    if pet == 'rhino': break
    print(pet)
else:
    print('That is all the animals')