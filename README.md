# README

I dette repository finder du programmer og data til at spille et 4 x 4 ordspil, som minder om Facebooks *WordBlitz* spil. Ideen er at skrive en algoritme, som kan spille spillet automatisk. Vi kan se se hvor godt vi klarer os i forhold til den. Hvis du ikke kender spillet betyder det ikke noget, da reglerne er forklarer herunder.

Det hjælper hvis du har en computer med Linux eller Mac, men det er dog ikke strengt nødvendigt. Vi skriver programmerne i  programmeringssproget Python.

## Spillets regler

En 4 x 4 spilleplade kan f.eks. se sådan her ud.

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

Som du kan se indeholder spillepladen 16 celler med bogstaver i. Spillet går ud på at finde så mange ord som muligt på spillepladen ved at holde sig til disse regler for hvert ord:

1. Vælg frit en startcelle og skriv bogstavet ned.
1. Vælg en nabocelle enten til venstre, højre, over, under eller langs en af de skrå retninger. Skriv bogstavet ned.
1. Gentag det foregående trin indtil du har skrevet et rigtigt dansk ord.
1. Du må højst bruge hver celle én gang per ord. Derfor kan du højst finde ord på 16 bogstaver.
1. Efter du har fundet et ord, starter du forfra fra trin 1. Gentag indtil du ikke kan finde flere ord.

**Eksempel**: Start på bogstavet B i venstre side. Hop videre til bogstavet R, som står til højre. Hop skråt ned til venstre til bogstavet Ø. Hop skråt ned til højre til bogstavet D. Nu har du dannet ordet BRØD.

> På ovenstående spilleplade kan du f.eks. danne orderne DØR, ARM, ARME, BRED, BRØD, BØDE, SPID, SPIR, SPIRE, SPIRER og SPIRRE? Kan du finde dem allesammen?

### Sådan tæller du point

Du modtager point for hvert bogstav du har benyttet til at danne ord. For at holde det simpelt får du 1 point per bogstav. I en mere avanceret udgave får du flere point for sjældne bogstaver som X, Z og Q, men det er ikke nødvendigt her.

**Eksempel**: lad os sige du du fandt ordene ARM og BRØD. Så ville du have fået 3 + 4 point.

## Programmeringsudfordring

Vi skriver to forskellige programmer, som kan løse følgende problemer:

- Generere tilfældige spilleplader, som er sjove at spille på (indeholder et rimeligt antal danske ord).
- Automatisk finde så mange ord som muligt på en spilleplade.

Før vi kan gå igang skal vi lige have styr på nogle ting, som f.eks. at have en ordbog over danske ord, hvilket vi gennemgår i næste afsnit.

## Dansk ordbog

Grundlaget for hele spillet er en ordbog med danske ord, så den skal vi have først. Uden en ordbog kan vi ikke tjekke at de ord vi finder er rigtige danske ord. F.eks. er de fleste enige om at ZGRTRAMC ikke et rigtigt ord på dansk, så man skal selvfølgeligt ikke have point for det.

Normalt er det er også vigtigt at ordbogen er så komplet som muligt, altså at den indeholder alle danske ord og alle bøjninger. Du skal jo helst ikke snydes for point bare fordi vi havde glemt at tilføje et ord til ordbogen. Men, vi kommer nok til at være lidt dovne.

### Bøjninger

I forhold til en komplet ordbog, så er det vigtigt at have alle bøjninger med. Ord på dansk bøjes ofte ved at tilføje forskellige endelser. Nogle gange ændrer order helt bogstav, f.eks. stige (nutid), steg (datid). Nedenunder kan du se nogle mulige bøjninger af navneordet ARM ved at følge grene i træet. F.eks. giver `ARM + E + N = ARMEN` ordet ARM i bestemt ental:

```                                                 
                              ┌───▶  E  ───▶  S  
                              │                  
        ┌───▶  E  ───▶  N  ───┤                  
        │                     │                  
 ARM ───┤                     └───▶  S           
        │                                        
        └───▶  S                                 
```

> Vores algoritme er ligeglad med om alle bøjninger er med i ordbogen. Derfor indeholder vores ordbog kun stammen af hvert ord, f.eks. ARM men ikke ARMEN.

### Ordbogsfil

Vi bruger en ordbog fra [www.stavekontrolden.dk](http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.dic). På hjemmesiden findes også en [fil med bøjninger](http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.aff), men den bruger vi ikke, da vores ordbog jo ikke behøver at være komplet.

Vi har downloadet ordbogsfilen "da_DK.dic" med kommandoen `wget` og den ligger allerede i mappen data, så du behøver ikke gøre det igen:

```
cd data
wget http://www.stavekontrolden.dk/main/sspinputfiles/da_DK.dic
```

Du kan bruge kommandoen `wc -l` til at tælle hvor mange linjer der er i filen. Da der er ét ord per linje fortæller det dig hvor mange ord der er i ordbogen.

```
$ wc -l da_DK.dic
  167344 da_DK.dic
```

Der er altså 167.344 ord i ordbogen; helt klart nok til at have det sjovt. Lad os hvad der er i filen med kommandoen `head`:

da_DK.dic (udsnit):

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
