from Index.models import *
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import *
from django.core.urlresolvers import reverse


#-------------------------------------------------------------------------


class MainView(View):
	def get(self,request):
		return render(request, 'Index.html',{
			'articol':Article.objects.active(),
			'titlu':TitlulZilei.objects.all(),
			'titlutab':TitlulZileiTab.objects.all(),
			'imaginebara':Picture.objects.all(),
			'categorie':Category.objects.all(),
			}
			)
#-------------------------------------------------------------------------

class CategoryView(View):
	def get(self, request, category_slug) :
		category = get_object_or_404(Category, slug=category_slug)

		return render(request,'categories.html',{
			'category':category,
			'titlu':TitlulZilei.objects.all(),
			'titlutab':TitlulZileiTab.objects.all(),
			'imaginebara':Picture.objects.all(),
			'categorie':Category.objects.all(),
			#'cat':Category.objects.all()
			#'posts':Article.objects.filter(categorie = category)
			})
#-------------------------------------------------------------------------

class PostView(View):
	def get(self,request,slug):
		post = get_object_or_404(Article,slug=slug)
		return render(request,'post.html',{
			'post':post,
			'titlu':TitlulZilei.objects.all(),
			'titlutab':TitlulZileiTab.objects.all(),
			'imaginebara':Picture.objects.all(),
			}
			)











#def main(request):
#	articol= Article.objects.all()
#	paginator = Paginator(articol,5)
#	
#	try: page = int(request.GET.get("page", '1'))
#	except ValueError: page = 1
#	
#	try:
#		articol = paginator.page(page)
#	except (InvalidPage, EmptyPage):
#		articol = paginator.page(paginator.num_pages)
#	
#	return render(request,'Index.html',{
#		'articol':Article.objects.active(),
#		'titlu':TitlulZilei.objects.all(),
#		'titlutab':TitlulZileiTab.objects.all(),
#		'imaginebara':Picture.objects.all()
#		}
#		)

