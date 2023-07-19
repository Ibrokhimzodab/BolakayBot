from app import dp, bot, types
from .model import User, Group
from db.state import AdminState
from .adminKeyboards import menuAdminKeyboard, cancelKeyboard
from .adminI18 import menuAdminKb, mainMenuAdmin, cancel
from .keyboards import menuKeyboard
from .i18 import mainMenu
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['admin'])
async def checkAdmin(message: types.Message):
    if User.isUserAdmin(message.from_user.id):
        await AdminState.menu.set()
        return await bot.send_message(message.chat.id, mainMenuAdmin, reply_markup=menuAdminKeyboard)


@dp.message_handler(Text(equals=menuAdminKb), state=AdminState.menu)
async def adminMenu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['menu'] = message.text
        if message.text == menuAdminKb[0]:
            users = User.getAllUsers()
            user_data_list = []
            for user in users:
                user_data = f"User ID: {user.id}, Chat ID: {user.chatId}, Name: {user.name}, Phone: {user.phone}, isActive: {user.isActive}"
                user_data_list.append(user_data)

            all_users_data = '\n\n'.join(user_data_list)
            all_users_data_with_count = f"{all_users_data}\n\nTotal Users: {len(user_data_list)}"
            await bot.send_message(message.chat.id, all_users_data_with_count)
            return await AdminState.menu.set()
        elif message.text == menuAdminKb[1]:
            groups = Group.getAll()
            groupDataList = []
            for group in groups:
                groupData = f"Group ID: {group.id}, Chat ID: {group.groupId}, Name: {group.name}, " \
                            f"Type: {'qoy' if group.typeId == 1 else 'echki'}, isActive: {group.isActive}"
                groupDataList.append(groupData)

            allGroupDataList = '\n\n'.join(groupDataList)
            await bot.send_message(message.chat.id, allGroupDataList)
            return await AdminState.menu.set()
        elif message.text == menuAdminKb[2]:
            await bot.send_message(message.chat.id, "Send group id / group name / type\n"
                                                    "Example:\n"
                                                    "-100136723/ECHKI GROUP/2\n"
                                                    "-100131341/QOY GROUP/1", reply_markup=cancelKeyboard)
            return await AdminState.addState.set()
        elif message.text == menuAdminKb[3]:
            await bot.send_message(message.chat.id, "Send user id", reply_markup=cancelKeyboard)
            return await AdminState.addState.set()
        elif message.text == menuAdminKb[4]:
            await bot.send_message(message.chat.id, "Send user id to ban/activate", reply_markup=cancelKeyboard)
            return await AdminState.banState.set()
        elif message.text == menuAdminKb[5]:
            await bot.send_message(message.chat.id, "Send group id to ban/activate", reply_markup=cancelKeyboard)
            return await AdminState.banState.set()
        elif message.text == menuAdminKb[6]:
            user = User.getUser(message.chat.id)
            return await bot.send_message(message.chat.id, mainMenu[user.language],
                                          reply_markup=menuKeyboard[user.language])
        #     # TODO: send advertisement


@dp.message_handler(lambda message: message.text, state=AdminState.addState)
async def addAdminOrGroup(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        menu = data["menu"]
        if message.text == cancel:
            await AdminState.menu.set()
            return await bot.send_message(message.chat.id, mainMenuAdmin, reply_markup=menuAdminKeyboard)
        if menu == menuAdminKb[2]:
            chat_id, name, group_type = message.text.split("/")
            Group(groupId=chat_id, name=name, typeId=group_type).save()
            await bot.send_message(message.chat.id, "Group added", reply_markup=menuAdminKeyboard)
            return await AdminState.menu.set()
        elif menu == menuAdminKb[3]:
            User.setUserToAdmin(message.text)
            await bot.send_message(message.chat.id, "User role changed to admin", reply_markup=menuAdminKeyboard)
            return await AdminState.menu.set()


@dp.message_handler(lambda message: message.text, state=AdminState.banState)
async def banUserOrGroup(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        menu = data["menu"]
        if message.text == cancel:
            await AdminState.menu.set()
            return await bot.send_message(message.chat.id, mainMenuAdmin, reply_markup=menuAdminKeyboard)
        if menu == menuAdminKb[5]:
            Group.changeGroupStatus(message.text)
            await bot.send_message(message.chat.id, "Group status changed", reply_markup=menuAdminKeyboard)
            return await AdminState.menu.set()
        elif menu == menuAdminKb[4]:
            User.changeUserStatus(message.text)
            await bot.send_message(message.chat.id, "User status changed", reply_markup=menuAdminKeyboard)
            return await AdminState.menu.set()
