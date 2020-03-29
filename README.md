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