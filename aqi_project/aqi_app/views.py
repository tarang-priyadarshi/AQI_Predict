from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == "POST":
        city = request.POST['city']
        api_request = requests.get(f"https://api.waqi.info/feed/{city}/?token=cfea963f782b0517441e1679d740ea5078ac72e2")
        
        try:
            api = json.loads(api_request.content.decode('utf-8'))
            if api['data']['aqi'] < 51:
                quality = "Good"
                col = "good"
                aqi_range = "0 - 50"
            elif api['data']['aqi'] < 101:
                quality = "Moderate"
                col = "moderate"
                aqi_range = "51 - 100"
            elif api['data']['aqi'] < 151:
                quality = "Unhealthy for Sensitive Groups"
                col = "usg"
                aqi_range = "101 - 150"
            elif api['data']['aqi'] < 201:
                quality = "Unhealthy"
                col = "unhealthy"
                aqi_range = "151 - 200"
            elif api['data']['aqi'] < 301:
                quality = "Very Unhealthy"
                col = "veryunhealthy"
                aqi_range = "201 - 300"
            else:
                quality = "Hazardous"
                col = "hazardous"
                aqi_range = "300+"

            return render(request, 'home.html', {
                'api': api,
                'quality': quality,
                'col': col,
                'aqi_range': aqi_range,
            })
        except Exception as e:
            api = "Error"
            return render(request, 'home.html', {
                'api': api,
            })
    
    else:
        api_request = requests.get("https://api.waqi.info/feed/delhi/?token=cfea963f782b0517441e1679d740ea5078ac72e2")
        
        try:
            api = json.loads(api_request.content.decode('utf-8'))
            if api['data']['aqi'] < 51:
                quality = "Good"
                col = "good"
                aqi_range = "0 - 50"               
            elif api['data']['aqi'] < 101:
                quality = "Moderate"
                col = "moderate"
                aqi_range = "51 - 100"                
            elif api['data']['aqi'] < 151:
                quality = "Unhealthy for Sensitive Groups"
                col = "usg"
                aqi_range = "101 - 150"                
            elif api['data']['aqi'] < 201:
                quality = "Unhealthy"
                col = "unhealthy"
                aqi_range = "151 - 200"
            elif api['data']['aqi'] < 301:
                quality = "Very Unhealthy"
                col = "veryunhealthy"
                aqi_range = "201 - 300"
            else:
                quality = "Hazardous"
                col = "hazardous"
                aqi_range = "300+"

            return render(request, 'home.html', {
                'api': api,
                'quality': quality,
                'col': col,
                'aqi_range': aqi_range,
                
            })
        except Exception as e:
            api = "Error"
            return render(request, 'home.html', {
                'api': api,
            })

def about(request):
    return render(request, 'about_me.html', {})


# Create your views here.
