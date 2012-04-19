# Create your views here.
import json
import os.path

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.template import Context, Template

def editor(request):
    file_name = request.GET['f']
    with open(file_name, 'r') as f:
        content = f.read()
    return render_to_response('editor.html', {
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
    content = request.POST['c'].encode('utf8')
    f = open(file_name, 'w')
    f.write(content)
    f.close()
    return HttpResponse('ok')

def explorer(request):
    return render_to_response('explorer.html', {
        'eye': request.GET.get('eye', ''),
    }, context_instance=RequestContext(request))

def explorer_api(request):
    file_name = request.GET.get('f', '.')
    files = []
    for f in os.listdir(file_name):
        if os.path.isdir(os.path.join(file_name, f)):
            file_type = 'directory'
        else:
            file_type = 'file'
        files.append({ 'type': file_type, 'file': f })
    files.sort(key=lambda x:(x['type'], x['file']))
    return HttpResponse(json.dumps(files), content_type='application/json')

