from app import model
from app.database import Base,engine

Base.metadata.create_all(bind=engine)

print("notes database tables created successfully ")