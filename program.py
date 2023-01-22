wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
region = input("Wybierz swój region: wpisz USA lub EUR 	")
plec = input("Podaj swoją plec: k-kobieta lub m- mężczyzna")
# Sprawdzamy czy podany wiek jest liczbą

if wiek.isdigit() == False:
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
wiek=int(wiek)
if region == "EUR":
	if wiek>=18 and wiek<=40:
		print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	elif wiek>40:
		print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
		print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
	else:
		exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
if region == "USA":
	if wiek >= 21 and wiek <= 40:
		print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	elif wiek > 40:
		print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
		print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
	else:
		exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")