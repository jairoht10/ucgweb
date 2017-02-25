from django.shortcuts import render

def post_list(request):
    return render(request, 'articulo/post_list.html',{})
