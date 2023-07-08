from fastapi import APIRouter


router = APIRouter(
    prefix='/users',
    tags=['User and auth']
)


@router.post('/signup')
def create_user():
    pass