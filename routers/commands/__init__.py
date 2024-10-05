__all__ = ("router",)

from aiogram import Router

from .base_command import router as base_commands_router
from .func_pay import router as pay_router

router = Router(name=__name__)

router.include_routers(
    base_commands_router,
    pay_router,
)