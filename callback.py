from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import utilite


async def call_start(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'start_income':
        await state.update_data(kind_of_pay='income')
        await utilite.get_summa(call.message, state)
    elif call.data == 'start_pay':
        await state.update_data(kind_of_pay='pay')
        await utilite.get_category(call.message, state)
    elif call.data == 'start_stat':
        await state.update_data(stat_date ='stat')
        await utilite.get_stat_date(call.message, state)

async def call_category(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'category_home':
        await state.update_data(kind_of_category='home')
    elif call.data == 'category_food':
        await state.update_data(kind_of_category='food')
    elif call.data == 'category_auto':
        await state.update_data(kind_of_category='auto')
    elif call.data == 'category_save':
        await state.update_data(kind_of_category='save')
    elif call.data == 'category_personal':
        await state.update_data(kind_of_category='personal')
    elif call.data == 'category_rest':
        await state.update_data(kind_of_category='rest')
    await utilite.get_summa(call.message, state)

async def call_date(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'date_01':
        await state.update_data(stat_date='01')
    elif call.data == 'date_02':
        await state.update_data(stat_date='02')
    elif call.data == 'date_03':
        await state.update_data(stat_date='03')
    elif call.data == 'date_04':
        await state.update_data(stat_date='04')
    elif call.data == 'date_05':
        await state.update_data(stat_date='05')
    elif call.data == 'date_06':
        await state.update_data(stat_date='06')
    elif call.data == 'date_07':
        await state.update_data(stat_date='07')
    elif call.data == 'date_08':
        await state.update_data(stat_date='08')
    elif call.data == 'date_09':
        await state.update_data(stat_date='09')
    elif call.data == 'date_10':
        await state.update_data(stat_date='10')
    elif call.data == 'date_11':
        await state.update_data(stat_date='11')
    elif call.data == 'date_12':
        await state.update_data(stat_date='12')
    await utilite.get_date(call.message, state)

async def call_cancel(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer(text='Задача сброшена, начните сначала')
    await utilite.cmd_start(call.message, state)
    await call.answer()