from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import logging
import random
import time
from datetime import datetime,timedelta
from UserApp.models import User,ActivityPeriod

userNames = ['Olivia','Amelia','Isla','Ava','Emily','Monica','Joey','Chandler','Rachel','Phoebe','Ross','Shwetha']
userIds=['1111','9344','4567','1298','3333','4444','7777','4667','9087','9999','4109','1234']
timeZones = ['America/Iqaluit','Europe/Kirov','Asia/Almaty','Europe/Athens','Canada/Atlantic','Africa/Blantyre','Asia/Anadyr','America/St_Barthelemy','America/St_Johns','Europe/Moscow','Europe/Isle_of_Man','Antarctica/Davis']
start_date = "01-01-2019 00:00:00"
end_date = "01-01-2020 23:59:59"

def getStartEndDate(start=start_date, end=end_date):
    frmt = '%d-%m-%Y %H:%M:%S'
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + random.random() * (etime - stime)
    dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return [dt,dt+timedelta(minutes=random.randint(1,60))]

def getUser():
    index = random.randint(0, 11)
    return [userNames[index],userIds[index]]

def getTZ():
    return random.choice(timeZones)   

logger = logging.getLogger(__name__)
  
class Command(BaseCommand):
    #print sys.argv
    args = ''
    help = 'Populate User data to DB. Pass the number of entries to insert to DB as an argument.'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('datacount', nargs='+', type=str)

    def handle(self, *args, **options):  
        try:
            runTasks(options['datacount'])
        except Exception as e:                
            self.stdout.write('Error %s' % e) 
            logger.exception(e)
        self.stdout.write('done')      
        return

def runTasks(inputList) :
    try:
        print "Start Script"
        for i in xrange(int(inputList[0])):
            startDate,endDate = getStartEndDate()
            userName,userId = getUser()
            tz = getTZ()
            obj = User(userId=userId,userName=userName,tz=tz)
            obj.save()
            obj.activityperiod_set.create(startTime=startDate,endTime=endDate)
    except Exception as E:
        print E
        logger.info(str(E));
