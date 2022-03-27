import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        #saldo on senteissä
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        #saldo tulostuu euroissa
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(251)
        self.assertEqual(str(self.maksukortti), "saldo: 12.51")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(91)
        self.assertEqual(str(self.maksukortti), "saldo: 9.09")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(9999)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_ota_rahaa_palauttaa_True_jos_rahat_riittivat(self):        
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_ota_rahaa_palauttaa_False_jos_rahat_eivat_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(2000))
