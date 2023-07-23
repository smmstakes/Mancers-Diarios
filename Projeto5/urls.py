from django.contrib import admin
from django.urls import path
from App_Projeto5.views import home, contact, pag_login, login_verif, pag_register, register_verif
from App_Projeto5.views import deslogar, pag_user1, visualizar_entradas, criar_entrada
from App_Projeto5.views import editar_entrada, excluir_entrada, pag_inicial, contact_user

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("login/", pag_login, name="pag_login"),
    path("login/verif/", login_verif, name="login_verif"),
    path("register/", pag_register, name="pag_register"),
    path("register/verif", register_verif, name="register_verif"),
    path("logout/", deslogar, name="logout"),
    path("home/", pag_user1, name="pag_user1"),
    path("diario/", visualizar_entradas, name="visualizar_entradas"),
    path("diario/criar/", criar_entrada, name="criar_entrada"),
    path("diario/editar/<int:entrada_id>/", editar_entrada, name="editar_entrada"),
    path("diario/excluir/<int:entrada_id>/", excluir_entrada, name="excluir_entrada"),
    path("pag_inicial/", pag_inicial, name="pag_inicial"),
    path("contact_user/", contact_user, name="contact_user"),
]
