# Word-Matrix Algoritmer

I dette repository finder du programmer og data til at spille et 4 x 4 ordspil, som minder om Facebooks *WordBlitz* spil. Ideen er at skrive en algoritme, som kan spille spillet automatisk. Vi kan også se hvor godt vi klarer os i forhold til den. Det er OK hvis du ikke kender spillet i forvejen, da reglerne er forklaret herunder.

Det hjælper hvis du har en computer med Linux eller Mac, men det er dog ikke strengt nødvendigt. Vi skriver programmerne i  programmeringssproget Python og i dette dokument bruger vi et par Linux kommandoer. Mest for sjov skyld og narrestreger.

## Spillets regler

Spillet foregår på en 4 x 4 spilleplade, som f.eks. kan se sådan her ud.

```
┌───┬───┬───┬───┐
│ A │ R │ M │ O │
├───┼───┼───┼───┤
│ B │ R │ E │ C │
├───┼───┼───┼───┤
│ Ø │ I │ P │ D │
├───┼───┼───┼───┤
│ E │ D │ S │ A │
└───┴───┴───┴───┘
```

Du kan se 4 rækker og 4 søjler med bogstaver. Spillet går ud på at finde så mange ord som muligt ved at trække en sti gennem spillepladen. Når du leder efter et ord skal du holde dig til disse regler:

1. Vælg frit en startcelle og start dit ord med dette bogstav.
1. Vælg en nabocelle enten til venstre, højre, over, under eller langs en af de skrå retninger og ryk dertil. Tilføj cellens bogstav til dit ord.
1. Gentag det foregående trin indtil du har fundet et rigtigt dansk ord.
1. Hver celle må kun bruges én gang per ord. Derfor kan du højst finde ord på 16 bogstaver (usandsynligt at du finder så et langt ord).
1. Hvis du har fundet et ord, starter du forfra fra trin 1. Gentag indtil du ikke kan finde flere ord og husk de ord du fandt.

På ovenstående spilleplade kan du f.eks. finde orderne DØR, ARM, ARME, BRED, BRØD, BØDE, SPID, SPIR, SPIRE, SPIRER og SPIRRE? Kan du finde dem allesammen og måske endnu flere?

### Point-tælling

Du får point for hvert bogstav der indgår i et ord du fandt. I en mere avanceret udgave får du flere point for sjældne bogstaver som X, Z og Q, men det er ikke nødvendigt her.

> 👑 *Simplificering:* For at holde det simpelt giver alle bogstaver 1 point. Dovenskaben længe leve!

Lad os sige du du fandt ordene ARM og BRØD. Så ville du have fået 3 + 4 point, da ordene er på henholdsvis 3 og 4 bogstaver.


## Udfordringen

Udfordringen består i at finde noget data og skrive et par programmer:

- **Find dansk ordbog**: vi skal bruge en dansk ordbog, for ellers ved vi ikke om de ord vi finder er rigtige danske ord. Ordbogen skal være på en form som vores programmer kan læse. Det skal altså være en fil af en slags.
- **Skriv program 1**: genererer tilfældige spilleplader, som er sjove at spille på; den skal f.eks. indeholde mange danske ord; der skal også være både korte og lange ord.
- **Skriv program 2**: finder automatisk så mange ord som muligt på en spilleplade.

Før vi kan gå igang skal vi lige have styr på nogle ting, som f.eks. at have en ordbog over danske ord, hvilket vi gennemgår i næste afsnit.

### Part 1: Dansk ordbog

Grundlaget for hele spillet er en ordbog med danske ord, så den skal vi have først. Uden en ordbog kan vi ikke tjekke at de ord vi finder er rigtige danske ord. F.eks. er de fleste enige om at ZGRTRAMC ikke et rigtigt ord på dansk, så man skal selvfølgeligt ikke have point for det.

