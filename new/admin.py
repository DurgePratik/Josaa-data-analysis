from django.contrib import admin
from .models import Admission
from .models import Contact

# Register your models here.
admin.site.register(Admission)
admin.site.register(Contact)


# username: admin
# password: admin