from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, JSON
from db.setup import session, Base, engine


# Define the 'Admin' table
class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)

    def __init__(self, user_id):
        self.user_id = user_id

    @classmethod
    def is_admin(self, user_id):
        admin = session.query(Admin).filter_by(user_id=user_id).first()

        return admin is not None

    def register(self, user_id):
        if not self.__class__.is_admin(user_id):
            self.user_id = user_id
            self.save()

    def save(self):
        session.add(self)
        session.commit()

Base.metadata.create_all(engine)
