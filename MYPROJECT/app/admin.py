from django.contrib import admin

from .models import State
from .models import City
from .models import UserRegister
from .models import BuyUsedcars
from .models import SellUsedcars
from .models import Newcars



admin.site.register(State)
admin.site.register(City)
admin.site.register(UserRegister)
admin.site.register(BuyUsedcars)
admin.site.register(SellUsedcars)
admin.site.register(Newcars)


