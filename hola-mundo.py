import tools
from student import Student
from Question import Question
from Chef import Chef
from ChineseChief import ChineseChef
print ("¡Hola mundo!")
num = 15
print (num)
EDAD = 20
Edad = 25
edad = EDAD + Edad
print (edad)
print (EDAD)
print (Edad)
nombre = "Python"
print (nombre)
print (len(nombre))
print (nombre[0])
print (nombre[1])
print (nombre[2])
print (nombre[3])
print (nombre[1:6])
print (nombre[1:])
print (nombre[:4])
print (nombre[0:6:3])
#nun = int (input("Ingrese un Número: "))#
#print (nun)#
años = 50
años += 3
print (años)
años -= 2
print (años)
num_a = 6
num_a %= 2
print (num_a)
print ("   /|")
print ("  / |")
print (" /  |")
print ("/___|")
character_name = "John"
character_age = "35"
print ("There once was a man named "+ character_name +", ")
print ("he was "+ character_age + " years old. ")
character_name = "Mike"
character_age = "20"
print("He really liked the name "+ character_name +", ")
print ("but didn´t like being " + character_age + ", ")
print ("Giraffe \nAcademy")
phrase = "Giraffe Academy"
print (phrase +" is cool")
print (phrase.lower())
print (phrase.upper())
print (phrase.isupper())
print (phrase.upper().isupper())
print (len (phrase))
print (phrase[0])
print (phrase.index("G"))
print (phrase.replace("Giraffe", "Elephant"))
my_num = -5
print (abs(my_num))
print (pow(9, 9))
print (max(4, 6))
print (min (4,6))
#name = input("Enter you name:  ")
#age = input("Enter you nage:  ")
#print ("Hello " + name + "! you are the best, you have " + age + " years old")
#Calculator#
#num1 = input("Enter you frist number: ")
#num2 = input("Enter you second number: ")
#result = float(num1) + float(num2)
#print (result)
#mads libs
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural_noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + color )
#print(plural_noun +" are blue")
#print("Ilove " + celebrity)
#Listas
lucky_numbers = [4, 8, 15, 16, 23, 42, 1, 3, 6]
friends = ["Kevin", "Karen", "Kris", "Oscar", "Alberto", "Jesus", "Jesus"]
friends[1] = "MIKE"
print(friends[2])
print(friends[-1])
print(friends[1:6])
friends.sort()
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Oscar")
print(friends)
print(friends.index("Jesus"))
print(friends.count("Jesus"))
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
#Tupples
def sayhi(name, age):
    print("Hello " + name +" " + age)
print("Top")
sayhi("Mike", "35")
sayhi("Steve", "20")
print("Bottom")
def cube(num3):
    return num3*num3*num3
print(cube(3))
# condicionantes
is_male = True
is_tall = True
if is_male or is_tall:
    print(" You are a male or tall or both")
else: 
    print("You are neither male nor tall")
if is_male and is_tall:
    print(" You are a male or tall or both")
else: 
    print("You are neither male nor tall or both")
def max_num(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3:
        return num1    
    elif num4 >= num1 and num4 >= num2:
        return num4
    elif num3 >= num1 and num3 >= num2:
        return num2
        
    else:
        num3
print (max_num(2, 5, 9, 8))
'''numa = float(input("Enter fris number: "))
op = input("Enter operador: ")
numb =float(input("Enter second number: "))
if op == "+":
    print(numa + numb)
elif op == "-":
    print(numa - numb)
elif op == "*":
    print(numa * numb)
elif op == "/":
    print(numa / numb)
else:
    print("Invalid")'''
#Dictonaries
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversion["Nov"])
print(monthConversion.get("Dec"))
#ciclos
i = 1
while i<= 10:
    print(i)
    i = i + 1

print("Done")
'''
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess!= secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You Win")'''

for letter in "Giraffe AcademY":
    print(letter)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(2, 3))
print("")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][2])
for row in number_grid:
    for col in row:
        print(col)
# translator
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g" 
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a Phrase")))'''

try:
    value = 10 / 0
    numeroo = int(input("Pon un numero porfa : "))
    print(numeroo)
except ZeroDivisionError:
    print("Division por cero")
except ValueError:
    print("Entrada invalida")
dato = open("datos.txt", "r")
print(dato.readable())
#print(dato.read())
for employee in dato.readlines():
    print(employee)
print("")
#print(dato.readline()[0])
dato = open("datos.txt", "a")
dato.write("\nEnero   ocho")
dato = open("datos.txt", "r")
print(dato.read())
dato.close()
datoo = open("datos.txt", "w")
datoo.write("Nuevo documento")
print(tools.roll_dice(10))
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Homero", "Fsica", 4.3, True)
print(student2.name)
print(student1.on_honor_roll())
print(student2.on_honor_roll())
'''uestion_prompts = [
    "What color are apples?\n(a) Read/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Reas\n(b) Red\n(c) Blue\n\n"
]
question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " / " + str(len(questions)) + " Correct")

run_test(question)'''
myChef = Chef()
myChef.make_chiken()
myChineseChef = ChineseChef()
myChineseChef.make_special_dish()