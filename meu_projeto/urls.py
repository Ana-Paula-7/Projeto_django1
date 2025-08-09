from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='/tarefas/')),
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),

]
