from aiogram import Router, types
from aiogram.filters import Command

router = Router(name=__name__)

@router.message(Command('pay', prefix='!/'))
async def pay(message: types.Message):
    await message.answer(
        text='Оплата'
    )