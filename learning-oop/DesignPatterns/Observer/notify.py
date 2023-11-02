from facebook import Event
from facebook import EmailDelivery
from facebook import PushNotification
from facebook import SMSNotification

event = Event()

email = EmailDelivery()
push = PushNotification()
sms = SMSNotification()

event.subscribe(email)
event.subscribe(push)
event.subscribe(sms)

print(event._observers)

event.notify('E ziua lui Ion')
