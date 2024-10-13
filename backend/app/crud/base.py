from typing import Generic, TypeVar, Type, Any

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")

from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError, DataError, OperationalError


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**
        * `model`: A SQLAlchemy model class
        """

        self.model = model

    # def get(self, db: Session, id: Any) -> ModelType:
    #     return db.query(self.model).filter(self.model.id == id).first()

    def get(self, db: Session, field: str, value: Any) -> ModelType:
        return db.query(self.model).filter(getattr(self.model, field) == value).first()

    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        db.add(db_obj)

        try:
            db.commit()
            db.refresh(db_obj)
        except IntegrityError as e:
            db.rollback()
            # Handle the IntegrityError
            raise HTTPException(status_code=400, detail=str(e.orig))
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                status_code=400, detail="Integrity Error: " + str(e.orig)
            )
        except DataError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Data Error: " + str(e.orig))
        except OperationalError as e:
            db.rollback()
            raise HTTPException(
                status_code=500, detail="Operational Error: " + str(e.orig)
            )

        return db_obj

    def update(
        self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType | dict[str, Any]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


def remove(self, db: Session, id: int) -> ModelType:
    obj = db.query(self.model).get(id)
    db.delete(obj)
    db.commit()
    return obj
