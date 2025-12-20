from kps_peli import KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly

PELIT = {"a": KPSPelaajaVsPelaaja, "b": KPSTekoaly, "c": KPSParempiTekoaly}


def luo_peli(vastaus):
    pelimuoto = PELIT.get(vastaus)
    if pelimuoto:
        peli = pelimuoto()
        return peli
