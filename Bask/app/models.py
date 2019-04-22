from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey , Boolean
from sqlalchemy.orm import relationship
from app import db
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
class Unit(Model,AuditMixin):
    id = Column(Integer, primary_key=True)
    text = Column(String(50), nullable=False)
    code = Column(String(10),nullable=False)

class Doctype(Model,AuditMixin):
    id = Column(Integer, primary_key=True)
    text = Column(String(50), nullable=False)
    code = Column(String(10),nullable=False)

'''

BASK CODE RELEASE

'''

class Category(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    code = Column(String(30), nullable=False)
    rel_cat_id = Column(Integer, ForeignKey('category.id'))

    def __repr__(self):
        return self.code

class Codecomposer(Model, AuditMixin):
    id = Column(Integer, primary_key=True)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    position = Column(Integer, default=0, nullable=False)
    is_key = Column(Boolean)

    def __repr__(self):
        return str(self.id)
    
    def catname(self):
        return str(self.category.code)

    #codecomposer_id = Column(Integer, ForeignKey('project.id'))


class Project(Model,AuditMixin):
    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True, nullable=False)
    name = Column(String(50), unique=True, nullable=False)

    codecomposer_id = Column(Integer, ForeignKey('codecomposer.id'))
    codecomposer = relationship(Codecomposer)
    
    def __repr__(self):
        return self.code


class Matrix(Model,AuditMixin):
    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True, nullable=False)

    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)

    def __repr__(self):
        return self.code


class Codeitem(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True, nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)

    def __repr__(self):
        return self.code

    def catname(self):
        return str(self.category.code)

    def composerpos(self):
        session = db.session
        comp = session.query(Codecomposer).filter(Codecomposer.category_id == self.category_id).first()
        return comp.position


class Code(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True, nullable=False)


    matrix_id = Column(Integer, ForeignKey('matrix.id'))
    matrix = relationship(Matrix)

    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)

    def __repr__(self):
        return self.code
  