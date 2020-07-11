from django.contrib import admin
from fin.models import Categoria, Despesa, Salario

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ['id','nome_desp','valor_dep', 'cat_dep', 'data_dep','data_reg_dep']
    list_per_page = 5

@admin.register(Salario)
class SalarioAdmin(admin.ModelAdmin):
    list_display = ['valor_sal', 'valor_extra', 'data_sal', 'data_extra']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_cat']