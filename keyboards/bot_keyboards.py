from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from keyboards.bot_buttons import BUTTONS_DCT


async def form_webapp_kbrd(form_link, btn_text):
    """
    Формирование клавиатуры с одной WebApp кнопкой
    :param form_link: ссылка на веб-форму.
    :param btn_text: текст кнопки.
    """
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text=btn_text,
                web_app=WebAppInfo(url=form_link)
            )
        ],
    ])

CANCEL_SEND_COMMENT_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['COME_BACK_LATER'],
    ],
])
