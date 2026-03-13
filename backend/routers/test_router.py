from ..controllers.hello_controller import hello
from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def hello_route():
    return hello()
