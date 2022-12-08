# Ohtuminiprojekti!

![GHA workflow badge](https://github.com/jyrikangas/ohtuminiprojekti/workflows/CI/badge.svg)

# Linkit 

- [Tästä](https://ohtuminiprojekti.fly.dev:5000/) sovellukseen.
- [Tästä](https://helsinkifi-my.sharepoint.com/:x:/g/personal/kajy_ad_helsinki_fi/Ef1LbjVAhbtOkqyw6ePnJrQBQsuSYnmgXV5_LpB7lgaqeA?e=40hfPr) backlogeihin. 
Ensimmäisellä välilehdellä product backlog, toisella välilehdellä 1. sprintin backlog ja kolmannella välilehdellä 2. sprintin backlog. 
- [Tästä](https://app.codecov.io/gh/jyrikangas/ohtuminiprojekti) testikattavuusraporttiin.

# Definition of done

- Toteutettu hyväksymiskriteerien mukaisesti
- Asiakkaan käytettävissä
- Dokumentoitu
- Testattu kattavasti

# Ohjelman käyttö lokaalisti

  1. Kopioi repositorio omalle koneellesi
  2. Asenna riippuvuudet komennolla:
  ```bash
  poetry install
  ``` 
  4. Siirry kansioon src
  5. Aja init_db.py komennolla:
  ```bash
  python3 init_db.py
  ```
  3. Siirry virtuaaliympäristöön komennolla:
  ```bash
  poetry shell
  ```
  4. Käynnistä sovellus komennolla:
  ```bash
  flask run
  ```
        

