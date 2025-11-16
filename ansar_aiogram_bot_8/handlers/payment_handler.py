from aiogram import Router, types, filters

from ..config.settings import PAYMENT_TOKEN
from ..utils.constants import PRICES

router = Router()


@router.message(filters.Command("buy"))
async def buy_handler(message: types.Message):
    await message.bot.send_invoice(
        chat_id=message.from_user.id,
        title='Премиум подписка',
        description='Доступ к эксклюзивному контенту',
        payload='premium-access',
        provider_token=PAYMENT_TOKEN,
        currency="RUB",
        prices=PRICES,
        photo_url="https://www.spot.uz/media/img/2022/06/UanMas16557049693541_l.jpg"
    )


@router.pre_checkout_query()
async def pre_checkout_query_handler(query: types.PreCheckoutQuery):
    await query.answer(ok=True)


@router.message(lambda message: message.successful_payment is not None)
async def successful_payment_handler(message: types.Message):
    await message.answer("Оплата успешно завершена!")
