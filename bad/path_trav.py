from django.http import HttpResponse
import os

def foo_2(request):
  param = request.GET.get('param')
  file_path = os.path.join("MY_SECRET", param)
  file_path = os.path.abspath(file_path)
  # ok: taint-backend-path-traversal-open
  f = open(file_path, 'r')
  return HttpResponse(content=f, content_type="text/plain")
