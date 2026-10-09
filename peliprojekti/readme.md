# Saveyourboat
Pelaajan vene on hajonnut. Tavoitteena on ansaita 100 euroa ja korjata vene satamassa.


# Toimintaperiaatteet ja kolme reittiä
Paikat ovat Satama, Ranta ja Järvi. Satamasta kuljetaan rannan kautta
järvelle. Rannalta saa tutkimusvälineen ja järveltä ongen.

1. **Kalastaja:** kerää onki ja vähintään 6 roskaa. Kalasta ja myy saalis
   satamassa, kunnes myyntituloja on 100 euroa. Roskapalkkiota ei tarvitse
   lunastaa tällä reitillä. Ahven maksaa 5, hauki 10 ja kuha 15 euroa.
2. **Ympäristönsuojelija:** kerää kaikki 10 roskaa ja lunasta satamassa
   10 euroa jokaisesta. Tämä riittää korjaukseen ilman kalastusta.
3. **Tutkija:** kerää tutkimusväline ja tee tutkimus kaikissa kolmessa
   paikassa. Lunasta satamassa 100 euron kertapalkkio. Kalastamista tai
   siivoamista ei tarvita tällä reitillä.

Kaikki reitit päättyvät valintaan **Korjaa vene** satamassa. Myös reittien
yhdistäminen onnistuu. Rahaa ei kulu muihin toimintoihin.

# Ominaisuudet ja tallennus
- Nimi ja ikä, aloitusvalikko ja funktiolla toteutettu pelin päävalikko.
- Liikkuminen, paikkojen tutkiminen, esineiden kerääminen ja tavaralista.
- Kalastus, saalislista, myynti, siivous, tutkimukset ja kertaluonteiset palkkiot.
- Intro ja ohjeet luetaan tekstitiedostoista jokaisella käynnistyksellä.
- Valinta 12 tallentaa. Pelivalikon 0 tallentaa ja palaa aloitusvalikkoon.
- Aloitusvalikon 2 jatkaa tallennettua peliä. Voitto tallennetaan myös.

`tallennus.json` sisältää aluksi `null`: peliä ei ole vielä tallennettu.
Tallennuksessa säilyvät nimi, ikä, sijainti, raha, esineet, saalis, roskat,
jo palkitut roskat, tutkitut paikat, tutkimuspalkkio ja veneen korjaus.
Latauksessa kerätyt esineet poistetaan alkuperäisistä paikoistaan.
Tallennuspaikkoja on yksi. Uusi tallennus korvaa vanhan. Sulje peli
valikkojen kautta, jotta edistyminen tallentuu. JSON-tiedostoa ei tarvitse muokata käsin.

# Kestävyysnäkökulma
Peli käsittelee YK:n kestävän kehityksen tavoitetta 14, Vedenalaista elämää.
Tarinan järvi laskee mereen. Roskat vaikuttavat suoraan peliin: jos niitä
on vähintään 5, kalastaminen ei onnistu. Siivous palauttaa mahdollisuuden
kalastaa. Tutkimusreitti kiinnittää huomiota veneilyyn ja roskien kulkuun.
Pelissä voi voittaa myös pyytämättä yhtään kalaa. 


# Projektirakenne
```text
peliprojekti/
    main.py          Käynnistys, syötteet ja valikot
    pelaaja.py       Pelaaja-luokka ja pelaajan toimintoja
    huone.py         Huone-luokka eli pelin paikka
    esine.py         Esine-luokka
    toiminnot.py     Paikkojen luonti ja pelin toiminnot
    tiedostot.py     Tekstien lukeminen ja JSON-tallennus/lataus
    intro.txt        Aloitustarina
    ohjeet.txt       Peliohjeet
    tallennus.json   Yksi tallennettu pelitilanne
    readme.md        Projektin kuvaus ja käyttöohjeet
```