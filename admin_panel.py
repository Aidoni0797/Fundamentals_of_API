# Код не рабочий
from aiogram.types import TelegramObject
from aiogram.filters import BaseFilter


admin_ids = [5630011467]


class IsAdmin(BaseFilter):
    async def __call__(self, obj: TelegramObject) -> bool:
        return obj.from_user.id in admin_ids


@dp.message(Command('admin'), IsAdmin())
async def admin_command(message: types.Message) -> None:
    await message.answer('Добро пожаловать в Админ-панель!')