import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import message
from button5 import menu,menu2,menu4,menu3,menu5,menu6,menu7,menu8,menu9,menu10,menu12,menu11,menu16,menu15,menu13,menu14




logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token='5017645039:AAGSqLmQDHtDdzIEnUuVK1uw5Ln4GRfBhCg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f" Привет {user}, это тест бот", reply_markup=menu2)
    await message.answer(f"Выбирайте предмет")





@dp.message_handler(Text(equals=["Математика"]))
async def accoun(message: types.Message):
    await message.answer(f" Выбирайте класс", reply_markup=menu)


@dp.message_handler(Text(equals=["Физика"]))
async def accoun(message: types.Message):
    await message.answer(f" Выбирайте класс", reply_markup=menu4)

@dp.message_handler(Text(equals=["Химия"]))
async def accoun(message: types.Message):
    await message.answer(f" Выбирайте класс", reply_markup=menu3)


@dp.message_handler(Text(equals=["Математика 5 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Представьте в виде неправильной дроби 5 2/3 . В ответе запишите числитель полученной дроби.", reply_markup=menu5)



@dp.message_handler(Text(equals=["Математика 6 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Какие делители числа 68", reply_markup=menu6)



@dp.message_handler(Text(equals=["Математика 7 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Упростите 5(2а+1) - 3.", reply_markup=menu7)




@dp.message_handler(Text(equals=["Математика 8 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"x >= 6. x - ?", reply_markup=menu12)




@dp.message_handler(Text(equals=["Математика 9 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Решите неравенство:(x-13)*(x-29)=>0", reply_markup=menu11)

# @dp.message_handler(Text(equals=["9 класс"]))
# async def accoun(message: types.Message):
#     await message.answer(f"Выбирайте класс", reply_markup=menu2)





@dp.message_handler(Text(equals=["Вернуться назад"]))
async def accoun(message: types.Message):
    await message.answer("Выбирайте предмет ", reply_markup=menu2)


@dp.message_handler(Text(equals=["Вернуться  назад"]))
async def accoun(message: types.Message):
    await message.answer("Выбирайте предмет ", reply_markup=menu2)



@dp.message_handler(Text(equals=["Вернуться   назад"]))
async def accoun(message: types.Message):
    await message.answer("Выбирайте предмет ", reply_markup=menu2)





@dp.message_handler(Text(equals=["Химия 7 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Что изучает наука химия?", reply_markup=menu8)



@dp.message_handler(Text(equals=["Химия 8 класс"]))
async def accoun(message: types.Message):
    await message.answer(f" Для защиты от коррозии используют металл – ......", reply_markup=menu10)


@dp.message_handler(Text(equals=["Химия 9 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Выберите вещество, которое реагирует с раствором хлорида алюминия.", reply_markup=menu9)


@dp.message_handler(Text(equals=["Физика 6 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Какое из трех слов обозначает физическое тело?", reply_markup=menu13)





@dp.message_handler(Text(equals=["Физика 7 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Чтo тaкoe физикa?", reply_markup=menu14)






@dp.message_handler(Text(equals=["Физика 8 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"Какая энергия выделяется при отвердевании алюминия массой 20 кг, взятого при температуре отвердевания?", reply_markup=menu15)


@dp.message_handler(Text(equals=["Физика 9 класс"]))
async def accoun(message: types.Message):
    await message.answer(f"В начале 17 века стали говорить, что тело, получившие после натирания способность притягивать другие тела наэлектризовано. О каких явлениях идет речь", reply_markup=menu16)


@dp.message_handler(Text(equals=["17/3"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)


@dp.message_handler(Text(equals=["17/5"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)






@dp.message_handler(Text(equals=["15/17"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["1,2,68,34,17"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)





@dp.message_handler(Text(equals=["7,9,46,7"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)





@dp.message_handler(Text(equals=["1, 7, 8, 32, 16"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["10а+5-3"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["10а"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["10а-2"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)





@dp.message_handler(Text(equals=["[13; 29]"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["(13;29)"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["0;13"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)


@dp.message_handler(Text(equals=["(-∞; 6)"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)


@dp.message_handler(Text(equals=["(-∞; 6]"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["(6; +∞]"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)


@dp.message_handler(Text(equals=["Вещества, их свойства и превращения"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["Деление живых клеток"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["Болезни и их лечение"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["сульфат бария"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["оксид магния"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)






@dp.message_handler(Text(equals=["гидроскид натрия"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["серебро"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["кобальт"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["цинк"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)






@dp.message_handler(Text(equals=["Кипение"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["Скорость"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)





@dp.message_handler(Text(equals=["Самолёт"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)



@dp.message_handler(Text(equals=["наука о природе"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)





@dp.message_handler(Text(equals=["наука изучающее электричество"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)





@dp.message_handler(Text(equals=["наука изучающий тела"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["2,3 МДж"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)


@dp.message_handler(Text(equals=["2 МДж"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["7,8 МДж"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["элктрических"]))
async def acc(message: types.Message):
     await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-2.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["Магнитных"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)




@dp.message_handler(Text(equals=["химических"]))
async def accoun(message: types.Message):
    await message.answer_photo('https://cf2.ppt-online.org/files2/slide/f/Fjbqcw7ILUi6n9aS0pPelNYOEvHGJXsMd5k8uDQTh/slide-3.jpg',reply_markup = menu2)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


















