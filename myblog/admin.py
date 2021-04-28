from django.contrib import admin
from myblog.models import Personne,Unite,Grade,Produit,Etudient
# Register your models here.
admin.site.register(Unite)
admin.site.register(Grade)
admin.site.register(Personne)
admin.site.register(Produit)
admin.site.register(Etudient)
admin.site.site_header='az Clinique'
admin.site.site_title='Myblog'