from django.urls import path
from  myblog import views
app_name = 'myblog'
urlpatterns = [
    path('',views.index,name='index'),
    path('list/',views.list,name='list'),
    path('formset/',views.formset,name='formset'),
   
    path('addetud/', views.addetud, name='addetud'),

    path('addprod/',views.addprod,name='addprod'),
    path('prodlist/',views.prodlist,name='prodlist'),
    path('editprod/<int:pk>/',views.editprod,name='editprod'),
    path('delprod/<int:pk>/', views.delprod, name='delprod'),
    path('formsetadd/', views.formsetadd, name='formsetadd'),
    path('formsetadd1/', views.formsetadd1, name='formsetadd1'),
    
    path('pdf1/', views.render_pdf_view, name='render_pdf_view'),
    
    path('addfact/', views.addfact, name='addfact'),
    path('listfact/', views.listfact, name='listfact'),
    path('editfact/<int:pk>/', views.editfact, name='editfact'),
    path('delfact/<int:pk>/', views.delfact, name='delfact'),
    path('listetud/', views.listetud, name='listetud'),
    
]
