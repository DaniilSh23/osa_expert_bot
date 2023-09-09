import os
import sys

import loguru
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN', '123456:dadwdawd')
BOT_USERNAME = os.environ.get('BOT_USERNAME', 'CourseTrainBot')
API_ID = os.environ.get('API_ID', '1234567890')
API_HASH = os.environ.get('API_HASH', 'какой-то там хэш')
BOT_MANAGER_ID = os.environ.get('BOT_MANAGER_ID', 1978587604)
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'ключик от API OpenAI')

# Абсолютный путь к директории проекта
BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# Константы для API Django проекта
BASE_HOST_URL = os.environ.get('BASE_HOST_URL', 'http://127.0.0.1:8000/')
WRITE_USR_URL = f'{BASE_HOST_URL}osa_gpt/write_usr/'
GET_ANSWER_GPT = f'{BASE_HOST_URL}osa_gpt/answer_gpt/'

# Ссылки на веб-страницы
BASE_FORM_PAGE_URL = os.environ.get('BASE_FORM_PAGE_URL', 'https://danyasevas111.fvds.ru/')
NEW_APPLICATION_FORM_URL = f'https://danyasevas111.fvds.ru/osa_gpt/new_application/'
# NEW_APPLICATION_FORM_URL = 'https://ya.ru'  # Todo: удалить, это для теста


# Настройки логгера
MY_LOGGER = loguru.logger
MY_LOGGER.remove()  # Удаляем все предыдущие обработчики логов
MY_LOGGER.add(sink=sys.stdout, level='DEBUG')   # Все логи от DEBUG и выше в stdout
MY_LOGGER.add(  # системные логи в файл
    sink=f'{BASE_DIR}/logs/sys_log.log',
    level='DEBUG',
    rotation='2 MB',
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=True
)

# Словари для хранения чего-либо
WORKING_CLIENTS = dict()    # Словарь для запущенных клиентов
CLIENT_CHANNELS = dict()    # Каналы для запущенных клиентов
STATES_DCT = dict()     # Состояния бота

