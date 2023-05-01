import eel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_URI
from model.userVO import User


engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)

# Create a declarative base object
Base = declarative_base()
# Add User Object to Base and create the table
Base.metadata.create_all(bind=engine, tables=[User.__table__])

from exposeAPI.userEel import UserAPI
user_eel = UserAPI(Session)
eel.expose(user_eel.add_user)
eel.expose(user_eel.get_users)

eel.init('web')
eel.start('index.html', size=(1000, 800))