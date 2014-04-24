#coding:utf-8
from django.contrib import admin
from polls.models import Choice, Poll

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question"]
    fieldsets = [
        (None, {"fields":["question"]}),
        ("时间信息", {"fields":["pub_date"], "classes":["collapse"]}, ),
    ]
    inlines = [ChoiceInline]
    list_display = ("question", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question"]

admin.site.register(Poll, PollAdmin)
