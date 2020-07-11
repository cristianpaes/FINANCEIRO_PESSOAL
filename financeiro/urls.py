from django.contrib import admin
from django.urls import path
from fin import views
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/financeiro/')),
    path('financeiro/', views.grafico_financeiro),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_sistema),
    path('salario/', views.visual_salario),
    path('salario/cad_salario/', views.cadastrar_salario),
    path('despesas/', views.visual_despesas),
    path('despesas/cad_despesa/', views.cadastrar_despesa),
    path('despesas/cad_despesa/submit', views.submit_despesa),
    path('despesas/categoria/', views.visual_categoria),
    path('categoria/cad_categoria/', views.cadastrar_categoria),
    path('categoria/cad_categoria/submit', views.submit_categoria),
]
