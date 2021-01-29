from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

id = "root"
password = "1q2w3e4r5t"
host = "localhost"
db_name = "covid"

def getSession():
    
    engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4".format(id, password, host, db_name), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    return session