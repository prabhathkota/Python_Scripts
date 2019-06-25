**What is Celery**

•	Celery is an asynchronous task queue. It can be used for anything that needs to be run asynchronously, e.g., background computation of expensive queries. 

**What is RabbitMQ**

•	RabbitMQ is a message broker widely used with Celery

**Steps to install**

    pip install celery

    brew install rabbitmq

    PATH=$PATH:/usr/local/sbin

    Start RabbitMQ server

    rabbitmq-server


**How to configure RabbitMQ?**

    rabbitmqctl add_user prabhath prabhath123

    rabbitmqctl add_vhost prabhath_vhost

    rabbitmqctl set_user_tags prabhath prabhath_tag

    rabbitmqctl set_permissions -p prabhath_vhost prabhath ".*" ".*" ".*"


**Project Structure**

    test_celery
        • celery.py
        • run_tasks.py
        • tasks.py


**How to run?**

$ python -m test_celery.run_tasks

    Task finished? False
    Task result: None
    Task finished? False
    Task result: None

