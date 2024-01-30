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
    latitude_decimal = Column(Numeric(precision=9, scale=6))
    longitude_decimal = Column(Numeric(precision=10, scale=7))
    address = Column(Text)
    email = Column(String(500))
    telephone = Column(String(500))
    line = Column(String(500))
    icon = Column(String(500))
    next_process = Column(String(500))
    status = Column(String(2))

    entities = relationship('Entity')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'coordinates': [self.latitude_decimal, self.longitude_decimal],
            'address': self.address,
            #'telephone': self.telephone,
        }

class Entity(Base):
    STATUS_CHOICES = (
        ('F', 'Free'),
        ('O', 'Occupied'),
    )

    STATUS_FREE = 'F'
    STATUS_OCCUPIED = 'O'

    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    store_id = Column(Integer, ForeignKey('store.id', ondelete='SET NULL'), nullable=True)
    status = Column(String(10)) # F: free, O: occupied

    store = relationship('Store', overlaps='entities')

    @staticmethod
    def find_free(store_id=None, is_one=False):
        query = Entity.query.filter(Entity.status==Entity.STATUS_CHOICES[0][0])
        if store_id:
            query = query.filter(Entity.store_id==store_id)

        if is_one:
            return query.first()

        return query.all()


class Lending(Base):
    __tablename__ = 'lending'

    STATUS_CHOICES = (
        ('L', 'lend'),
        ('R', 'returned')
    )
    STATUS_LEND = 'L'
    STATUS_RETURNED = 'R'

    id = Column(Integer, primary_key=True)
    person = Column(String(500))
    phone = Column(String(500))
    email = Column(String(500))
    date_start = Column(Date)
    date_end = Column(Date)
    store_id = Column(Integer, ForeignKey('store.id', ondelete='SET NULL'), nullable=True)
    entity_id = Column(Integer, ForeignKey('entity.id', ondelete='SET NULL'), nullable=True)
    remarks = Column(Text)
    status = Column(String(10), default='L') # L: lend, R: returned

    store = relationship('Store')
    entity = relationship('Entity')

    @classmethod
    def admin_save(self, obj):
        #print(self, self.status, obj.status, flush=True)
        if obj.status == self.STATUS_RETURNED:
            if entity := session.get(Entity, obj.entity_id):
                entity.status = Entity.STATUS_FREE
                session.commit()

class LendLog(Base):
    __tablename__ = 'lend_log'

    id = Column(Integer, primary_key=True)
    memo = Column(String(500))
    entity_id = Column(Integer, ForeignKey('entity.id', ondelete='SET NULL'), nullable=True)
    entity = relationship('Entity')
