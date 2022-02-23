from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests

from security.jwt_token import create_access_token
from security.secrets import Secret
import facebook
from models import end_user_model
from constants import Utils
from schemas import end_user_schema


def googleLogin(access_token: str, db: Session, response: Response):
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(access_token, requests.Request(), Secret.ClIENT_ID)

        userid = idinfo['sub']
        email = idinfo['email']
        name = idinfo['name']
        picture = idinfo['picture']

        end_user = db.query(end_user_model.EndUser).filter(end_user_model.EndUser.auth_user_id == userid).first()

        if not end_user:
            new_end_user = end_user_model.EndUser(
                id=Utils.gen_pk_perm(),
                auth_user_id=userid,
                user_name=name,
                email=email,
                profile_pic=picture,
                auth_provider="google"
            )

            db.add(new_end_user)
            db.commit()
            db.refresh(new_end_user)

            token_payload = {
                "id": new_end_user.id,
                "auth_user_id": new_end_user.auth_user_id,
            }
            access_token = create_access_token(
                token_payload
            )
            response.status_code = status.HTTP_201_CREATED
            return {
                'detail': "User Created Successfully",
                'access_token': access_token,
                'token_type': "bearer",
                'user_id': new_end_user.id,
                'user': end_user_schema.ShowEndUser.parse_obj(vars(new_end_user ))
            }

        else:
            token_payload = {
                "id": end_user.id,
                "auth_user_id": end_user.auth_user_id,
            }
            access_token = create_access_token(
                token_payload
            )
            response.status_code = status.HTTP_200_OK

            return {
                'detail': "Login Successful",
                'access_token"': access_token,
                'token_type': "bearer",
                'user_id': end_user.id,
                'user': end_user_schema.ShowEndUser.parse_obj(vars(end_user))
            }

    except ValueError:
        # Invalid token
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Not Authorized")


def facebookLogin(access_token, db: Session, response: Response):
    try:
        graph = facebook.GraphAPI(access_token)
        args = {'fields': 'id,name,email,picture.type(large)', }
        profile = graph.get_object('me', **args)
        userid = profile.get('id')
        name = profile.get('name')
        email = profile.get('email')
        picture = profile.get('picture')['data']['url']

        end_user = db.query(end_user_model.EndUser).filter(end_user_model.EndUser.auth_user_id == userid).first()

        if not end_user:
            new_end_user = end_user_model.EndUser(
                id=Utils.gen_pk_perm(),
                auth_user_id=userid,
                user_name=name,
                email=email,
                profile_pic=picture,
                auth_provider="facebook"
            )
            db.add(new_end_user)
            db.commit()
            db.refresh(new_end_user)

            token_payload = {
                "id": new_end_user.id,
                "auth_user_id": new_end_user.auth_user_id,
            }
            access_token = create_access_token(
                token_payload
            )
            response.status_code = status.HTTP_201_CREATED
            return {
                'detail': "User Created Successfully",
                'access_token': access_token,
                'token_type': "bearer",
                'user_id': new_end_user.id,
                'user': end_user_schema.ShowEndUser.parse_obj(vars(new_end_user))
            }

        else:
            token_payload = {
                "id": end_user.id,
                "auth_user_id": end_user.auth_user_id,
            }
            access_token = create_access_token(
                token_payload
            )
            response.status_code = status.HTTP_200_OK

            return {
                'detail': "Login Successful",
                'access_token"': access_token,
                'token_type': "bearer",
                'user_id': end_user.id,
                'user': end_user_schema.ShowEndUser.parse_obj(vars(end_user))
            }
    except ValueError as ve:
        # Invalid token
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=str(ve))
