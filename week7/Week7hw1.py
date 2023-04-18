from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection string
db_string = "sqlite:///films_db.sqlite"

# Create an engine object to interact with the database
engine = create_engine(db_string, echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Film class with the required columns
class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

# Create the table(s) in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Part 2: Manipulating with Database

# Add 3 films to the films table
film1 = Film(title='Star Wars: Episode I - The Phantom Menace', director='George Harrison', release_year=1999)
film2 = Film(title='Dark City', director='Alex Proyas', release_year=1998)
film3 = Film(title='The Lord of the Rings: The Return of the King', director='Peter Jackson', release_year=2003)
session.add_all([film1, film2, film3])
session.commit()

# Update one film
film = session.query(Film).filter_by(title='Star Wars: Episode I - The Phantom Menace').first()

if film is not None:
    film.director = 'George Lucas'
    session.commit()
else:
    print("Film not found")
# Print data from table
films = session.query(Film).all()
for film in films:
    print(f'{film.title} directed by {film.director} released in {film.release_year}')

# Delete all data from table
session.query(Film).delete()
session.commit()

