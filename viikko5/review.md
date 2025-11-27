# Copilotin kommentit ja muutosehdotukset

- Copilotin mukaan funktion nimi round() ei ole hyvä, sillä se on sama kuin Pythonin sisäänrakennettu funktio round(). Copilot ehdotti funktion uudelleennimeämistä -> play_round(). Muutos hyväksytty ✅
- Copilotin mukaan won_point() metodi ei tarkista pelaajien nimiä väärien nimien varalta. Copilot ehdottaa validoinnin lisäämistä ja ValueErrorin nostamista, jos metodille annetaan väärä pelaajanimi. Muutos hyväksytty ✅
- Copilotin mukaan overtime_score() funktiolla ei ole return statementtia, jos kaikki ehdot epäonnistuvat. Copilot ehdottaa eksplisiittisen return None argumentin lisäämistä tai RuntimeErrorin nostamista, kun kaikki ehdot epäonnistuvat. Muutos hyväksytty ✅

# Copilotin hyödyllisyys

Copilotin esittämät kommentit vaikuttivat hyödyllisiltä. Se ei ottanut kantaa toimivan sovelluksen päätoiminnallisuuteen, mutta ehdotti muutamia hyvän tavan mukaisia muutoksia arvojen validointiin sekä virheiden ja poikkeustilanteiden käsittelyyn. Esitetyt kommentit oli helppo ja selkeä ymmärtää, ja muutokset toteuttaa pull requestin review -sivulla.
