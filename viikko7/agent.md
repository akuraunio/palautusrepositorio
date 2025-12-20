## agent.md

- Agentin tekemeä web-käyttöliittymä toimii ja testit menevät läpi. Pelkästään pelaaja vs pelaaja pelimoodi ei toimi, käyttöliittymästä ei voi pelata toista siirtoa ja se jää jumiin.
- Varmistuin toimivasta ratkaisusta testaamalla itse käyttöliittymää manuaalisesti.
- En ole 100% varma toimivuudesta, sillä en itse tehnyt testejä, mutta peli on yksinkertainen joten toimivuus oli helppo todeta kokeilemalla
- Agentti käytti pohjana alkuperäistä pelilogiikkaa eikä muuttanut sitä mitenkään
- Agentin tekemät testit olivat kattavat. Sen tekemät testit tehtäväpohjan tekoäly luokille eivät menneet läpi eikä se saanut niitä korjattua.
- Agentin tekemä koodi on ymmärrettävää ja se osaa selittää yksittäisiä rivejä hyvin kysyttäessä
- Agentti teki paljon inline css sivupohjiin, oman readmen testeille, ja teki erittäin kattavat testit joista jokainen yksittäinen testi testaa pienintä mahdollista osaa testattavasta metodista. Nämä olivat uusia asioita minulle.
- Opin testeistä miten testata html sivun toimintaa ilman robot testejä pelkästään pytestilla. Tosin robot testit ovat varmaan yleensä parempia.
- Pyysin agenttia selittämään mikä on pytest.fixture. Vastauksen se kirjoitti kommenttina rivin alle.
- Myös testit jotka testaavat että peli loppuu 5 pisteeseen toimivat, vaikka muutin sovelluksen voittopisteet kolmeen pisteeseen ja totesin sen toimivan käyttöliittymän kautta. Syynä on se että testit asettavat pelaajan pisteiksi 4 ja testaavat, triggeröikö seuraava siirto voiton
- Annoin agentille yhden komennon per kohta tehtävänannossa, ja sen lisäksi pyysin sitä kaksi kertaa korjaamaan testejä, missä se ei onnistunut.
