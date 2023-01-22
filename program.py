wiek = input("Podaj wiek użytkownika jako liczbę całkowitą: ")

if wiek.isdigit() == False:
    exit("Wiek musi być liczbą albo nie jest liczbą całkowitą")

wiek = int(wiek)
if wiek>=18 and wiek<=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
elif wiek>120:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    print("W Twoim wieku picie jest ekstremalne, pijesz na własne ryzyko")
else:
    exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

