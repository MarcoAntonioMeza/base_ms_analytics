from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms.grupos import GroupForm

# Create your views here.
def index (request):
    return render(request, 'adminv2/grupos/index.html')

def create (request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupos_view', id=id)  # Redirige al listado de grupos
    else:
        form = GroupForm()
    return render(request, 'adminv2/grupos/create.html',{ 'form': form })

def view (request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, 'adminv2/grupos/view.html', {'group': group})


def update (request, id):
    group = get_object_or_404(Group, pk=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('grupos_view', id=id)
    else:
        form = GroupForm(instance=group)
    return render(request, 'adminv2/grupos/update.html', {'form': form, 'group': group})



def delete (request, id):
    group = get_object_or_404(Group, pk=id)
    group.delete()
    return redirect('group_list')









def index_list_ajax(request):
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')

    # Filtrado por búsqueda
    grupos = Group.objects.all()
    if search_value:
       grupos = grupos.filter(
        Q(name__icontains=search_value) |
        #Q(apellido_paterno__icontains=search_value) |
        #Q(email__icontains=search_value)|
        Q(id__icontains=search_value)
        #Q(username__icontains=search_value)
    )
    # Paginación
    paginator = Paginator(grupos, length)
    page_number = (start // length) + 1
    page_obj = paginator.get_page(page_number)

    # Serializar datos
    data = [
        {
            "id": s.id,
            "name": f"{s.name}".upper(),
            #"phone": str(s.telefono),
            #"phone2": str(s.telefono2),
            #'tipo': s.get_tipo_display(),
            #'estado': s.get_status_display(),
            #
            #"email": str(s.email),
            ##"created_at": s.created_at,
            #"created_at": format(s.created_at, 'd-m-Y h:i:s'),
            ##"created_by": str(s.created_by.username) if s.created_by else "",
        }
        for s in page_obj
    ]

    return JsonResponse({
        "draw": draw,
        "recordsTotal": paginator.count,
        "recordsFiltered": paginator.count,
        "data": data
    })
