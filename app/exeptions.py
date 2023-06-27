from fastapi import HTTPException, status

OkExeption = HTTPException(
    status_code=status.HTTP_200_OK,
    detail='Ok'
)

NotFoundItemExeption = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Item not found'
)