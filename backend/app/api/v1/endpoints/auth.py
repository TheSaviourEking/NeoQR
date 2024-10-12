from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def login():
    return "here"


@router.get("/signup")
def signup():
    """heoooo"""
    return "here"
