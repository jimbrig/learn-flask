from flask import render_template
from flask_appbuilder import BaseView, expose, has_access

from . import appbuilder, db

from . import appbuilder, db

class DemoView(BaseView):
    default_view = "method1"

    @expose('/method1/')
    @has_access
    def method1(self):
        message = 'message #1: Method1'
        return render_template('method1.html', message=message)

    @expose('/method2/<message>')
    @has_access
    def method2(self, message):
        message = 'message #2: %s' % (message)
        return render_template('method1.html', message=message)

    @expose('/method3/')
    @has_access
    def method3(self):
        message = 'message #3: Method3'
        return render_template('method3.html', message=message, 
                               base_template=appbuilder.base_template, appbuilder=appbuilder)

appbuilder.add_view(DemoView(), "Message1",
                    category='Demo View', category_icon='fa-envelope',
                    href="/demoview/method1/")

appbuilder.add_link("Message2", category='Demo View',
                    href="/demoview/method2/FAB_Demo_view")

appbuilder.add_link("Message3", category='Demo View',
                    href="/demoview/method3/")

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
    
db.create_all()
