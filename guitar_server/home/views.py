from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.



def index(request):
    context = {}
    # featuredProducts = FeaturedProduct.get_actives()
    # context['featuredProducts'] = featuredProducts
    template = loader.get_template('index.html')
    import pdb
    # pdb.set_trace()
    return HttpResponse(template.render(context, request))