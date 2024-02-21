from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article,Relationship

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        r = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if not dictionary.get('main'):
                continue
            elif dictionary['main'] is True:
                r += 1
        if r == 0:
            raise ValidationError('Choose a main theme')
        elif r > 1:

            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('You can not choose more than one!')
        return super().clean()  # вызываем базовый код переопределяемого метода

class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [Relationship]
    save_on_top = True
