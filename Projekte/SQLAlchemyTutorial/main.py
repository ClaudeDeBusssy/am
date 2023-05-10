import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = db.Column("ssn", db.Integer, primary_key=True)
    firstname = db.Column("firstname", db.String)
    lastname = db.Column("lastname", db.String)
    gender = db.Column("gender", db.CHAR)
    age = db.Column("age", db.Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"


engine = db.create_engine("sqlite:///test_database.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# felixzehe = Person(491241, "Felix", "Zehe", "M", 21)
# session.add(felixzehe)
# session.commit()


results = session.query(Person).filter(Person.firstname == "Felix")
for r in results:
    print(r)
