"""
Projektdokumentation för Genomsnittsåldersberäknare:
Utvecklingsprocess:
- Algoritmen skapades först i pseudokod för att tydligt definiera programmets flöde.
- Kodutvecklingen genomfördes stegvis, med kontinuerliga tester efter varje ny funktion.
- Fokus lades på att säkerställa programmets robusthet genom att hantera olika typer av felaktiga användarinmatningar.

Felsökning:
- Syntaxfel och logiska fel åtgärdades löpande under kodskrivningen.
- Särskild uppmärksamhet ägnades åt att testa programmet med oväntade inmatningar, såsom icke-alfabetiska tecken i namn och ogiltiga värden för kön och ålder.
- Ett strukturerat felsökningstillvägagångssätt användes för att identifiera och lösa problem, vilket dokumenterades i utvecklingsloggen.

Reflektion:
- Detta projekt har stärkt mina färdigheter i Python-programmering, särskilt i felhantering och användarinteraktion.
- Jag har lärt mig vikten av att planera och strukturera koden noggrant före utvecklingen, samt värdet av kontinuerlig testning.
"""


def main():
    # Ordboken 'genders' innehåller två kategorier: 'M' för män och 'F' för kvinnor.
    # För varje kategori lagrar vi 'total_age' som är summan av alla åldrar och 'count' som är antalet personer.
    genders = {'M': {'total_age': 0, 'count': 0}, 'F': {'total_age': 0, 'count': 0}}

    while True:
        # Anropar funktionen 'input_person_details' för att få inmatade uppgifter om en person.
        person = input_person_details()
        # Uppdaterar total ålder och antal personer för respektive kön med den inmatade personens information.
        update_totals(person, genders)

        # Frågar användaren om nästa åtgärd: lägga till en annan person eller se genomsnittsåldrarna.
        # Om användaren matar in 'r', visas genomsnittsåldrarna och programmet avslutas.
        # Om användaren trycker på Enter, fortsätter programmet att ta emot uppgifter för nästa person.
        next_action = input("Tryck på Enter för att lägga till en annan person eller skriv 'R' för att se genomsnittsåldrarna: ").lower()
        if next_action == 'r':
            print_averages(genders)
            break

def input_person_details():
    # Den här funktionen ansvarar för att samla in personuppgifter från användaren.
    # Den kommer att fortsätta fråga efter namn, kön och ålder tills giltiga värden matas in.
    while True:
        # Användaren matar in ett namn, som måste bestå av endast bokstäver och mellanslag.
        name = input("Ange personens namn (Förnamn Efternamn): ")
        if all(part.isalpha() for part in name.split()):
            break
        print("Ogiltigt namn. Endast alfabetiska tecken och mellanslag är tillåtna.")

    # Användaren matar in ett kön. Detta måste vara 'M' för man eller 'F' för kvinna.
    # Funktionen kommer att fortsätta fråga tills ett av dessa värden matas in.
    gender = input("Ange personens kön (M/F): ").upper()
    while gender not in ['M', 'F']:
        print("Ogiltigt kön. Vänligen ange 'M' för man eller 'F' för kvinna.")
        gender = input("Ange personens kön (M/F): ").upper()

    # Användaren matar in en ålder, som måste vara ett positivt heltal.
    # Funktionen kontrollerar att inmatningen är en siffra och fortsätter fråga tills det är korrekt.
    while True:
        age = input("Ange personens ålder: ")
        if age.isdigit():
            break
        print("Ogiltig inmatning för ålder. Vänligen mata in ett nummer.")

    # Returnerar en ordbok med personens namn, kön och ålder.
    return {'name': name, 'gender': gender, 'age': int(age)}

def update_totals(person, genders):
    # Denna funktion tar emot en persons uppgifter och uppdaterar 'genders'-ordbokens totala åldrar och antal.
    # Den adderar personens ålder till den totala åldersumman för rätt kön och ökar antalet registrerade personer med 1.
    genders[person['gender']]['total_age'] += person['age']
    genders[person['gender']]['count'] += 1

def print_averages(genders):
    # Funktionen går igenom varje kön i 'genders'-ordboken och beräknar samt skriver ut genomsnittsåldern.
    for gender, data in genders.items():
        if data['count'] == 0:
            print(f"Inga data för {gender}.")
        else:
            average_age = data['total_age'] / data['count']
            print(f"Genomsnittsålder för {gender} är: {average_age:.2f}")

if __name__ == "__main__":
    # Om scriptet körs direkt, kör huvudfunktionen
    main()
