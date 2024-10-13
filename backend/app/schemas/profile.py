from pydantic import BaseModel
from typing import Optional


class ProfileBase(BaseModel):
    bio: Optional[str] = None
    profile_image: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    pass
