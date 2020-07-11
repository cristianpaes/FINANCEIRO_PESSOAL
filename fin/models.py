from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
     nome_cat = models.CharField(max_length=150, unique=True, verbose_name='Categoria')

     class Meta:
        db_table = 'categoria'

     def __str__(self):
        return self.nome_cat

class Salario(models.Model):
    valor_sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Salario Liquido')
    valor_extra = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='Valor do Extra')
    data_sal = models.DateField(verbose_name='Data do Salário')
    data_extra = models.DateField(verbose_name='Data do Extra')
    data_reg_sal = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'salario'

    def __float__(self):
        return self.valor_sal

class Despesa(models.Model):
    nome_desp = models.CharField(max_length=150,verbose_name='Descrição da Despesa')
    valor_dep = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='Valor Despesa')
    cat_dep = models.ForeignKey(Categoria,on_delete= models.DO_NOTHING,verbose_name='Categoria')
    data_dep = models.DateField()
    data_reg_dep = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'despesa'

    def __str__(self):
        return self.nome_desp