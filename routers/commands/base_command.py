from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown

router = Router(name=__name__)

# Обработка команды старт
@router.message(CommandStart())
async def handle_start(message: types.Message):

    await message.answer(
        text=f"Привет, {markdown.hbold(message.from_user.full_name)}!\n"
             f"Напишите команду /info если не знаете для чего нужен данный бот!\n"
             f"Если знаете то напишите /pay ",
        parse_mode=ParseMode.HTML,
    )

#Информация о боте
@router.message(Command('info', prefix='!/'))
async def handler_info_command(message: types.Message):
    await message.answer(
        text='Данный бот предназначен для оплаты входя в приватный телеграмм канал\n'
             'Как это работает?\n'
             '1: Вы перечисляете сумму на номер кошелька\n'
             '2: После перевода суммы вас добавляют в приватный телеграмм канал',
    )