Normalt er det er også vigtigt at ordbogen er så komplet som muligt, altså at den indeholder alle danske ord og alle bøjninger. Du skal jo helst ikke snydes for point bare fordi vi havde glemt at tilføje et ord til ordbogen. Men, vi kommer nok til at være lidt dovne.

#### Bøjninger

I forhold til en komplet ordbog, så er det i princippet vigtigt at have alle bøjninger med, men vi tillader os at være lidt dovne.

> 👑 *Simplificering:* Algoritmen er den samme med og uden bøjninger, så lad os ignorere bøjninger og koncentrere os om koden. Dovenskaben længe leve!

#### Ordbogsfilerne

Vi bruger en dansk ordbog fra hjemmesiden [stavekontrolden.dk](http://stavekontrolden.dk). Ordbogen består af to filer, nemlig en ordfil ([da_DK.dic](http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.dic)), som indeholder alle ordene i deres grundform (altså uden bøjninger) og så en fil med bøjningsreglerne ([da_DK.aff](http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.aff)). I det efterfølgende bruger vi kun ordfilen "da_DK.dic".

Du finder ordbogsfilerne i mappen "data".

Hvis du har lyst, kan du selv downloade ordbogsfilerne med kommandoen `wget`.

```
cd data
wget http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.dic
wget http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.aff
```

#### Ekstra udfordringer

Vi kan tælle hvor mange ord der er i ordfilen ved hjælp af kommandoen `wc -l`. Den tæller egentlig hvor mange linjer der er i filen, men da der cirka er ét ord per linje er det næsten det samme.

```
$ wc -l da_DK.dic
  167344 da_DK.dic
```

Der er altså 167.344 linjer i ordbogen og cirka lige så mange ord. Hvis vi kigger på de første linjer i filen med kommandoen `head`, kan vi se hvor mange der ord der helt præcist er:

```
$ head -20 da_DK.dic
157883 # (c) Stavekontrolden.dk
universitetsverden/70,73,7,976,939,947
Uruk/55
Nordjylland/55,939,947
cand.
Nippur/55
vidnepligt/70,73,7,976,939,947
vidnesbyrd/70,252,10,976,939,947
vidneudsagn/70,252,10,976,939,947
vidskræmt/976,466
vidskræmts/976
vidskræmte/976
vidskræmtes
vidnegodtgørelse/70,73,7,976,939,947
vidneførsel/815,822,70,944,939,947
vidneforklaring/70,73,7,976,939,947
vidnefast/976,466
vidnefasts/976
vidnefaste/976
vidnefastes
```

Vi kan se, at der står 157883 i starten af filen. Det er nok det præcise antal ord i ordbogen. Hvis man åbner hele filen, kan man faktisk se en del tomme linjer, hvilket forklarer hvorfor antal linjer og antal ord er forskelligt.

### Part 2: Generer spilleplade

Her skal du lave et program som kan generere spilleplader. Dit program skal printe fire linjer. Hver linje skal bestå af præcist fire danske bogstaver uden mellemrum. For eksempel som her:

```
$ python <generator>.py
ABCD
EFGH
IJKL
MNOP
```


> 👑 Jeg har allerede skrevet et program, der laver tilfældige spilleplader. Du kan læse beskrivelsen af programmet i filen [GENERATE.md](./GENERATE.md). Du er velkommen til at bruge det som inspiration.

### Part 3: Spil spillet

Her skal du lave et program som kan spille et 4 x 4 word matrix spil. Dit program skal indlæse en spilleplade fra en fil (eller stdin) og printe alle de ord som det kan finde på spillepladen. For eksempel som her:

```
python <spiller>.py spilleplade.txt
BLE
LÆBE
ÆBLE
BLÆR
LÆR
LÆRE
```

TODO: angiv script til at tælle point automatisk (ide: `wc` plus lidt magi).

> 👑 Jeg har allerede skrevet et program, som kan spille spillet. Du kan læse beskrivelsen af programmerne i filen [PLAY.md](./PLAY.md). Du er velkommen til at bruge det som inspiration.
