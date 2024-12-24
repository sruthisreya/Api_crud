
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Peoples


@receiver(post_save, sender=Peoples)
def person_saved(sender, instance, created,**kwargs):
    if created:
        if not instance.user_id:
            instance.user_id = f"USER-{ Peoples.objects.count()}"
            instance.save(update_fields=['user_id'])
            print(f"A new person created with user_id:{instance.user_id},{instance.name},{instance.age}")
    else:
        print(f"Person updated:{instance.user_id},{instance.name},{instance.age}")


@receiver(post_delete, sender=Peoples)
def person_deleted(sender, instance,**kwargs):
    print(f"Person deleted: {instance.user_id}")