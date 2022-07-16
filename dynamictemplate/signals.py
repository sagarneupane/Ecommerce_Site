from django.db.models.signals import post_delete,pre_save,post_save
from dynamictemplate.models import Logo,CarosulData
from django.dispatch import receiver


@receiver(post_delete,sender=CarosulData)
def post_delete_CarosulData(sender,instance,*args,**kwargs):
    
    try:
        instance.headline_image.delete(save=False)
    except:
        pass

@receiver(pre_save,sender=CarosulData)
def pre_save_carosulData(sender,instance,*args,**kwargs):
    
    try:
        old_data = instance.__class__.objects.get(id=instance.id).headline_image.path
        try:
            new_data = instance.headline_image.path
        
        except:
            new_data = old_data
        
        if new_data!= old_data:
            import os
            if os.path.exists(old_data):
                os.remove(old_data)
    except:
        pass


@receiver(post_delete,sender=Logo)
def post_delte_Logo(sender,instance,*args,**kwargs):
    
    try:
        instance.logo_image.delete(save=False)
    except:
        pass

@receiver(pre_save,sender=Logo)
def pre_save_Logo(sender,instance,*args,**kwargs):
    
    try:
        old_image_path = instance.__class__.objects.get(id=instance.id).logo_image.path
        
        try:
            new_image_path = instance.logo_image.path

        except:
            new_image_path = old_image_path
        
        if new_image_path != old_image_path:
            import os
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
    
    except:
        pass
