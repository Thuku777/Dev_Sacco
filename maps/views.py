from django.shortcuts import render

# Create your views here.
def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoidGh1a3U3NzciLCJhIjoiY2tlanB2NGsyMDJ2ODMxbnN4eHdmdzRrMCJ9.0JMwbEkwb8rupJzSUx4ZBw'
    context = {
        'mapbox_access_token': mapbox_access_token
    }
    return render(request, 'map.html', context)