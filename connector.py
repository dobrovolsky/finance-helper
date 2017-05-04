import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.model_wrapper import ModelWrapper
from model.models import Base


class Connector:
    def __init__(self, db):
        self.engine = create_engine(db)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def update_model(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    con = Connector(db=os.environ['DB'])
    con.update_model()
    con.session.add(ModelWrapper.add_user('user', '#1', 'user@user.com'))
    con.session.commit()
