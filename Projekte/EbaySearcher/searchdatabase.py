import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


class SearchDatabaseClass():
    def __init__(self):
        self.engine = db.create_engine("sqlite:///test_database.db", echo=True)

        self.base = declarative_base().metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


class ebayEntries(declarative_base()):
    __tablename__ = "ebayEntries"

    id = db.Column("id", db.Integer, primary_key=True)

    text = db.Column("text", db.String)
    price = db.Column("price", db.Numeric(10, 2))
    place = db.Column("place", db.String)
    link = db.Column("link", db.String)

    def __init__(self, id, text, price, place, link):
        self.id = id
        self.text = text
        self.price = price
        self.place = place
        self.link = link

    def __repr__(self):
        return f"({self.id}) {self.text} {self.price} {self.place}"


# felixzehe = Person(491241, "Felix", "Zehe", "M", 21)
# session.add(felixzehe)
# session.commit()


# results = session.query(Person).filter(Person.firstname == "Felix")
# for r in results:
#     print(r)

nesdc = SearchDatabaseClass()
