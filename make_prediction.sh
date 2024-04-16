
echo "Starting the script" >> /tmp/fetch_and_call_api.log

echo "PATH is $PATH" >> /tmp/fetch_and_call_api.log

echo "Python path: $(which python)" >> /tmp/fetch_and_call_api.log

source /Users/jeremyvangansbeg/venv/bin/activate

echo "Environment activated" >> /tmp/fetch_and_call_api.log

python /Users/jeremyvangansbeg/Documents/project/celery_django_rest/manage.py fetch_api_and_call >> /tmp/fetch_and_call_api.log 2>&1

echo "Script completed" >> /tmp/fetch_and_call_api.log
