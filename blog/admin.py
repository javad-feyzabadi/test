from django.contrib import admin
from . models import Article,Category

#create actions 
def make_published(modeladmin,request,queryset):
    row_updated = queryset.update(status ='P')
    if  row_updated == 1 :
        message_bit = '1 article was'
    else:
        message_bit = '%s article were' % row_updated
    modeladmin.message_user(request,'%s succesfuly marked as published')
make_published.short_description = 'mark selected article as published'

def make_draft(modeladmin,request,queryset):
    row_updated = queryset.update(status = 'D')
    if  row_updated == 1 :
        message_bit = '1 article was'
    else:
        message_bit = '%s article were' % row_updated
    modeladmin.message_user(request,'%s succesfuly marked as drafted')
make_draft.short_description = 'mark selected article as drafted'

class CategoryAdmin(admin.ModelAdmin):
    list_display=("position","title","slug","status","parent")
    list_filter =(["status"])
    search_fields =('title','slug')
    prepopulated_fields={'slug':('title',)}



class ArticleAdmin(admin.ModelAdmin):
    list_display=("title",'thumbnail_tag',"slug","publish","status","get_category")
    list_filter =("publish","status")
    search_fields =('title','description')
    prepopulated_fields={'slug':('title',)}
    ordering = ["status","-publish"]
    actions = [make_published,make_draft]

    def get_category(self,obj):
        return ", ".join([category.title for category in obj.categorey_published()])

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
