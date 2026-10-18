from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def asosiy_menyu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌐 IT Course",
                    callback_data="it_course"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✍🏼 IELTS course",
                    callback_data="ielts_course"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📖 Maktab darsliklari",
                   callback_data="darslar"
                )
            ]
        ]
    )
def it_tugmalar():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💻 Dastulaw boyica qollanma",
                    callback_data="dasturlaw"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✌ orqaga",
                    callback_data="orqaga"
                )
            ]
            
        ]
    )
def ielts_tugmalari():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✍🏼 IELTS malomot",
                    callback_data="ielts_malutmot"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✌ orqaga",
                    callback_data="orqaga"
                )
            ]
        ]
    )
def dars_tugmalari():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1-sinf",
                    callback_data="sinf_1"
                )
            ],
            [
                InlineKeyboardButton(
                    text="2-sinf",
                    callback_data="sinf_2"
                )
            ],
            [
                InlineKeyboardButton(
                    text="3-sinf",
                    callback_data="sinf_3"
                )
            ],
            [
                InlineKeyboardButton(
                    text="4-sinf",
                    callback_data="sinf_4"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✌ orqaga",
                    callback_data="orqaga"
                )
            ]
        ]
        
    )
        
        

