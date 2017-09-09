# Celery settings as described here 
# http://docs.celeryproject.org/en/latest/userguide/configuration.html
broker_url = 'pyamqp://guest@localhost//'
result_backend = 'rpc://'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

# Verify that your configuration file works properly
# python -m celeryconfig