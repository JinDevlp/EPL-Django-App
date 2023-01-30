from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

"""
need to import this to app.py
def read(self):
    import user.signals
"""

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def updateUser(sender,instance,created, **kwargs):
    profile = instance
    user = profile.user

    if created == False: # Make sure user is not created
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender,instance, **kwargs):
    try:
        user = instance.user
        user.delete()
        print("Deleting User...")
    except:
        pass

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)