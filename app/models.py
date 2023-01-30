from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String,
    Text,
    DateTime,
    Date,
    Boolean,
    ForeignKey,
    Table,
    desc,
)
from sqlalchemy.orm import (
    relationship,
    backref,
    validates,
)
#from sqlalchemy.dialects.postgresql import JSONB
#from sqlalchemy.ext.declarative import declared_attr
from flask_login import UserMixin

from app.database import (
    Base,
    session,
    TimestampMixin,
)

class User(Base, UserMixin, TimestampMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(500))
    passwd = Column(String(500))
    phone = Column(String(500))
    email = Column(String(500))
    status = Column(String(1), default='P')
    # is_admin
    admin_store_id = Column(Integer, ForeignKey('store.id', ondelete='SET NULL'), nullable=True)
    admin_store = relationship('Store')

class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    title = Column(String(500))

class Entity(Base):
    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    store_id = Column(Integer, ForeignKey('store.id', ondelete='SET NULL'), nullable=True)
    store = relationship('Store')


class LendLog(Base):
    __tablename__ = 'lend_log'

    id = Column(Integer, primary_key=True)
    memo = Column(String(500))
    entity_id = Column(Integer, ForeignKey('entity.id', ondelete='SET NULL'), nullable=True)
    entity = relationship('Entity')
