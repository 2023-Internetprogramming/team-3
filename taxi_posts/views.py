from django.shortcuts import render, redirect
from .models import Ride
from .forms import RideForm
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def ride_list(request):
    rides = Ride.objects.order_by('-pk')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(rides, 10) 
    try:
        rides = paginator.page(page)
    except PageNotAnInteger:
        rides = paginator.page(1)
    except EmptyPage:
        rides = paginator.page(paginator.num_pages)

    return render(request, 'taxi_posts/ride_list.html', {'rides': rides, 'page_obj': rides})

def ride_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    return render(request, 'taxi_posts/ride_detail.html', {'ride': ride})


@login_required
def ride_create(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user
            new_item.save()
            return HttpResponseRedirect('/rides/')
        
    form = RideForm()
    return render(request, 'taxi_posts/ride_form.html', {'form': form})


@login_required
def ride_delete(request):
    ride_id = request.GET.get('id')
    
    if ride_id:
        item = get_object_or_404(Ride, pk=ride_id)
        
        if request.user != item.author:
            return HttpResponseForbidden("글을 삭제할 권한이 없습니다.")
        
        item.delete()
        
    return redirect('ride_list')


@login_required
def ride_update(request, id):
    item = get_object_or_404(Ride, pk=id)
    
    if request.user != item.author:
        return HttpResponseForbidden("글을 수정할 권한이 없습니다.")

    if request.method == 'POST':
        form = RideForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ride_detail', ride_id=item.id)

    else:
        form = RideForm(instance=item)

    return render(request, 'taxi_posts/ride_update.html', {'form': form})