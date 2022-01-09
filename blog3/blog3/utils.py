import uuid#random olarak harflerden ve rakamlardan olusan uniq id olusturur
from .models import Post
def get_random_code():
    code=str(uuid.uuid4())[:11].replace("-","")
    return code
#print(get_random_code())normalde baya uzun bir id getiriyor biz- sizilk 11 i tercih ettik

