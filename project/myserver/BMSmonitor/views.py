from django.shortcuts import render
from django.http import HttpResponse
from BMSmonitor.models import *
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


def index(request):
    return HttpResponse("HelloWorld")


def update_cell_data(request):
    
    if request.method == 'POST':
        # POST 요청에서 데이터 가져오기
        c0_voltage = float(request.POST.get('cell0_voltage'))  # 배터리 모듈 ID
        c1_voltage= float(request.POST.get('cell1_voltage'))
        c2_voltage= float(request.POST.get('cell1_voltage'))
        c3_voltage= float(request.POST.get('cell1_voltage'))
        temp = float(request.POST.get('temperature'))
        chargeFlag = float(request.POST.get('chargeFlag'))
        
        
        c0_soc = c0_voltage -5
        c1_soc = c1_voltage -5
        c2_soc = c2_voltage -5
        c3_soc = c3_voltage -5
        
      
        
        
        
        module, created = Module.objects.update_or_create(
             # 모듈 식별을 위한 필드
          
            defaults={
               
                'cell0_voltage': c0_voltage,
                'cell0_soc':c0_soc,
                'cell1_voltage': c1_voltage,
                'cell1_soc':c1_soc,
                'cell2_voltage': c2_voltage,
                'cell2_soc':c2_soc,
                'cell3_voltage': c3_voltage,
                'cell3_soc':c3_soc,
                'charge_flag' : chargeFlag,
                'temperature':temp,
               
            }
        )
        
        print(c0_voltage)
        print(c1_voltage)
        print(c2_voltage)
        print(c3_voltage)
        print(temp)
        print(chargeFlag)     
        

        if created:
            return HttpResponse("Cell data created successfully", status=200)
        else:
            return HttpResponse("Cell is not created", status=200)
    else:
        return HttpResponse("Invalid request method", status=400)


def show_cell_data(request):
    # 최근에 업데이트된 Cell 데이터 가져오기
    latest_cell_data = Module.objects.last()
  
    return render(request, 'BatteryData.html', {'cell_data': latest_cell_data}) 
     
def real_time_update(request):
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {"temperature": Module.objects.id('1').temperature}
        return JsonResponse(data)
    else:
        return JsonResponse({'ERROR':'Invalid Request'}, status=400)
 