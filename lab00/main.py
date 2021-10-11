litera = 'J'
nazw = 'kowalski'
imie = 'jan'
c1 = "20"
c2 = "21"
wiek = 20
a = 100
list1 = [1, 2, 3, 8]

#1
#Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia,
# oraz nazwisko, a następnie zwróci te wartości połączone kropką.
# Przykładowe wyjście: J. Kowalski.

def foo1(litera, nazw):
    return (litera + ". " + nazw)

print(foo1(litera, nazw))

#2
#Przygotować funkcję, która przyjmie w parametrach imię i nazwisko,
# oraz zwróci pierwszą literę imienia i nazwisko połączone kropką.
# Funkcja powinna również dbać o poprawność wielkich liter.
# Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.

def foo2(imie, nazw):
    litera = imie[0].upper()
    nazw = nazw.capitalize()
    return(litera + ". " + nazw)

print(foo2(imie, nazw))

#3
#Przygotować funkcję, która przyjmie 3 argumenty:
# 2 pierwsze cyfry aktualnego roku, 2 ostatnie cyfry aktualnego roku,
# wiek użytkownika, a następnie zwróci jego rok urodzenia.

def foo3(c1, c2, wiek):
    rok = c1 + c2
    rok = int(rok)
    rok = rok - wiek
    return(rok)

print(foo3(c1, c2, wiek))

#4
#Przygotować funkcję, która przyjmie 3 parametry:
# imię, nazwisko i funkcję przetwarzającą te dane,
# a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze.
# Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2),
# wyjście: J. Kowalski.

def foo4(imie, nazw, foo):
    return(foo(imie, nazw))

print(foo4(imie, nazw, foo2))

#5
#Przygotować funkcję, która przyjmie 2 argumenty,
# a następnie zwróci wynik ich dzielenia. Należy sprawdzić w jednej
# instrukcji if (bez użycia elif i else), czy obydwie liczby są dodatnie
# oraz czy druga liczba jest różna od 0.

def foo5(a, b):
    if(a >= 0) & (b > 0):
        return (a/b)

print(foo5(a, wiek))

#6
#Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby
# w pętli, dopóki suma wszystkich podanych do tej pory liczb nie osiągnie
# wartości 100.

suma = 0
while(suma < 100):
    suma += int(input("Podaj liczbe:"))

#7
#Przygotować funkcję, która przyjmie 1 argument w postaci listy,
# a następnie zwróci te elementy w postaci krotki.

def foo7(list1):
        return tuple(list1)

print(foo7(list1))
#print(type(foo7(list1)))

#8
#Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy
# wartości używając pętli, a następnie wartości z tej zostanią zrzutowane
# do krotki.

list2 = []
while(len(list2) < 4):
    list2.append(input("Podaj wartosc:"))

list2 = tuple(list2)
# print(list2)
# print(type(list2))

#9
#Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy,
# a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu
# argumentowi. Nie należy w tym zadaniu używać instrukcji warunkowych!
# Przykładowo, wejście: 6, wyjście: sobota.

def foo9(i: int):
    switcher = {
                0: 'poniedzialek',
                1: 'wtorek',
                2: 'środa',
                3: 'czwartek',
                4: 'piątek',
                5: 'sobota',
                6: 'niedziela'
                                    }
    return switcher.get(i, "Nie ma takiego dnia tygodnia")

print(foo9(6))

#10
#Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków,
# a następnie zwróci wartość logiczną informującą o tym
# czy przekazany tekst jest palindromem.

def foo10(s: str):
    le = len(s) - 1
    for i in range(0, int(le / 2)):
        if s[i] != s[le - i]:
            return False
    return True

print(foo10("madam"))



