from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from myblog.models import Unite,Grade,Produit,Facture,Operation,Etudient
from django.db.models import Count, Sum, Case, When
from django.forms import modelformset_factory,inlineformset_factory
from myblog.forms import ProduitForm,EtudeForm,OperationForm,FactureForm

from django.contrib.auth.decorators import login_required
#xhtml2pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
@login_required
def index(request):
    result = Unite.objects.values('lib_unt').filter(personne__annee=2020).annotate(s1=Sum(Case(When(personne__grade=1, then='personne__qte'), default=0)), s2=Sum(Case(When(personne__grade=2, then='personne__qte'), default=0)), s3=Sum(Case(When(personne__grade=3, then='personne__qte'), default=0)))
    test = Unite.objects.all()
    print(test)
    print(result)
    return render(request, 'myblog/index.html', {'results': result})
    
@login_required
def list(request):
    produits = Produit.objects.all()
    ProduitFormset = modelformset_factory(
        Produit, ProduitForm, can_delete=True, extra=0)
    formset = ProduitFormset(request.POST or None,
                             prefix="produits", queryset=produits)
    if request.method == 'POST':
        formset = ProduitFormset(
            request.POST, request.FILES, prefix="produits")
        #return HttpResponse(formset)
        if formset.is_valid():
            #return HttpResponse(formset)
            chaine = formset.data['recordelete'].split(',')
            for i in chaine:
                if formset.data['recordelete']:
                    get_object_or_404(Produit,id=i).delete()
                #if form.data['test']:
                #get_object_or_404(Mouvement,id=form.data['test']).delete()
                             
            for mvt in formset:
                mvt.save()
            return redirect('myblog:index')
    return render(request, "myblog/listprod.html", {"formset": formset})

@login_required
def formset(request):
    produits = Produit.objects.none()
    ProduitFormset = modelformset_factory(
        Produit, ProduitForm, can_delete=True)
    formset = ProduitFormset(request.POST or None,prefix="mouvemens", queryset=produits)
    if request.method == 'POST':
        #return HttpResponse(formset)
        if formset.is_valid():
            instances = formset.save()
            return redirect('myblog:list')
    return render(request, "myblog/formset.html", {"formset": formset})

@login_required
def addprod(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        #return HttpResponse(form.cleaned_data)
        form.save()
        return redirect('myblog:pordlist')
    return render(request,'myblog/addprod.html',{'form':form})


@login_required
def prodlist(request):
    produits = Produit.objects.all()
    return render(request,'myblog/prodlist.html',{'produits':produits})

@login_required
def editprod(request,pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('myblog:prodlist')
    return render(request,'myblog/editprod.html',{'form':form})

@login_required
def delprod(request,pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('myblog:prodlist')

@login_required
def formsetadd(request):
    Formsetproduit = modelformset_factory(
        Produit, ProduitForm, can_delete=True, extra=0)
    formset = Formsetproduit(request.POST or None, request.FILES or None, prefix="produits")
    if request.POST:
        pass
    if formset.is_valid():
        #return HttpResponse(formset)
        instances = formset.save()
        return redirect('myblog:prodlist')
    return render(request,'myblog/formsetadd.html',{'formset':formset})

@login_required
def formsetadd1(request):
    Formsetproduit = modelformset_factory(
    Produit, ProduitForm, can_delete=True, extra=0)
    formset = Formsetproduit(request.POST or None, request.FILES or None, prefix="produits")
    if request.POST:
        pass
    if formset.is_valid():
        instances = formset.save()
        return redirect('myblog:prodlist')
    return render(request,'myblog/formsetadd1.html',{'formset':formset})

@login_required
def render_pdf_view(request):
    template_path = 'myblog/pdf1.html'
    produits= Produit.objects.all()
    context = {'produits': produits}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def addetud(request):
    form = EtudeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        #return HttpResponse(form.cleaned_data)
        form.save()
        return redirect('myblog:prodlist')
    return render(request, 'myblog/addetud.html', {'form': form})

@login_required
def listetud(request):
    etudients=Etudient.objects.all()
    return render(request, 'myblog/listetud.html', {'etudients': etudients})

@login_required
def addfact(request):
    form = FactureForm(request.POST or None)
    #OperationFormSet = modelformset_factory(Operation, OperationForm, extra=1)
    OperationFormSet = inlineformset_factory(Facture,Operation, OperationForm, extra=1)
    formset = OperationFormSet(
        request.POST or None,  queryset=Operation.objects.none(), prefix='oper')
    """     formset = OperationFormSet(
            request.POST or None, request.FILES or None, queryset=Operation.objects.none(), prefix='oper')
    """    
    if request.method=='POST':
        pass
    if form.is_valid and formset.is_valid():
        fs=form.save(commit=False)
        fs.save()
        instances=formset.save(commit=False)
        for instance in instances:
            instance.facture = fs
            instance.save()

        return redirect('myblog:listfact')
    context={'form':form,'formset':formset}
    return render(request,'myblog/addfact.html',context)

@login_required
def editfact(request,pk):
    fact=get_object_or_404(Facture,pk=pk)
    form=FactureForm(request.POST or None,instance=fact)
    OperationFormsSet=inlineformset_factory(Facture,Operation,OperationForm,extra=1,can_delete=True)
    formset = OperationFormsSet(
        request.POST or None,  instance=fact, prefix='oper')
    if form.is_valid() and formset.is_valid():
        #fs= form.save(commit=False)
        #fs.save()
        form.save()
        instances = formset.save()
        return redirect('myblog:listfact')

    context={'form':form,'formset':formset}
    return render(request,'myblog/editfact.html',context)
 
@login_required
def listfact(request):
    factures=Facture.objects.all()
    return render(request,'myblog/listfact.html',{'factures':factures})

@login_required
def delfact(request,pk):
    facture = get_object_or_404(Facture, pk=pk)
    facture.delete()
    return redirect('myblog:listfact')


