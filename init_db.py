from database import Base, engine
import models  # Ensures models are imported

def initialize_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_db()
