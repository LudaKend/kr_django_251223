from django.db import models
from spammer.models import Spammer

NULLABLE = {'null': True, 'blank': True}


class Mailing(models.Model):
    '''класс-модель для рассылок'''
    subject = models.CharField(max_length=100, verbose_name='Тема')
    #spammer = models.ForeignKey('spammer.Spammer', on_delete=models.CASCADE, verbose_name='ФИО менеджера')
    spammer = models.ForeignKey(Spammer, on_delete=models.CASCADE, verbose_name='ФИО менеджера')
    mailing_text = models.TextField(verbose_name='Текст письма', **NULLABLE)
    time = models.TimeField(verbose_name='время отправки', **NULLABLE)
    period = models.ForeignKey('Period', on_delete=models.CASCADE,verbose_name='периодичность', **NULLABLE)
    status = models.ForeignKey('StatusMailing', on_delete=models.CASCADE,verbose_name='статус', default=0)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.subject}, {self.spammer}, {self.spammer_id}, {self.time}, {self.period}, {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Period(models.Model):
    '''вспомогательный справочник для выбора периодичности запуска рассылок'''
    period = models.CharField(max_length=100, verbose_name='периодичность')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.period}'

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'


class StatusMailing(models.Model):
    '''вспомогательный справочник со статусами рассылок'''
    status = models.CharField(max_length=100, verbose_name='статус')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.status}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
