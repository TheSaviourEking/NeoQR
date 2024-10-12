from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: int
    __name_: str

    # Automatically generate table names if not explicitly defined
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name_.lower()


# from app.models.user import User
# from app.models.item import Item
