import subprocess

subprocess.run('cls', shell=True)

points = 0


print("""Fråga 1: Vem räknas ofta som världens första programmerare?
A) Grace Hopper
B) Margaret Hamilton
C) Ada Lovelace""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 2: Vad användes för att programmera de första datorerna?
A) Hålkort
B) Touchskärmar
C) USB-minnen""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 3: Vad hette den kända datorn som användes under andra världskriget?
A) COBOL
B) ENIAC
C) Apollo""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "B":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 4: Vem utvecklade programmeringsspråket COBOL?
A) Grace Hopper
B) Ada Lovelace
C) Margaret Hamilton""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 5: Var arbetade Margaret Hamilton?
A) Microsoft
B) NASA
C) Apple""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "B":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 6: Under vilket årtionde började internet bli tillgängligt för allmänheten?
A) 1970-talet
B) 1980-talet
C) 1990-talet""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 7: Vilket språk används för att skapa interaktivitet på webbsidor?
A) JavaScript
B) COBOL
C) Python""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 8: Vilka två tekniker används för att strukturera och formge webbsidor?
A) HTML och CSS
B) COBOL och ENIAC
C) NASA och Apollo""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 9: Vad används programmering till inom sjukvården?
A) Att analysera data och hjälpa läkare
B) Att bygga hus
C) Att laga bilar""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)


print("""Fråga 10: Vad har programmering bland annat hjälpt forskare med?
A) Att analysera miljödata
B) Att göra hålkort
C) Att bygga ENIAC""")

while True:
    answer = input("Svar: ")

    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

print("Du fick", points, "poäng av 10!")