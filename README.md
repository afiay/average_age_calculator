# Genomsnittsålderskalkylator Efter Kön

Detta Python-skript beräknar genomsnittsåldern för varje kön baserat på användarinput. Programmet uppmanar användaren att mata in personliga uppgifter för flera individer och ger sedan ut genomsnittsåldern för varje kön.

## Hur man kör programmet

Se till att du har Python installerat på ditt system. Du kan köra programmet från terminalen eller kommandotolken:

```bash
python average_age_calculator.py
```


## Funktioner

- Insamlar persondata för ett obestämt antal individer.
- Hanterar inmatning i ett strukturerat format: Namn, Kön (M/K), och Ålder.
- Tillhandahåller genomsnittsålder för varje kön efter att användaren har färdigställt inmatningen av alla individer.
- Tillåter fortsättning av datamatare eller beräkning av resultat på användarens kommando.

## Funktioner i koden

- `main()`: Huvudfunktionen. Den initierar lagringsstrukturen och styr programmets flöde baserat på användarens input.
- `input_person_details()`: Frågar användaren efter personuppgifter (namn, kön, ålder) och validerar inmatningen. Den säkerställer att namn innehåller endast alfabetiska tecken och mellanslag, kön är antingen 'M' eller 'K', och ålder är ett numeriskt värde.
- `update_totals(person, genders)`: Uppdaterar den löpande totalåldern och räkningen för personens angivna kön.
- `print_averages(genders)`: Beräknar och skriver ut genomsnittsåldern för varje kön.

## Kodstruktur
- **Initialisering:** Skapar en ordlista för att lagra totalåldern och antalet individer för män ('M') och kvinnor ('K').
- **Datainmatningsloop:** Fortsätter att fråga användaren efter information tills valet görs att visa resultatet.
- **Datainmatning och validering:** Säkerställer att endast giltig information accepteras (namn med endast bokstäver och mellanslag, kön som 'M' eller 'K', och ålder som numeriska värden).

### Initialisering

genders = {'M': {'total_age': 0, 'count': 0}, 'F': {'total_age': 0, 'count': 0}}


Koden initierar en ordlista för att lagra total ålder och antal för män ('M') och kvinnor ('K').

### Inmatningsloop

`while`-loopen i `main()`-funktionen fortsätter att fråga användaren efter inmatning tills användaren bestämmer sig för att se resultatet.

### Datainmatning och Validering

`input_person_details()` hanterar inmatning av individuella data. Funktionen upprätthåller giltig inmatning genom loopar och frågar igen om inmatningen inte uppfyller kriterierna.

### Uppdatera Totaler

Efter varje giltig inmatning ökar `update_totals()` totalåldern och antalet för det specificerade könet.

### Beräkna och Skriva ut Genomsnitt

När användaren anger att inga fler personer kommer att läggas till, kallas `print_averages()` för att beräkna och visa genomsnittsåldrarna.

## Framtida Förbättringar

- Hantera fler könsalternativ bortom den binära indelningen 'M' och 'K'.
- Spara inmatad data till en fil för varaktig lagring.
- Implementera felhantering för oväntade avstängningar eller avbrott.
- Inkludera ytterligare statistisk information som median och typvärde.

## Kontaktinformation

För eventuella frågor angående detta skript, vänligen kontakta ägaren av repositoryt.
