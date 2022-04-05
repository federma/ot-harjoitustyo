Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa

```mermaid
 classDiagram
      Noppa "*" --> "1" Pelilauta
      Ruutu "*" --> "1" Pelilauta
      Pelaaja "*" --> "1" Pelinappula
      Pelinappula "*" --> "1" Ruutu
      class Pelilauta{
          id
          pelaajat
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