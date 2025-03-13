import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Spieler(Base):
    __tablename__ = "spieler"

    spielerId = db.Column("spielerId", db.String, primary_key=True)
    name = db.Column("name", db.String)
    rang = db.Column("rang", db.Integer)
    verein = db.Column("verein", db.String)
    position = db.Column("position", db.String)

    def __init__(self, spielerId, name, rang, verein, position):
        self.spielerId = spielerId
        self.name = name
        self.rang = rang
        self.verein = verein
        self.position = position

    def __repr__(self):
        return f"({self.spielerId} {self.name} {self.rang} {self.verein} {self.position})"


class Spieltage(Base):
    __tablename__ = "spieltage"

    spielerId = db.Column("spielerId", db.String, db.ForeignKey(
        "spieler.spielerId"), primary_key=True)
    spieltagId = db.Column("spieltagId", db.Integer, primary_key=True)
    Marktwert = db.Column("Marktwert", db.Integer, )
    Einsätze = db.Column("Einsätze", db.Integer, )
    PunkteSpieltag = db.Column("PunkteSpieltag", db.Integer, )
    PunkteDurschnitt = db.Column("PunkteDurschnitt", db.Float, )
    PunkteGesamt = db.Column("PunkteGesamt", db.Integer, )
    PunkteMarktwert = db.Column("PunkteMarktwer", db.Float)

    def __init__(self, spielerId, spieltagId, Marktwert, Einsätze, PunkteSpieltag, PunkteDurschnitt, PunkteGesamt, PunkteMarktwert):
        self.spielerId = spielerId
        self.spieltagId = spieltagId
        self.Marktwert = Marktwert
        self.Einsätze = Einsätze
        self.PunkteSpieltag = PunkteSpieltag
        self.PunkteDurschnitt = PunkteDurschnitt
        self.PunkteGesamt = PunkteGesamt
        self.PunkteMarktwert = PunkteMarktwert

    def __repr__(self):
        return f"({self.spielerId} {self.spieltagId} {self.Marktwert} {self.Einsätze} {self.PunkteSpieltag} {self.PunkteDurschnitt} {self.PunkteGesamt} {self.PunkteMarktwert})"


def getSession():
    engine = db.create_engine("sqlite:///kickbase.db", echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session

    # spieler1 = Spieler(1, "Felix Zehe", 1, "Barfußbetlehem", "Kampftrinker")
    # spieltag1 = Spieltage(1, 4500000, 7, 100, 230.22, 1924)
    # session.add(spieler1)
    # session.add(spieltag1)
    # session.commit()
