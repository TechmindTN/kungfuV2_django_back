
import os

def get_upload_path(instance, filename):
    extension=filename.split(".").pop()
    name=str(instance.user)+"_"+str(instance.season)+"."+extension
    return os.path.join(
       instance.path, name)
