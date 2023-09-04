from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Device, DeviceLog






@receiver(post_save, sender=Device)
def archive_order(sender, instance, created, **kwargs):
    if created:
        DeviceLog.objects.create(device=instance,company_name=instance.company, device_name = instance.name, condition= instance.condition, checked_out=instance.checked_out) 