from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DECIMAL

Base = declarative_base()


class PrimaryField:
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(PrimaryField, Base):
    __tablename__ = 'users'

    first_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    email = Column(String(length=255), nullable=False, unique=True)
    phone = Column(String(length=20))

    items = relationship('Item', back_populates='user')
    accounts = relationship('Account', back_populates='user')
    categories = relationship('Category', back_populates='user')

    def __repr__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Account(PrimaryField, Base):
    __tablename__ = 'accounts'

    name = Column(String(length=30), nullable=False)
    amount = Column(DECIMAL, nullable=False)
    user_id = Column('user_id', ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    user = relationship('User', back_populates='accounts')


class Category(PrimaryField, Base):
    __tablename__ = 'categories'

    name = Column(String(30), nullable=False)
    description = Column(String(500))

    items = relationship('Item', back_populates='category')
    user_id = Column('user_id', ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    user = relationship('User', back_populates='categories')

    def __repr__(self):
        return self.name


class Item(PrimaryField, Base):
    __tablename__ = 'items'

    name = Column(String(30), nullable=False)
    price = Column(DECIMAL, nullable=False)
    count = Column(Integer, nullable=False)
    description = Column(String(500))
    category_id = Column('category_id', ForeignKey('categories.id', ondelete='RESTRICT', onupdate='CASCADE'),
                         nullable=False)
    date = Column(Date)

    user_id = Column('user_id', ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    user = relationship('User', back_populates='items')
    category = relationship('Category', back_populates='items')

