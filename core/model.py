from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, JSON
from db.setup import session, Base, engine


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    groupId = Column(BigInteger)
    name = Column(String)
    typeId = Column(Integer)
    isActive = Column(Boolean)

    def __init__(self, groupId, name, typeId):
        self.groupId = groupId
        self.name = name
        self.typeId = typeId
        self.isActive = True

    @classmethod
    def getAll(cls):
        return session.query(Group).order_by(Group.id)

    @classmethod
    def changeGroupStatus(cls, Id):
        group = session.query(Group).filter_by(id=Id).first()
        group.isActive = not group.isActive
        group.save()

    @classmethod
    def getAllWithTypeId(cls, typeId):
        return session.query(Group).filter_by(typeId=typeId).all()

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
    isActive = Column(Boolean)
    isAdmin = Column(Boolean)

    def __init__(self, userId, chatId, name, phone, language):
        self.userId = userId
        self.chatId = chatId
        self.name = name
        self.phone = phone
        self.language = language
        self.isActive = True
        self.isAdmin = False

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
    def changeLang(cls, userId, lang):
        user = session.query(User).filter_by(userId=userId).first()
        user.language = lang
        user.save()

    @classmethod
    def getAllUsers(cls):
        return session.query(User).order_by(User.id)

    @classmethod
    def isUserAdmin(cls, chatId):
        user = session.query(User).filter_by(chatId=chatId, isAdmin=True).first()
        return user is not None

    @classmethod
    def setUserToAdmin(cls, Id):
        user = session.query(User).filter_by(id=Id).first()
        user.isAdmin = True
        user.save()

    @classmethod
    def changeUserStatus(cls, Id):
        user = session.query(User).filter_by(id=Id).first()
        user.isActive = not user.isActive
        user.save()

    def save(self):
        session.add(self)
        session.commit()

Base.metadata.create_all(engine)
