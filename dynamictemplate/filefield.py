from django.template.defaultfilters import filesizeformat
from django.db.models import FileField
from django.forms import forms
from django.core.files.images import get_image_dimensions

class ContentRestrictionFileField(FileField):
    
    def __init__(self,*args,**kwargs):
        self.content_types = kwargs.pop("content_types",[])
        self.max_upload_size = kwargs.pop("max_upload_size",0)
        self.width = kwargs.pop("width",0)
        self.height = kwargs.pop("height",0)
        
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
                width,height = get_image_dimensions(file)
                print(self.width)
                if self.width==0 or self.height==0:
                    pass
                elif self.width - 10 <= width <= self.width + 10 and self.height - 10 <= height <= self.height + 10:
                    pass
                else:
                    raise forms.ValidationError(("Please Upload the image of dimensions %spx X %spx. Your Current Dimensions is %spx X %spx ")
                                                %(self.width,self.height,width,height))
        except AttributeError:
            pass
        
        return data