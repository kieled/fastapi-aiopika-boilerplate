from fastapi import APIRouter
from .test import test_router

router = APIRouter()

router.include_router(test_router)
