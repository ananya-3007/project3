from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("""<h1> Welcome to my Blog </h1>
                        <p> Hope you are doing well.</p>
                        <ol>
                        <li> Apple</li>
                        <li> Mango</li>
                        <li> Chikku</li>
                        <li> Banana </li>
                        </ol>"""
                        )
# Create your views here.
def about(request):
    return HttpResponse('<h1>About</h1>')