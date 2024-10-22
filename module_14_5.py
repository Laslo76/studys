from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import api_key
import crud_functions_ as db


bot = Bot(token=api_key.my_api)
dp = Dispatcher(bot, storage=MemoryStorage())

first_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]
        ], resize_keyboard=True)

second_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calc')
button_formula = InlineKeyboardButton(text='Формулы расчёта', callback_data='calc_info')
second_kb.add(button_calc)
second_kb.add(button_formula)

buy_kb = InlineKeyboardMarkup(resize_keyboard=True)
buy_but = [InlineKeyboardButton(text=f'{i[1]}', callback_data='product_buying') for i in db.get_all_products()]
buy_kb.row(*buy_but)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class UserRegistration(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def start_messages(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=first_kb)


@dp.message_handler(text="Информация")
async def get_info(message):
    await message.answer("Программа расчета потребности калорий на основе формулы Миффлина - Сан Жеора")


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    products = db.get_all_products()
    for prod in products:
        with open(f'{prod[3]}', 'rb') as img:
            await message.answer_photo(img, f'Название: {prod[1]} | Описание: {prod[2]} | Цена: {prod[4]}')
    await message.answer(f'Выберите продукт для покупки:', reply_markup=buy_kb)


@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Выберите опцию:", reply_markup=second_kb)


@dp.message_handler(text="Регистрация")
async def registration(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await UserRegistration.username.set()


@dp.callback_query_handler(text='calc')
async def start_call(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.callback_query_handler(text='calc_info')
async def info_call(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=float(message.text))
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=float(message.text))
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()

    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()


@dp.message_handler(state=UserRegistration.username)
async def set_username(message, state):
    if message.text != '' and not db.is_include(message.text):
        print(not db.is_include(message.text))
        await state.update_data(username=str(message.text))
        await message.answer("Введите свой email:")
        await UserRegistration.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя:")
        await UserRegistration.username.set()


@dp.message_handler(state=UserRegistration.email)
async def set_email(message, state):
    if message != '':
        await state.update_data(email=message.text)
        await message.answer("Введите свой возраст:")
        await UserRegistration.age.set()
    else:
        await message.answer("Введите свой email:")
        await UserRegistration.email.set()


@dp.message_handler(state=UserRegistration.age)
async def set_age(message, state):
    try:
        await state.update_data(age=int(message.text))
    except Exception as e:
        await message.answer("Введите свой возраст:")
        await UserRegistration.age.set()

    data = await state.get_data()
    db.add_user(data['username'], data['email'], data['age'], 1000)
    await message.answer(f"Пользователь {data['username']} зарегистрирован")
    await state.finish()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
