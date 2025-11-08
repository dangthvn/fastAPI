from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils
from . import oauth2

router = APIRouter(
    tags=["Authentication"]
)
@router.post("/login", response_model=schemas.Token)
def login(user_credential: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.email).first()
    if not user or not utils.verify_password(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    # Create a token (e.g., JWT) here for the authenticated user
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}