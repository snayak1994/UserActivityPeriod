from django.http import HttpResponse
from models import User,ActivityPeriod
from datetime import datetime
import json
from django.db.models import Q

def getUserTableData(userId):
    u = User.objects.get(userId=userId)
    return [u.userName,u.tz]

def getUserData(request):
    result = {"ok":False,
                        "members":[]}
    
    if request.method=='GET':
        try:
            startTime = request.GET.get('starttime')
            endTime = request.GET.get('endtime')
            start = datetime.strptime(startTime, '%Y-%m-%d')
            end = datetime.strptime(endTime, '%Y-%m-%d')
            a = ActivityPeriod.objects.filter(Q(startTime__date__gte=start)&Q(endTime__date__lte=end))
            for i in a :
                data = {"start_time":i.startTime.strftime("%b %d %Y %H:%M:%S.%f"),"end_time":i.endTime.strftime("%b %d %Y %H:%M:%S.%f")}
                if len(result["members"])>0:
                    flag = False
                    for each in result["members"]:
                        if each["id"] == i.userId_id:
                            each["activity_periods"].append(data)
                            flag = True
                    if not flag:
                            temp = {}
                            temp["id"] = i.userId_id
                            temp["activity_periods"] = [data]
                            res = getUserTableData(i.userId_id)
                            temp["real_name"] = res[0]
                            temp["tz"] = res[1]
                            result["members"].append(temp)
                else:
                    temp = {}
                    temp["id"] = i.userId_id
                    temp["activity_periods"] = [data]
                    res = getUserTableData(i.userId_id)
                    temp["real_name"] = res[0]
                    temp["tz"] = res[1]
                    result["members"].append(temp) 
            result["ok"] = True
            response = HttpResponse(json.dumps(result))
            response['Status'] = 'OK'
        except Exception,e:
            result["ok"] = False
            result["members"] = []
            response = HttpResponse(json.dumps(result))
            response['Status'] = 'DateTime should be in the format %Y-%m-%d'
    return response
