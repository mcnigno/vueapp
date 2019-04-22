from flask import render_template, jsonify, g
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, has_access, expose
from app import appbuilder, db
from .models import Unit, Doctype, Category, Codecomposer, Project, Matrix, Codeitem, Code

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""

class VueMain(BaseView):
    #route_base = '/vuemain'
    default_view = 'vuemain' 

    @expose('/vuemain')
    @has_access
    def vuemain(self):
        return render_template('VueMain.html', base_template=appbuilder.base_template, appbuilder=appbuilder)
 

class VueUnitView(BaseView):
    default_view = 'units' 

    @expose('/units')
    @has_access
    def units(self):
        response = [
            {'text':'2pong','id':'002'},
            {'text':'Pong','id':'001'},
            {'text':'Song','id':'003'}
            ]
        res = db.session.query(Unit).filter(Unit.created_by_fk == g.user.id).all()
        res2 = [{'id':x.code,'text': x.text} for x in res]
        print(res2)
        print(g.user.id)
        
        return jsonify(res2)

class VueDoctypeView(BaseView):
    default_view = 'doctypes' 

    @expose('/doctypes')
    @has_access
    def doctypes(self):
        
        res = db.session.query(Doctype).filter(Doctype.created_by_fk == g.user.id).all()
        res2 = [{'id':x.code,'text': x.text} for x in res]
        print(res2)
        print(g.user.id)
        
        return jsonify(res2)

class UnitView(ModelView):
    datamodel = SQLAInterface(Unit)
    list_columns = ['text','code'] 

class DoctypeView(ModelView):
    datamodel = SQLAInterface(Doctype)
    
    
class CategoryView(ModelView):
    datamodel = SQLAInterface(Category)
    list_columns = ['id','code','rel_cat_id'] 
    add_columns = ['code','rel_cat_id'] 

class CodeComposerView(ModelView):
    datamodel = SQLAInterface(Codecomposer)
    list_columns = ['id','catname','position','is_key'] 
    add_columns = ['category','position','is_key'] 
    


class ProjectView(ModelView):
    datamodel = SQLAInterface(Project)
    #related_views = [CodecomposerView]
    list_columns = ['id','code','name','codecomposer'] 
    add_columns = ['code','name','codecomposer'] 

class MatrixView(ModelView):
    datamodel = SQLAInterface(Matrix)
    list_columns = ['id','code','project'] 
    add_columns = ['code','project'] 

class CodeItemView(ModelView):
    datamodel = SQLAInterface(Codeitem)
    list_columns = ['id','code', 'category_id', 'catname','composerpos'] 
    add_columns = ['code','project','category'] 
    base_order = ['category_id','asc']

class CodeView(ModelView):
    datamodel = SQLAInterface(Code)
    list_columns = ['id','code', 'project'] 
    add_columns = ['code','project'] 

appbuilder.add_view(VueMain,"Vue Main")
appbuilder.add_view(VueUnitView,"Vue Unit") 
appbuilder.add_view(UnitView,'Unit')
appbuilder.add_view(DoctypeView,'DocType')
appbuilder.add_view(VueDoctypeView,'Vue DocType')

appbuilder.add_view(CategoryView,'Category', category='Setting')
appbuilder.add_view(CodeComposerView,'Code Composer', category='Setting')
appbuilder.add_view(ProjectView,'Project', category='Setting')
appbuilder.add_view(MatrixView,'Matrix', category='Setting')
appbuilder.add_view(CodeItemView,'Code Item', category='Setting')
appbuilder.add_view(CodeView,'Code', category='Setting')


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
 

