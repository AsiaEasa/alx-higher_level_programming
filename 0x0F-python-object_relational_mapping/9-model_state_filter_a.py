#!/usr/bin/python3
"""
Script that lists State objects with a  from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    if len(argv) != 4:
         print("Usage: {} <mysql_username> <mysql_password> <database_name>"
               .format(argv[0]))
         exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_a = session.query(State).filter(State.name.like('%a%'))
   for state in states_a:
        print("{}: {}".format(state.id, state.name))
   session.close()
