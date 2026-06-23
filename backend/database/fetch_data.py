from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helpers.config import settings

DATABASE_URL = f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.Endpoint}:{settings.port}/{settings.database}"


engine = create_engine(DATABASE_URL)
Base = declarative_base()

class ClientInfo(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(225))
    docker_image = Column(String(50))
    port = Column(Integer)
    health_point = Column(String(50))
    status = Column(String(50))

Session = sessionmaker(bind=engine)
session = Session()

class Fetch():

    @staticmethod
    def take_for_deploy(id):

        result =  session.query(
            ClientInfo.docker_image,
            ClientInfo.port,
            ClientInfo.health_point,
            ClientInfo.email,
            ClientInfo.name
        ).filter(
            ClientInfo.id == id
        ).first()

        return result


