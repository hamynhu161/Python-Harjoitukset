# Questora 

## Pelin idea

Antti on seikkailukirjoista innostunut poika, joka uskoo, että jokaisessa paikassa on piilotettu salaisuus. Hänen tavoitteensa on löytää eri seikkailun salaisuudet ja kirjoittaa niistä omaan seikkailupäiväkirjaansa.

Lähde seikkailumatkalle Antin kanssa ja tutki erilaisia maailmoja. 
    - Metsä-seikkailu 
    - Aavikko-seikkailu 
    - Meri-seikkailu

## Tavoite

Tavoitteena on löytää alueen mysteeri ja kerätä mahdollisimman paljon pisteitä.
Pelaaja voittaa seikkailun, kun hän on kerännyt kaksi vinkkiä ja löytänyt niiden avulla alueen salaisuuden.

## Toimintaperiaatteet ja toiminnallisuudet

Seikkailun aikana tapahtumat määräytyvät osittain satunnaisesti. Pelaaja voi esimerkiksi löytää uuden esineen, menettää esineen, kohdata vihollisen, auttaa hädässä oleva eläin, tai saada vihjeen alueen salaisuudesta. 

Oikeiden esineiden käyttäminen ja onnistuneet valinnat antavat pelaajalle pisteitä. Pelaaja voi myös menettää pistettä jos hän menettää esineen tai tekee tilanteeseen sopimattonman valinnan.
    - Esineen kerääminen: +15 pistettä
    - Esineen menettäminen: -15 pistettä
    - Sopivan esineen käyttäminen vihollista vastaan: +30 pistettä
    - Ei ole sopivaa esinettä: -10 pistettä
    - Vinkin löytäminen: +50 pistettä

Lopuksi pelaaja voi nähdä muiden pelaajien tulokset Questoran tulostaulukosta.

## Kestävän kehityksen näkökulmasta

Peli kannustaa auttamaan muita, tekemään sopivaa valintoja ja pohtimaan päätöstensä seurauksia. Lisäksi peli herättää kiinnostusta erilaisiin ympäristöihin ja niiden tutkimiseen.

## Pelin rakenne
```text
peliprojekti/
│
├── main.py                         ← pääohjelma
├── readme.md
├── intro.txt
├── ohjeet.txt
├── tallennetut_peli.txt
├── tallennetut_tulos.txt
└── peli/              
    ├── __init__.py                 ← paketin alustus, tuo moduulit käyttöön
    ├── esine.py                    ← sisältää Esine-luokan
    └── huone.py                    ← sisältää Huone-luokan
    └── pelaaja.py                  ← sisältää Pelaaja-luokan ja pelaajan toimintoja
    └── hahmo.py                    ← sisältää Hahmo-luokan
    └── piste.py                    ← sisältää Piste-luokan ja pisteiden hallinnan
    └── tiedostonhallinta.py        ← sisältää Tiedot-luokan ja hallitsee tiedostojen tallentamista, lataamista...
    └── tulostaulukko.py            ← tulostaulukon näyttäminen
    └── asetukset.py                ← äänenvoimakkuuden ja kirkkauden asetukset


