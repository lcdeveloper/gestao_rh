from django.urls import path
from .views import FuncionarioList, FuncionarioEdit

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='edit_funcionario')


]