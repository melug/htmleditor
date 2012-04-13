from django.conf.urls.defaults import *

urlpatterns = patterns("htmleditor.views",
    url(r"^editor/$", "home", name="editor-home"),
    url(r"^editor/preview$", "preview", name="editor-preview"),
    url(r"^editor/update$", "update", name="editor-update"),
)
