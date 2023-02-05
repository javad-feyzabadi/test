from django.contrib import admin

from . models import Article,Category,IPAddress

from accounts.models import User

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
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display=("title","author",'thumbnail_tag',"slug","publish","is_special","status","get_category")
    list_filter =("publish","status",'author')
    search_fields =('title','description')
    prepopulated_fields={'slug':('title',)}
    ordering = ["status","-publish"]
    actions = [make_published,make_draft]


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(IPAddress)
