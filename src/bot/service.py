from dataclasses import dataclass
from typing import Coroutine
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup
from src.bot.keyboard import exit_keyboard
from src.bot.models import SubscriberModel
from src.bot.state import StateData
from src.settings.bot import dispatcher, bot
from src.user.service import UserService


@dataclass
class BotService:
    """Сервис бота"""

    @staticmethod
    @dispatcher.message(Command("start"))
    async def start_message(message: Message) -> Message:
        chat_id = message.chat.id
        await bot.send_message(chat_id=chat_id, text="ну привет")

    @staticmethod
    @dispatcher.message(Command("subscribe"))
    async def user_subscribe(message: Message) -> Message:
        """Подписка на рассылку"""
        user_service = UserService()
        user = await user_service.get_user_by_telegram(message.chat.id)
        if user:
            await bot.send_message(chat_id=message.chat.id, text="Вы уже подписаны на рассылку")
            return False
        user = SubscriberModel(telegram=message.chat.id)
        await user_service.add_user(user)
        await bot.send_message(chat_id=message.chat.id, text="успешно подписаны на уведомления")

    @staticmethod
    @dispatcher.message(Command("send"))
    async def send_message_to_subscriber(message: Message, state: FSMContext) -> Message:
        """запуск диалога создания сообщения"""
        buttons = ReplyKeyboardMarkup(keyboard=exit_keyboard)
        await message.answer(
            "Напишите сообщение для отправки или нажмите на кнопку для отмены",
            reply_markup=buttons,
        )
        await state.set_state(StateData.message_text)

    @staticmethod
    @dispatcher.message(StateData.message_text)
    async def process_send(message: Message, state: FSMContext) -> Message:
        """Отправка сообщения и очистка состояния"""
        await state.update_data(message_text=message.text)
        data = await state.get_data()
        data = data.get("message_text")
        if data == "Выход":
            await bot.send_message(chat_id=message.chat.id, text="Отправка отменена")
            return False
        user_service = UserService()
        users = await user_service.get_all_users()
        for user in users:
            await bot.send_message(chat_id=user.telegram, text=data)
        await state.clear()
        await bot.send_message(chat_id=message.chat.id, text="Успешно отправленно")


async def init_bot() -> Coroutine:
    """Инициализация сервиса бота"""
    await bot.set_my_commands([
        BotCommand(command="subscribe", description="подписаться на рассылку"),
        BotCommand(command="send", description="Рассылка сообщений")
    ])
    await bot.delete_webhook()
    await dispatcher.start_polling(bot)
