from django.shortcuts import render_to_response

def home(request):
  render_to_response(request, 'base.html')
