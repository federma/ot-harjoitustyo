import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

# testit
# Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000 euroa, lounaita myyty 0)
#   Huomaa, että luokka tallentaa rahamäärän sentteinä
# Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
    # Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    # Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta

    def test_konstruktori_asettaa_kassan_rahamaaran_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_myytyjen_lounaiden_maaran_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    #edulliset käteisostot
    def test_edullinen_kateismaksu_lisaa_kassan_rahamaaran_oikein(self):
        self.kassa.syo_edullisesti_kateisella(340)
        #kassan rahamaara kasvanut 240
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_edullinen_kateismaksu_palauttaa_vaihtorahan_oikein(self):
        #edullisen hinta on 240, joten pitäisi palautua 100
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(340), 100)

    def test_edullinen_kateismaksu_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(340)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullinen_liian_pieni_maksu_ei_muuta_kassan_rahamaaraa(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullinen_liian_pieni_maksu_palauttaa_koko_maksun_vaihtorahana(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230), 230)

    def test_edullinen_liian_pieni_maksu_ei_muuta_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.edulliset, 0)

    #maukkaat käteisostot
    def test_maukkaan_kateismaksu_lisaa_kassan_rahamaaran_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        #kassan rahamaara kasvanut 400
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_maukkaan_kateismaksu_palauttaa_vaihtorahan_oikein(self):
        #maukkaan hinta on 400, joten pitäisi palautua 50
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(450), 50)

    def test_maukkaan_kateismaksu_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukkaan_liian_pieni_maksu_ei_muuta_kassan_rahamaaraa(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaan_liian_pieni_maksu_palauttaa_koko_maksun_vaihtorahana(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)

    def test_maukkaan_liian_pieni_maksu_ei_muuta_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.maukkaat, 0)

# seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
# Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    # Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    # Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    # Kassassa oleva rahamäärä ei muutu kortilla ostettaessa

    #edulliset korttiostot
    def test_korttiosto_edullinen_veloittaa_summan_kortilta_ja_palauttaa_True(self):
        kortti = Maksukortti(1000)
        #onnistuneen oston pitäisi palauttaa True
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(kortti))
        #kortilla tulee olla rahaa oston jälkeen 1000-240=760
        self.assertEqual(kortti.saldo, 760)

    def test_korttiosto_edullinen_kasvattaa_myytyjen_lounaiden_maaraa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_korttiosto_edullinen_ei_kasvata_myytyjen_lounaiden_maaraa_jos_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        #myytyjen määrä ei tule kasvaa
        self.assertEqual(self.kassa.edulliset, 0)

    def test_korttiosto_edullinen_ei_muuta_kortin_rahamaaraa_ja_palauttaa_False_jos_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        #epäonnistuneen oston pitäisi palauttaa False
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(kortti))
        #kortin rahamäärän ei tule muuttua
        self.assertEqual(kortti.saldo, 100)

    def test_korttiosto_edullinen_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    #maukkaat korttiostot
    def test_korttiosto_maukkaat_veloittaa_summan_kortilta_ja_palauttaa_True(self):
        kortti = Maksukortti(1000)
        #onnistuneen oston pitäisi palauttaa True
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(kortti))
        #kortilla tulee olla rahaa oston jälkeen 1000-400=600
        self.assertEqual(kortti.saldo, 600)

    def test_korttiosto_maukkaat_kasvattaa_myytyjen_lounaiden_maaraa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttiosto_maukkaat_ei_kasvata_myytyjen_lounaiden_maaraa_jos_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        #myytyjen määrä ei tule muuttua
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_maukkaat_ei_muuta_kortin_rahamaaraa_ja_palauttaa_False_jos_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        #epäonnistuneen oston pitäisi palauttaa False
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(kortti))
        #kortin rahamäärän ei tule muuttua
        self.assertEqual(kortti.saldo, 100)

    def test_korttiosto_maukkaat_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    # Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla

    def test_kortille_rahaa_ladatessa_kortin_saldo_muuttuu(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 123)
        self.assertEqual(kortti.saldo, 1123)

    def test_kortille_rahaa_ladatessa_kassan_rahamaara_muuttuu(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 123)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000+123)

    def test_negatiivisen_summan_lataus_kortille_ei_onnistu(self):
        kortti = Maksukortti(1000)
        #negatiivisen lataus palauttaa False
        self.assertFalse(self.kassa.lataa_rahaa_kortille(kortti, -123))
        #kortin saldo ei muutu
        self.assertEqual(kortti.saldo, 1000)
