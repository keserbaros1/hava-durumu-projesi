import unittest
from main import ortalama_hesapla

class TestOrtalamaHesapla(unittest.TestCase):
    def test_bos_liste(self):
        self.assertEqual(ortalama_hesapla([]), 0)

    def test_normal_liste(self):
        self.assertAlmostEqual(ortalama_hesapla([70, 80, 90]), 80.0)

    def test_tek_not(self):
        self.assertEqual(ortalama_hesapla([100]), 100.0)

if __name__ == '__main__':
    unittest.main()
