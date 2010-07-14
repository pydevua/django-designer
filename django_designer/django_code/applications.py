CONTRIB_APPS = {
    'admin': {'models': ['LogEntry']},
    'admindocs': {},
    'auth': {'models': ['Permission', 'Group', 'User', 'Message'],
             'middleware': ['AuthenticationMiddleware', 'RemoteUserMiddleware']},
    'comments': {'models': ['BaseCommentAbstractModel', 'Comment', 'CommentFlag']},
    'contenttypes': {'models': ['ContentType']},
    'csrf': {},
    'databrowse': {},
    'flatpages': {'models': ['FlatPage'],
                  'middleware': ['FlatpageFallbackMiddleware']},
    'formtools': {},
    'gis': {},
    'humanize': {},
    'localflavor': {},
    'markup': {},
    'messages': {'middleware': ['MessageMiddleware']},
    'redirects': {'models': ['Redirect'],
                  'middleware': ['RedirectFallbackMiddleware']},
    'sessions': {'models': ['Session'],
                 'middleware': ['SessionMiddleware']},
    'sitemaps': {},
    'sites': {'models': ['Site']},
    'syndication': {},
    'webdesign': {},
}

DJANGO_INITIAL_APPS = ['admin', 'auth', 'contenttypes', 'sessions', 'sites', 'messages']


def add_django_app(project, name):
    app = project.applications.create(name=name,
                        package='django.contrib', is_external=True, is_django=True)
    for model in CONTRIB_APPS[name].get('models', []):
        app.model_set.create(name=model, is_external=True)
    return app

def init_django_project(project):
    "Initializes project with default contrib django applications"
    for app in DJANGO_INITIAL_APPS:
        add_django_app(project, app)
