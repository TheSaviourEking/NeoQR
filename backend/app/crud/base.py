from typing import Generic, TypeVar, Type, Any, Dict, List, Optional, Union
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Base)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=Base)

from fastapi import HTTPException

# from sqlalchemy.orm import Session
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

    async def get(
        self, db: AsyncSession, field: str, value: Any
    ) -> Optional[ModelType]:
        query = select(self.model).where(getattr(self.model, field) == value)
        result = await db.execute(query)
        # return result.scalars().first()
        return result.fetchone()

    async def get_multi(
        self, db: AsyncSession, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        query = select(self.model).offset(skip).limit(limit)
        result = await db.execute(query)
        return result.all()
        # return await db.query(self.model).offset(skip).limit(limit).all()

    async def create(self, db: AsyncSession, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        db.add(db_obj)

        try:
            await db.commit()
            await db.refresh(db_obj)
        except IntegrityError as e:
            await db.rollback()
            # Handle the IntegrityError
            raise HTTPException(status_code=400, detail=str(e.orig))
        except IntegrityError as e:
            await db.rollback()
            raise HTTPException(
                status_code=400, detail="Integrity Error: " + str(e.orig)
            )
        except DataError as e:
            await db.rollback()
            raise HTTPException(status_code=400, detail="Data Error: " + str(e.orig))
        except OperationalError as e:
            await db.rollback()
            raise HTTPException(
                status_code=500, detail="Operational Error: " + str(e.orig)
            )

        return db_obj

    async def update(
        self,
        db: AsyncSession,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        await db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


async def remove(self, db: AsyncSession, id: int) -> ModelType:
    obj = await db.query(self.model).get(id)
    await db.delete(obj)
    await db.commit()
    return obj
