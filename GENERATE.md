# Program til at genere spilleplader

Generator-algoritmen:
1. vælg tilfældigt et ord på mellem 5-8 tegn fra ordbogen
1. placer ordet tilfældigt på spillepladen ved hjælp af placerings-algoritmen
1. udfyld tomme felter ved at sample et bogstav fra det danske alfabet med sandsynlighed = frekvens af bogstav (se figur).

Placerings-algoritmen:

1. vælg et tilfældigt startsted på pladen og skriv første bogstav der
1. vælg tilfældigt en ubrugt nabo til næste bogstav
1. hvis hele ord placeret: afslut
1. hvis ikke flere ubrugte naboer, gå til 1 (prøv forfra)
1. gå til 2

Den relative frekvens af bogstaver på dansk ses i figuren herunder.

![](./images/frekvenser.png)

Cirka 13% af bogstaverne i danske ord er således bogstavet E, mens Æ og Ø begge udgør cirka 2% af bogstaverne i danske ord.
