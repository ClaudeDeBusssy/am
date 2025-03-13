import database as db
import plotly.express as px


session = db.getSession()

spieltage = session.query(db.Spieltage).all()

x = []
y = []
spieler = []

marktwertdurchschnitt = 0
punktedurchschnitt = 0

spieltageLänge = 0

for spieltag in spieltage:
    marktwertdurchschnitt = marktwertdurchschnitt + spieltag.Marktwert
    punktedurchschnitt = punktedurchschnitt + spieltag.PunkteGesamt
    spieltageLänge = spieltageLänge + 1


marktwertdurchschnitt = marktwertdurchschnitt / spieltageLänge
punktedurchschnitt = punktedurchschnitt / spieltageLänge

print(spieltageLänge)
print(marktwertdurchschnitt)
print(punktedurchschnitt)

for spieltag in spieltage:
    y.append(spieltag.PunkteGesamt - ((punktedurchschnitt * spieltag.Marktwert) /
                                      marktwertdurchschnitt))
    x.append(spieltag.Marktwert)

    # x.append(spieltag.Marktwert - ((marktwertdurchschnitt * spieltag.PunkteGesamt) /
    #                                punktedurchschnitt))
    spieler.append(spieltag.spielerId)

fig = px.scatter(x=x, y=y, color=spieler)
fig.show()
