from django.shortcuts import render
from django.http import HttpResponseRedirect
from search_by_zip.models import Center
from search_by_zip.forms import ZipForm

# Page where the user can enter a zip code
def index(request):
	if request.method =='GET':
		form = ZipForm()
	else:
		form = ZipForm(request.POST)
		if form.is_valid():
			zipcode = form.cleaned_data['zipentered']
		return HttpResponseRedirect('/search_by_zip/results/'+str(zipcode))
	return render(request, "index.html", {'form':form})

# Page where results will be displayed
def results(request, zipentered):
	results_by_zip = Center.objects.filter(five_digit_zip=zipentered)
	return render(request, "results.html", {'providers':results_by_zip})