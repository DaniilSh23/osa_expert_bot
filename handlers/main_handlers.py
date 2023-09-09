from pyrogram import Client, filters
from pyrogram.types import Message

from keyboards.bot_keyboards import form_webapp_kbrd
from utils.req_to_bot_api import post_for_write_user, get_gpt_answer
from settings.config import MY_LOGGER, NEW_APPLICATION_FORM_URL


@Client.on_message(filters.command(['start', 'menu']))
async def start_handler(_, update):
    """
    Хэндлер для старта бота
    """
    MY_LOGGER.info(f'Сработал стартовый хэндлер для юзера {update.from_user.id!r}')
    write_usr_rslt = await post_for_write_user(tlg_username=update.from_user.username, tlg_id=update.from_user.id)
    if write_usr_rslt:
        await update.reply_text(
            text=f'👋 Привет!\n\n🐝 Я бот с ИИ, представляю компанию <b>"ОСА Автоэксперт"</b>.\n\n'
                 f'🎯 Наша цель - <b>содействия автомобилистам</b> в сложных дорожных ситуациях.\n\n'
                 f'🤝 Вот часть проблем, которые мы помогаем решить людям:\n'
                 f'🔹 некачественный ремонт и обман со стороны автосервисов\n'
                 f'🔹 уклонение от выплат страховыми компаниями\n'
                 f'🔹 отстаивание Ваших прав в суде и многое другое...\n\n'
                 f'🖋 Напишите мне Ваш вопрос, чтобы я смог предварительно Вам помочь.\n\n<b>Например:</b>\n'
                 f'<i>Страховая отказывается принять документы, не могу получить выплату, что делать?</i>\n'
                 f'<i>Что обязан автосервис, если сломался автомобиль после некачественного ремонта?</i>\n'
                 f'<i>Произошло ДТП, что нужно обязательно сделать, чтобы потом получить возмещение ущерба?</i>\n\n'
                 f'👨‍💼 Или можете сразу <b>оставить заявку</b>, чтобы связаться со специалистом.',
            reply_markup=await form_webapp_kbrd(form_link=NEW_APPLICATION_FORM_URL,
                                                btn_text='📱 Связаться со специалистом')
        )

    else:
        MY_LOGGER.error(f'Юзер {update.from_user.id!r} получил сообщение, что у бота тех работы!')
        await update.reply_text(
            text=f'У бота технические работы. Мы скоро закончим.🪛'
        )


@Client.on_message(filters.private)
async def ai_answer_handler(_, update: Message):
    """
    Хэндлер для обработки вопросов пользователей и ответов через ChatGPT.
    """
    MY_LOGGER.info(f'Сработал хэндлер для ИИ ответов пользователю {update.from_user.id!r}')
    info_msg = await update.reply_text(
        text=f'<b>🐝 ИИ "OSA_GPT"</b> генерирует ответ, нужно немного подождать...⏱',
        disable_notification=True,
    )
    gpt_answer = await get_gpt_answer(user_msg=update.text)
    await info_msg.delete()
    if not gpt_answer:
        await update.reply_text(text=f'🤷‍♂️ К сожалению, <b>ИИ не смог сгенерировать ответ</b> из-за перегрузки '
                                     f'сервера. Пожалуйста, попробуйте повторить запрос позже ⌛️')
        return

    await update.reply_text(
        text=f"<b>Ответ искусственного интеллекта '🐝 OSA_GPT':</b>\n\n{gpt_answer.get('gpt_answer')}",
        reply_markup=await form_webapp_kbrd(form_link=NEW_APPLICATION_FORM_URL,
                                            btn_text='📱 Связаться со специалистом')
    )
