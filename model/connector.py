from .model_wrapper import ModelWrapper
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.models import Base


class Connector(ModelWrapper):
    def __init__(self, db):
        self.engine = create_engine(db)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def update_model(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    con = Connector()
    con.update_model()
    con.session.commit()