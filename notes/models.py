from django.db import models

class Note(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, blank=False, null=False)
    text = models.TextField(verbose_name='Описание', blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        db_table = 'note_t'