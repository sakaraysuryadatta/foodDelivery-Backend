from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from database import Base
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    seller = Column(String)
    price = Column(Float)
    tax = Column(Float)
    discount = Column(Float)
    total_price = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    items = relationship("OrderItem", back_populates="order_no")
    owner = relationship("User", back_populates="orders")


class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    isveg = Column(Boolean)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order_no = relationship("Order", back_populates="items")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    orders = relationship('Order', back_populates="owner")


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    email = Column(String)
    password = Column(String)
    photo = Column(String)
    items = relationship('Items', back_populates="seller")


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    photo = Column(String)
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    seller = relationship('Seller', back_populates="items")
