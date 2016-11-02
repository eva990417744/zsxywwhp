from django.db import models


class Excle(models.Model):
    name = models.CharField(max_length=10)
    excle = models.FileField(upload_to='%Y/%m/%d/')
    add_time = models.DateField(auto_now=True)


class HP(models.Model):
    name = models.CharField(default='', max_length=50, verbose_name='hp_name')
    blood = models.IntegerField(default=50)
    add_time = models.DateField(auto_now_add=True)
    change_time = models.DateField(auto_now=True)
    grade_choices = (('one', 'one'),
                     ('two', 'two'),
                     ('three', 'three'))
    grade = models.CharField(choices=grade_choices, default='one', max_length=100)

    def debuff(self, name_text):
        q = DeBuff.objects.filter(name="%s" % name_text)
        return q

    def buff(self, name_text):
        q = DeBuff.objects.filter(name="%s" % name_text)
        return q

    def __str__(self):
        return self.name


class DeBuff(models.Model):
    key = models.ForeignKey(HP)
    name = models.CharField(max_length=50, default='', verbose_name='DeBuff_name')

    Level1 = ('值班没带工作证', '遗漏报修', '工单超时', '私活影响值班', '不签到', '值班联系不上','Other1')
    Level2 = ('不接电话', '工单被投诉', '不回短信', '旷工', '不能单刷',
              '对女生言行不当', '私自以网维名义发布消息', '查到路由不反映', '攻击网络',
              '使用路由器影响正常上网',
              '态度消极', '泄露资料', '被教职员工投诉','Other2')
    Level3 = ('认知不清', '泄露私人号码', '借出工作证', '丢失工作证',
              '宣传路由', '出售IP', '分裂', 'Other3')
    DeBuff_Choices = (
        ('Level1', (
            ('没带工作证', '没带工作证'),
            ('遗漏报修', '遗漏报修'),
            ('工单超时', '工单超时'),
            ('私活影响值班', '私活影响值班'),
            ('不签到', '不签到'),
            ('值班联系不上','值班联系不上'),
            ('Other1', 'Other'),
        ),
         ),
        ('Level2', (
            ('不接电话', '不接电话'),
            ('工单被投诉', '工单被投诉'),
            ('不回短信', '不回短信'),
            ('旷工', '旷工'),
            ('不能单刷', '不能单刷'),
            ('对女生言行不当', '对女生言行不当'),
            ('私自以网维名义发布消息', '私自以网维名义发布消息'),
            ('查到路由不反映', '查到路由不反映'),
            ('攻击网络', '攻击网络'),
            ('使用路由器影响正常上网', '使用路由器影响正常上网'),
            ('态度消极', '态度消极'),
            ('泄露资料', '泄露资料'),
            ('被教职员工投诉','被教职员工投诉'),
            ('Other2', 'Other2')
        )
         ),
        ('Level3', (
            ('认知不清', '认知不清'),
            ('泄露私人号码', '泄露私人号码'),
            ('借出工作证', '借出工作证'),
            ('丢失工作证', '丢失工作证'),
            ('宣传路由', '宣传路由'),
            ('出售IP', '出售IP'),
            ('分裂', '分裂'),
            ('Other3', 'Other3')
        )
         )
    )

    DeBuff_Reason = models.CharField(choices=DeBuff_Choices, max_length=100)
    DeBuff_Text = models.CharField(max_length=100, default='none', blank=True)
    add_time = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(DeBuff, self).save(*args, **kwargs)
        q = HP.objects.get(name=self.name)
        if self.DeBuff_Reason in self.Level1:
            q.blood -= 10
            q.save()
        elif self.DeBuff_Reason in self.Level2:
            q.blood -= 20
            q.save()
        elif self.DeBuff_Reason in self.Level3:
            q.blood -= 30
            q.save()


class Buff(models.Model):
    key = models.ForeignKey(HP)
    name = models.CharField(default='', max_length=50, verbose_name='Buff_name')

    Buff_Choices = (
        ('工作积极', '工作积极'),
        ('表现良好', '表现良好'),
        ('加班', '加班'),
        ('态度积极', '态度积极'),
        ('贡献想法', '贡献想法')
    )
    Buff_Reason = models.CharField(choices=Buff_Choices, max_length=100)
    Buff_Text = models.CharField(max_length=100, default='none', blank=True)
    add_time = models.DateField(auto_now_add=True, null=True)
    Level = ('工作积极', '表现良好', '加班', '态度积极', '贡献想法',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Buff, self).save(*args, **kwargs)
        q = HP.objects.get(name=self.name)
        q.blood += 5
        q.save()
