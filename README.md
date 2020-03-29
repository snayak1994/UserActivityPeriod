# UserActivityPeriod
Project maintains user details in DB along with his activity time intervals. This projects provides an API to fetch user details based on the input time interval.

Note : Python version used 2.7.13

# Instructions to run the project 
cd UserActivityPeriod
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate UserApp
python manage.py populateUserData 50 //Where 50 is the number of entried to populate in DB
pyton manage.py runserver


Sample request and response:
Request:
	http://127.0.0.1:8000/users/getdata?starttime=2019-12-05&endtime=2020-01-01
Response:
``` json
	{"ok": true, "members": [{"tz": "Canada/Atlantic", "activity_periods": [{"start_time": "Jan 01 2020 05:03:55.000000", "end_time": "Jan 01 2020 05:51:55.000000"}], "id": "3333", "real_name": "Emily"}, {"tz": "Antarctica/Davis", "activity_periods": [{"start_time": "Dec 13 2019 04:15:08.000000", "end_time": "Dec 13 2019 04:50:08.000000"}], "id": "1234", "real_name": "Shwetha"}, {"tz": "Asia/Almaty", "activity_periods": [{"start_time": "Dec 18 2019 11:29:44.000000", "end_time": "Dec 18 2019 12:24:44.000000"}, {"start_time": "Dec 10 2019 17:31:32.000000", "end_time": "Dec 10 2019 17:58:32.000000"}], "id": "4567", "real_name": "Isla"}, {"tz": "America/St_Barthelemy", "activity_periods": [{"start_time": "Dec 05 2019 14:07:13.000000", "end_time": "Dec 05 2019 14:28:13.000000"}], "id": "4667", "real_name": "Chandler"}]}
```