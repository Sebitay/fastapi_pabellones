'''Global database models'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pabellon(Base):
    __tablename__ = "pabellon"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)

    def __repr__(self):
        return (
            f"Pabellon(id={self.id}, nombre={self.nombre}, especialidad={self.especialidad})"
        )
