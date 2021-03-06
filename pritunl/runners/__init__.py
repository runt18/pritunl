from pritunl.runners.settings import start_settings
from pritunl.runners.updates import start_updates
from pritunl.runners.transaction import start_transaction
from pritunl.runners.task import start_task
from pritunl.runners.queue import start_queue
from pritunl.runners.host import start_host
from pritunl.runners.subscription import start_subscription
from pritunl.runners.server import start_server
from pritunl.runners.time_sync import start_time_sync
from pritunl.runners.listener import start_listener

def start_all():
    start_settings()
    start_updates()
    start_transaction()
    start_task()
    start_queue()
    start_host()
    start_subscription()
    start_server()
    start_time_sync()

    start_listener()
