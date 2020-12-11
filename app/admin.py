from django.contrib import admin

from app.models import *


# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    class Media:
        js = ('temp.js', 'bootstrap.min.js')

    list_display = ['sid', 'name', 'gender', 'campus_html', 'phone', 'major_html', 'sushe']
    search_fields = ['name', 'campus', 'phone', 'major']


class SuSheInfoAdmin(admin.ModelAdmin):
    class Media:
        js = ('temp.js', 'bootstrap.min.js')

    list_display = ['lv', 'ssid', 'size', 'extra', 'stus']
    search_fields = ['ssid', 'lv', 'extra']


admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(SuSheInfo, SuSheInfoAdmin)

admin.site.site_title = "学生宿舍管理系统"
admin.site.site_header = "学生宿舍管理系统"
