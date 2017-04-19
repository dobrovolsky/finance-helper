from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from model.qvariant_alchemy import Integer, String, Date, DECIMAL

Base = declarative_base()


class PrimaryField:
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(PrimaryField, Base):
    __tablename__ = 'users'

    first_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    email = Column(String(length=255), nullable=False, unique=True)
    phone = Column(String(length=20))

    item_lists = relationship('ItemList', back_populates='user')

    def __repr__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Category(PrimaryField, Base):
    __tablename__ = 'categories'

    name = Column(String(30), nullable=False)
    description = Column(String(500))

    items = relationship('Item', back_populates='category')

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

    category = relationship('Category', back_populates='items')
    item_lists = relationship('ItemList', back_populates='item')


class ItemList(PrimaryField, Base):
    __tablename__ = 'item_list'

    date = Column(Date)

    item_id = Column('item_id', ForeignKey('items.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    user_id = Column('user_id', ForeignKey('users.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)

    user = relationship('User', back_populates='item_lists')
    item = relationship('Item', back_populates='item_lists')
