import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from pankki import Pankki


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # alustetaan kauppa
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tehtaessa_yksi_ostos_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.viitegeneraattori_mock.uusi.return_value = 42

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_ostettaessa_kaksi_eri_tuotetta_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):

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

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 11
        )

    def test_ostettaessa_kaksi_samaa_tuotetta_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_ostettaessa_tuote_joka_on_loppu_ja_tuote_jota_on_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(
        self,
    ):

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

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_edellisen_ostoksen_hinta_ei_näy_uuden_ostoksen_hinnassa(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)

        self.kauppa.aloita_asiointi()

        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 0
        )

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_ostotapahtumalle(self):
        viitegeneraattori_mock = Mock()

        # alustetaan kauppa
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, viitegeneraattori_mock
        )

        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)

        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)

        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 43, "12345", "33333-44455", 5
        )

    def test_poista_tuote_korista(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 30

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)

        self.kauppa.poista_korista(3)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 0
        )
