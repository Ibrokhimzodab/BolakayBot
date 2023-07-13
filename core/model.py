from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, JSON
from db.setup import session, Base, engine


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    groupId = Column(BigInteger)
    name = Column(String)

    def __init__(self, groupId, name):
        self.groupId = groupId
        self.name = name

    @classmethod
    def getAll(cls):
        return session.query(Group).all()

    def save(self):
        session.add(self)
        session.commit()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    userId = Column(BigInteger)
    chatId = Column(BigInteger)
    name = Column(String)
    phone = Column(String, unique=True)
    language = Column(Integer)
    isAdmin = Column(Boolean)

    def __init__(self, userId, chatId, name, phone, language):
        self.userId = userId
        self.chatId = chatId
        self.name = name
        self.phone = phone
        self.language = language

    @classmethod
    def isUserAdmin(cls, userId):
        user = session.query(User).filter_by(userId=userId).first()
        return user.isAdmin

    @classmethod
    def isPhoneRegistered(cls, phone):
        user = session.query(User).filter_by(phone=phone).first()
        return user is not None

    @classmethod
    def isRegistered(cls, userId):
        user = session.query(User).filter_by(userId=userId).first()
        return user is not None

    @classmethod
    def getUser(cls, chatId):
        user = session.query(User).filter_by(chatId=chatId).first()
        return user

    @classmethod
    def getAllUsers(cls):
        return session.query(User).all()

    @classmethod
    def changeLang(cls, userId, lang):
        user = session.query(User).filter_by(userId=userId).first()
        user.language = lang
        user.save()

    def save(self):
        session.add(self)
        session.commit()

Base.metadata.create_all(engine)
