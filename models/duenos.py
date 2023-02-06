import basedatos.bd as bd
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Duenos(db.base):
    
    __tablename__= 'duenos'

    due_codigo = Column('due_codigo', Integer, primary_key=True, autoincrement=True)
    due_nombre = Column('due_nombre', String(100), nullable=False)
    due_tipo_usuario = Column('due_tipo_usuario', String(1), nullable=False)
    due_documento = Column('due_documento', String(15), nullable=False)
    
    def __init__(self, documento, nombre_completo, tipo_usuario):
        self.due_documento = documento
        self.due_nombre = nombre_completo
        self.due_tipo_usuario = tipo_usuario
    
    def __repr__(self):
        return f"<Duenos {self.documento}>"