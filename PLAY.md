# Program til at spille word matrix

Du bare køre programmet sådan her:

```
python src/generate.py | python src/play.py
```

Se også beskrivelsen af [generate.py](./GENERATE.md).

## Hvordan det virker

Programmet er baseret på to smarte datastrukturer, som dataloger kalder for
henholdsvis en [Stak](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
og en [Trie](https://en.wikipedia.org/wiki/Trie).

- Stakken bruges til at holde styr på hvor langt vi er kommet i vores søgning efter ord
- Trie'en bruges til at afgøre om en række bogstaver udgør starten på et ord.

Programmet starter med at filtrere ordbogen på alle de ord, som kun består af bogstaver
på spillepladen. Der er jo ingen grund til at lede efter ord, som vi alligevel
ikke kan danne med de bogstaver der findes på pladen.

> 👑 Programmet tester ikke hvor mange gange bogstavet findes, men filtrerer stadig det fleste ord væk. Længe leve dovenskaben.

Disse ord tilføjes til en Trie og dernæst begynder programmet at lede efter disse ord.

> 👑 Det smarte er at man kan spørge en Trie en række bogstaver, f.eks. "KA" udgør starten
på et ord, som vi tidligere har tilføjet til Trie'en. Hvis vi tidligere har tilføjet ordet "KATAPULT", så
vil svaret være ja.

Programmet starter søgningen med at tilføje alle 16 bogstaver på spillepladen til stakken. Dernæst udlæses det øverste element på stakken og undersøges. Hvis dette element er et ord udskrives det.

Dernæst undersøges det om ordet kunne være starten på et større ord ved at undersøge nabofelterne.
De nabofelter som både er ubesøgte og som udgør starten på et større ord (det er her vi bruger Trie'en) knyttes i enden af det ord vi udlæste fra stakken og skubbes tilbage på stakken.

Programmet fortsætter indtil der ikke er flere elementer på stakken.
