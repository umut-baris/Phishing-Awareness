from django.contrib import admin
from .models import Question, Answer, Video, Websites, Emails
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):

    list_display = ['ID', 'Phishing', 'Medium', 'URL', 'Screenshot']
    list_filter = ['Phishing', 'Medium']
    search_fields = ['URL']

    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)

class WebsitesAdmin(admin.ModelAdmin):

    list_display = ['ID', 'Phishing', 'URL', 'Html_Name']
    list_filter = ['Phishing']
    search_fields = ['URL']

    class Meta:
        model = Websites

admin.site.register(Websites, WebsitesAdmin)



class EmailsAdmin(admin.ModelAdmin):

    list_display = ['ID', 'Phishing', 'URL', 'Html_Name', 'CUTE']
    list_filter = ['Phishing', 'CUTE']
    search_fields = ['URL']

    class Meta:
        model = Emails

admin.site.register(Emails, EmailsAdmin)



class AnswerAdmin(admin.ModelAdmin):

    list_display = ['ID', 'answer']
    search_fields = ['answer']

    class Meta:
        model = Answer

admin.site.register(Answer, AnswerAdmin)

admin.site.register(Video)