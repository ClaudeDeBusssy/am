import database as db
import scrapper as sc


def fillDBwithScrappedData():
    scrapedData = sc.getAllPlayers()
    session = db.getSession()

    for spieler in scrapedData:
        # results = session.query(db.Spieler).filter(
        #     db.Spieler.name == spieler[0])

        # if len(results) == 0:

        spielerId = spieler[0] + spieler[1]

        dbSpieler = db.Spieler(
            spielerId, spieler[0], 1, spieler[1], spieler[2])

        gesamtpunkte = int(spieler[7].replace(".", ""))
        marktwert = int(spieler[4].replace("€", "").replace(".", ""))

        punktemarktwert = marktwert / gesamtpunkte

        dbSpieltag = db.Spieltage(
            spielerId,
            202307,
            marktwert,
            int(spieler[5]),
            int(spieler[3] if spieler[3] != '' else 0),
            float(spieler[6].replace(",", ".")),
            gesamtpunkte,
            punktemarktwert)

        session.add(dbSpieltag)
        session.add(dbSpieler)

    session.commit()


fillDBwithScrappedData()
