from django.contrib import admin

from setmeup.models import LichBaoCao
from baocao.models import BaoCao, MediaFile

# Register your models here.
admin.site.register(LichBaoCao)
admin.site.register(BaoCao)
admin.site.register(MediaFile)