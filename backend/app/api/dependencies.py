from app.db.session import SessionLocal

# Dependency injection function for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
