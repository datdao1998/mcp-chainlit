from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class UserInfoRequest(BaseModel):
    """Request model for user information

    :param email: Email address of user
    :type email: str
    :param phone:  Phone number of user
    :type phone: str
    """
    email: Optional[str] = Field("", description="Email address")
    phone: Optional[str] = Field("", description="Phone number")


class UserInfoResponse(BaseModel):
    """
    Response model for User Information Retrieve API
    """
    user_info: Optional[str] = Field("", description="User information")
    lucky_number: Optional[int] = Field(1, description="Lucky number of user")


class UserInfoError(BaseModel):
    """
    Response model for errors occuring when get user information
    """
    error: Optional[str] = Field("", description="Error message")
