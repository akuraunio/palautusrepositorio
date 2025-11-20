import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from pankki import Pankki


class TestKauppa(unittest.TestCase):
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tehtaessa_yksi_ostos_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        viitegeneraattori_mock.uusi.return_value = 42

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_ostettaessa_kaksi_eri_tuotetta_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30
            elif tuote_id == 1:
                return 100

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)
            elif tuote_id == 1:
                return Tuote(1, "Guinness", 6)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        viitegeneraattori_mock.uusi.return_value = 42

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(3)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 11
        )

    def test_ostettaessa_kaksi_samaa_tuotetta_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        viitegeneraattori_mock.uusi.return_value = 42

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(3)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_ostettaessa_tuote_joka_on_loppu_ja_tuote_jota_on_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30
            if tuote_id == 1:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)
            if tuote_id == 1:
                return Tuote(1, "Guinness", 6)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        viitegeneraattori_mock.uusi.return_value = 42

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(3)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
