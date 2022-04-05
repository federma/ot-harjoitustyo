Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa

```mermaid
 classDiagram
    Monopoli "1" -- "1" Pelitauta
    Noppa "2" -- "1" Pelilauta
    Ruutu "40" -- "1" Pelilauta
    Ruutu "1" --> "1" Ruutu
    Pelaaja "2..8" -- "1" Monopoli
    Pelaaja "1" -- "1" Pelinappula
    Pelinappula "1" --> "1" Ruutu
    class Monopoli {
        id
        pelaajat
    }
    class Pelilauta{
        id
        ruudut
    }
    class Noppa{
        id
    }
    class Ruutu{
        id
        seuraaja
    }
    class Pelaaja{
        nimi
        pelinappula
    }
    class Pelinappula{
        id
    }
```