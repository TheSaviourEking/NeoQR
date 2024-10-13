from pydantic import BaseModel

class ProfileBase(BaseModel):
    pass

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    pass
