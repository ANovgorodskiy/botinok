TOKEN = '5913757254:AAGn9Xd-vebTIF75qXuASBj0trSRk5m2wCI'

from aiogram.utils import executor
import random



def fact(numb):
    fact = 1
    for i in range(numb + 1):
        fact *= i
    return fact


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    await message.reply("Привет дорогой\n"
                        "Давно не видел тебя\n"
                        "Наедюсь я смогу тебе помочь. Вот мои команды:\n"
                        "/song – получить топ-5 песен\n"
                        "/game – получить топ-5 игр\n"
                        "/fact n – вычислить n-й факториал\n"
                        "/exams – узнай результаты надвигающихся экзаменов\n")





@dp.message_handler(commands=['song'])
async def get_songs(message: types.Message):

    await message.reply("Вот ТОП-5 песен:\n"
                        "1. Oxxymiron - Хомяк в бульбуляторе\n"
                        "2. Oxxymiron - Хомяк в бульбуляторе\n"
                        "3. Oxxymiron - Хомяк в бульбуляторе\n"
                        "4. Oxxymiron - Хомяк в бульбуляторе\n"
                        "5. Oxxymiron - Хомяк в бульбуляторе\n")


@dp.message_handler(commands=['game'])
async def get_game(message: types.Message):

    await message.reply("Вот ТОП-5 игр:\n"
                        "1. The Witcher 3: Wild Hunt\n"
                        "2. The Elder Scrolls V: Skyrim\n"
                        "3. Grand Theft Auto 5\n"
                        "4. Minecraft\n"
                        "5. Red Dead Redemption 2\n")


@dp.message_handler(commands=['fact'])
async def get_factorial(message: types.Message):

    mes = message.get_args()
    if len(mes) == 0:
        await message.answer("Ты не ввел число!\n")
        return

    arguments = mes.split(' ')

    if len(arguments) != 1:
        await message.answer("Ты ввел много аргументов!\n")
        return

    numb = int(arguments[0])

    await message.answer("Факториал посчитан: " + str(fact(numb)))



@dp.message_handler(commands=['exams'])
async def get_exam_res(message: types.Message):

    results = ['завалил', 'списал', 'ОТЛ', 'НЕУД', 'УД',
            'выгнали за мат в аудитории', 'не пришел']

    res = random.choice(results)

    await message.answer("Твой результат - " + res)

@dp.message_handler(commands=['football'])
async def get_films(message: types.Message):

    await message.reply("VAMOOOOOOOOS")

executor.start_polling(dp, skip_updates=True)