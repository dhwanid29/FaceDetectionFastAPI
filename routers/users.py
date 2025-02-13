from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from database import get_db
# from users import services
# from users.schemas import UserCreate, ResponseUser

router = APIRouter(tags=["users"])
#
# @router.post("/add-user", response_model=ResponseUser, status_code=201)
# def create(user: UserCreate, db: Session = Depends(get_db)):
#     # return services.UserService.create_user(user, db)
#     user_service = services.UserService(db)
#     new_user = user_service.create_user(user)  # Create the new user using the service
#     return ResponseUser(
#         id=new_user.id,
#         username=new_user.username,
#         first_name=new_user.first_name,
#         last_name=new_user.last_name,
#         email=new_user.email,
#         gender=new_user.gender,
#         registration_date=new_user.registration_date
#     )
