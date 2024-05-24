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
        module_id = request.POST.get('module_id')  # 배터리 모듈 ID
        M0_C0_voltage= request.POST.get('M0_C0_V')
        M0_C0_SOC = request.POST.get('M0_C0_SOC')
        M0_C1_voltage= request.POST.get('M0_C1_V')
        M0_C1_SOC = request.POST.get('M0_C1_SOC')
        M0_C2_voltage= request.POST.get('M0_C2_V')
        M0_C2_SOC = request.POST.get('M0_C2_SOC')
        M0_C3_voltage= request.POST.get('M0_C3_V')
        M0_C3_SOC = request.POST.get('M0_C3_SOC')
        
        module, created = Module.objects.update_or_create(
            moduleId=module_id,  # 모듈 식별을 위한 필드
            defaults={
               
                'cell0_voltage': M0_C0_voltage,
                'cell0_soc': M0_C0_SOC,
                'cell1_voltage': M0_C1_voltage,
                'cell1_soc':M0_C1_SOC,
                'cell2_voltage': M0_C2_voltage,
                'cell2_soc': M0_C2_SOC,
                'cell3_voltage': M0_C3_voltage,
                'cell3_soc':M0_C3_SOC,
               
            }
        )
        
        print(M0_C0_voltage)
        print(M0_C0_SOC)
        print(M0_C1_voltage)
        print(M0_C1_SOC)
        

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
 