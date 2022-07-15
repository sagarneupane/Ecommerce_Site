from django.template.defaultfilters import filesizeformat
from django.db.models import FileField
from django.forms import forms


class ContentRestrictionFileField(FileField):
    
    def __init__(self,*args,**kwargs):
        self.content_types = kwargs.pop("content_types",[])
        self.max_upload_size = kwargs.pop("max_upload_size",0)
        
        super(ContentRestrictionFileField,self).__init__(*args,**kwargs)
        
    def clean(self,*args,**kwargs):
        data = super(ContentRestrictionFileField,self).clean(*args,**kwargs)
        
        file = data.file
        
        try:
            content_type = file.content_type
            
            if content_type in self.content_types:
                
                if file.size > self.max_upload_size:
                    raise forms.ValidationError(("Please Keep filesize under %s. Current file size is %s") %(filesizeformat(self.max_upload_size),
                                                                                                             filesizeformat(file.size)))
        except AttributeError:
            pass
        
        return data