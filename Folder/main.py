import random

letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M",]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
special_characters = ["!","@","#","$","%","^","&","*",]

password_character1 = random.choice(letters)
password_character2 = random.choice(letters)
password_character3 = random.choice(letters)
password_character4 = random.choice(numbers)
password_character5 = random.choice(numbers)
password_character6 = random.choice(numbers)
password_character7 = random.choice(special_characters)
password_character8 = random.choice(special_characters)

password = [password_character7,password_character5,password_character3,password_character8,password_character6,password_character4,password_character2,password_character1]
random.shuffle(password)
print("".join(password))