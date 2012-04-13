# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.template import Context, Template

def home(request):
    file_name = request.GET['f']
    with open(file_name, 'r') as f:
        content = f.read()
    return render_to_response('editor_home.html', {
        'file': file_name,
        'content': content,
    }, context_instance=RequestContext(request))

def preview(request):
    file_name = request.GET['f']
    with open(file_name, 'r') as f:
        t = Template(f.read())
        r = t.render(RequestContext(request, { }))
    return HttpResponse(r)
    
def update(request):
    file_name = request.POST['f']
    content = request.POST['c']
    f = open(file_name, 'w')
    f.write(content)
    f.close()
    return HttpResponse('ok')

