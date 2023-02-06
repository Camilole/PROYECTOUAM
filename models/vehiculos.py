import controlservice.bd as bd
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Vehiculo(db.Base):
    __tablename__ = 'vehiculos'
    veh_codigo = Column('veh_codigo', Integer, primary_key=True, autoincrement=True),
    veh_placa = Column('veh_placa', String(10), nullable=False)
    veh_tipo = Column('veh_tipo', String(10), nullable=False)
    
  