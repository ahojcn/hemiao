from django.db import models
from django.utils.safestring import mark_safe


class SuSheInfo(models.Model):
    """
    宿舍信息
    """
    ssid = models.CharField(max_length=10, null=False, verbose_name='宿舍号')
    lv = models.IntegerField(verbose_name='宿舍楼层')
    size = models.IntegerField(choices=((2, '2人/间'), (4, '4/人间'), (6, '6/人间')), verbose_name='宿舍容量')
    extra = models.TextField(verbose_name='其他信息', default='暂无')

    def stus_property(self):
        stus = StudentInfo.objects.filter(ssid=self)
        res = "<table>"
        for i in stus:
            url = "/app/studentinfo/?q=" + str(i.name)
            res += f"<tr>" \
                   f"<td><a href='{url}'>{i.name}</a></td>" \
                   f"<td>{StudentInfo.CAMPUS_CHOICES[i.campus][1]}</td>" \
                   f"</tr>"
        res += "</table>"
        print(mark_safe(res))
        return mark_safe(res)

    stus_property.short_description = "学生"
    stus_property.allow_tags = True

    stus = property(stus_property)

    def __str__(self):
        return str(self.lv) + self.ssid + '(' + str(self.size) + ')'

    class Meta:
        verbose_name = '宿舍基本信息'
        verbose_name_plural = verbose_name
        ordering = ['lv', 'ssid']


class StudentInfo(models.Model):
    """
    学生信息
    """
    CAMPUS_CHOICES = ((0, '计算机科学学院'),
                      (1, '理学院'),
                      (2, '文学院'),
                      (3, '纺织学院'),
                      (4, '环境学院'),
                      (5, '城市学院'),
                      (6, '艺术学院'))
    sid = models.CharField(max_length=20, null=False, verbose_name='学号')
    name = models.CharField(max_length=50, null=False, verbose_name='姓名')
    campus = models.IntegerField(choices=CAMPUS_CHOICES, null=False, verbose_name='学院')
    major = models.CharField(max_length=50, null=False, verbose_name='专业')
    phone = models.CharField(max_length=20, null=False, verbose_name='手机')
    gender = models.BooleanField(choices=((0, '男'), (1, '女')), default=0, verbose_name='性别')
    ssid = models.ForeignKey(to=SuSheInfo, on_delete=models.CASCADE, related_name='宿舍', verbose_name='宿舍')

    def major_property(self):
        url = "/app/studentinfo/?q=" + str(self.major)
        return mark_safe(f'<a href="{url}">{self.major}</a>')

    major_property.short_description = "专业"
    major_property.allow_tags = True
    major_html = property(major_property)

    def campus_property(self):
        url = "/app/studentinfo/?q=" + str(self.CAMPUS_CHOICES[self.campus][1])
        return mark_safe(f'<a href="{url}">{self.CAMPUS_CHOICES[self.campus][1]}</a>')

    campus_property.short_description = "学院"
    campus_property.allow_tags = True
    campus_html = property(campus_property)

    def sushe_property(self):
        url = f'/app/susheinfo/?q={self.ssid.lv}+{self.ssid.ssid}'
        return mark_safe(f'<a class="temp2" href="{url}">{self.ssid}</a>')

    sushe_property.short_description = "宿舍"
    sushe_property.allow_tags = True
    sushe = property(sushe_property)

    def __str__(self):
        return self.name + '(' + self.CAMPUS_CHOICES[self.campus][1] + ',' + self.major + ')'

    class Meta:
        verbose_name = '学生基本信息'
        verbose_name_plural = verbose_name
        ordering = ['sid']
