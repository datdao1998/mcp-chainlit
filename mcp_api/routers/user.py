from fastapi import APIRouter, Depends, HTTPException

from mcp_api.schemas.user import UserInfoRequest, UserInfoResponse, UserInfoError
import mcp_api.controller.user as ctl


user_router = APIRouter(tags=["user"])

@user_router.post("/get-user-info", operation_id="get_user_info")
async def get_user_info(request: UserInfoRequest):
    """
    Return user information from their phone number and email address
    """
    phone = request.phone
    email = request.email

    response = ctl.get_user_info(email=email, phone=phone)

    if response["statusCode"] == 200:
        return UserInfoResponse(
            user_info=response["userInfo"],
            lucky_number=response["luckyNumber"]
        )
    
    return UserInfoError(error="Cannot extract user information")

