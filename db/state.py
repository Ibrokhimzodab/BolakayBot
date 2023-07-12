from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminLoginState(StatesGroup):
    password = State()


class AdminSystemMessageState(StatesGroup):
    message = State()


class AdminUserAddState(StatesGroup):
    telegramId = State()
    username = State()
    name = State()


class PerformIdState(StatesGroup):
    performid = State()


class AdminSendMessage(StatesGroup):
    message = State()


class AdminAdsMessage(StatesGroup):
    message_photo = State()


class RegisterState(StatesGroup):
    language = State()
    name = State()
    phone = State()


class FirstState(StatesGroup):
    subMenu = State()
    type = State()
    sale = State()
    photo = State()
    description = State()
    fromLoc = State()
    whereLoc = State()
    send = State()
