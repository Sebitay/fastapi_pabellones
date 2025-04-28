'''global database models'''

from sqlmodel import Field, SQLModel, Session


class Pabellon(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    especialidad: str

    def __repr__(self):
        return f'Pabellon(id={self.id}, nombre={self.nombre}, capacidad={self.capacidad}, ubicacion={self.ubicacion}, descripcion={self.descripcion})'