from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import api_key


bot = Bot(token=api_key.my_api)
dp = Dispatcher(bot, storage=MemoryStorage())

first_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')]
        ], resize_keyboard=True)

second_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calc')
button_formula = InlineKeyboardButton(text='Формулы расчёта', callback_data='calc_info')
second_kb.add(button_calc)
second_kb.add(button_formula)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_messages(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=first_kb)


@dp.message_handler(text="Информация")
async def get_info(message):
    await message.answer("Программа расчета потребности калорий на основе формулы Миффлина - Сан Жеора")


@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Выберите опцию:", reply_markup=second_kb)


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


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
