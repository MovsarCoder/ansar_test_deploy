from aiogram import Router

router = Router()

from .payment_handler import router as payment_router
router.include_router(payment_router)

from .start_handler import router as start_router
router.include_router(start_router)