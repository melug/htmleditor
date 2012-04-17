from django.conf.urls.defaults import *

urlpatterns = patterns("htmleditor.views",
    url(r"^editor/e/$", "explorer", name="editor-explorer"),
    url(r"^editor/e/api/$", "explorer_api", name="editor-explorer-api"),
    url(r"^editor/i/$", "editor", name="editor-editor"),
    url(r"^editor/preview/$", "preview", name="editor-preview"),
    url(r"^editor/update/$", "update", name="editor-update"),
)
