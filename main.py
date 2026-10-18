import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery,FSInputFile

from buttons import(
    asosiy_menyu,it_tugmalar,ielts_tugmalari,dars_tugmalari
)

TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(
        "xuw kelibsan ✌",
        reply_markup=asosiy_menyu()
)
@dp.callback_query(F.data=="it_course")
async def it_course(callback:CallbackQuery):
    await callback.message.edit_text("it course bolimni tanlang!",reply_markup=it_tugmalar())
    await callback.answer()

@dp.callback_query(F.data=="ielts_course")
async def ielts_course(callback:CallbackQuery):
    await callback.message.edit_text("ielts bolmini tanlang!",reply_markup=ielts_tugmalari())
    await callback.answer()
@dp.callback_query(F.data=="darslar")
async def darsliklar(callback:CallbackQuery):
    await callback.message.edit_text("sinfni tanlang!",reply_markup=dars_tugmalari())
    await callback.answer()

@dp.callback_query(F.data=="sinf_1")
async def sinf_1(callback:CallbackQuery):
    rasm=FSInputFile("muwuk.webp")
    await callback.message.answer_photo(photo=rasm)
    await callback.answer()
@dp.callback_query(F.data=="sinf_2")
async def sinf_2(callback:CallbackQuery):
    rasm=FSInputFile("2_sinf.webp")
    await callback.message.answer_photo(photo=rasm)
    await callback.answer()
@dp.callback_query(F.data=="sinf_3")
async def sinf_3(callback:CallbackQuery):
    rasm=FSInputFile("3_sinf.webp")
    await callback.message.answer_photo(photo=rasm)
    await callback.answer()
@dp.callback_query(F.data=="sinf_4")
async def sinf_4(callback:CallbackQuery):
    rasm=FSInputFile("4_sinf.webp")
    await callback.message.answer_photo(photo=rasm)
    await callback.answer()
async def main():
    await dp.start_polling(bot)
if __name__=="__main__":
    asyncio.run(main())