""" from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post) """

""" from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Post, PostAdmin) """

from django.contrib import admin
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        # Aggregate articles per day
        chart_data = (
            Article.objects.annotate(date=TruncDay("createdDate"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )
        
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Article, ArticleAdmin)


from django.contrib import admin
from .models import ContactSubmission

# admin.py

from django.contrib import admin
from django.db.models.functions import TruncHour, TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'message')

    change_list_template = 'admin/posts/contactsubmission/contact_chart.html'

    def changelist_view(self, request, extra_context=None):
        # Aggregate submissions per hour and day
        chart_data_hour = (
            ContactSubmission.objects.annotate(hour=TruncHour('submitted_at'))
            .values('hour')
            .annotate(count=Count('id'))
            .order_by('hour')
        )

        chart_data_day = (
            ContactSubmission.objects.annotate(day=TruncDay('submitted_at'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )

        # Serialize data for use in JavaScript
        chart_data_hour_json = json.dumps(list(chart_data_hour), cls=DjangoJSONEncoder)
        chart_data_day_json = json.dumps(list(chart_data_day), cls=DjangoJSONEncoder)

        extra_context = {
            'chart_data_hour': chart_data_hour_json,
            'chart_data_day': chart_data_day_json,
        }

        return super().changelist_view(request, extra_context=extra_context)


from django.contrib import admin
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Post

class PostAdmin(admin.ModelAdmin):
    change_list_template = 'admin/posts/post/change_list.html'
    list_display = ('title', 'author', 'created_at')

    def changelist_view(self, request, extra_context=None):
        # Aggregate post count per author
        chart_data = (
            Post.objects.values('author')
            .annotate(y=Count('id'))
            .order_by('author')
        )
        
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Post, PostAdmin)


# sub

from .models import NewsletterUser

@admin.register(NewsletterUser)
class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    search_fields = ('email',)
    readonly_fields = ('created',)


# csv
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import admin
from django.urls import path
from .models import NewsletterUser

# Define the action for exporting emails to CSV
def export_emails_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'
    writer = csv.writer(response)
    writer.writerow(['Email'])

    for user in queryset:
        writer.writerow([user.email])

    return response

export_emails_to_csv.short_description = 'Export selected emails to CSV'

# Define the admin model for NewsletterUser
class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    actions = [export_emails_to_csv]

# Extend the NewsletterUserAdmin to include the custom URL
class CustomNewsletterUserAdmin(NewsletterUserAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('export/', self.admin_site.admin_view(self.export_emails_to_csv_view), name='export_emails_to_csv'),
        ]
        return custom_urls + urls

    def export_emails_to_csv_view(self, request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/admin/')
        queryset = self.model.objects.all()
        return export_emails_to_csv(self, request, queryset)

# Unregister the old admin and register the new one
admin.site.unregister(NewsletterUser)
admin.site.register(NewsletterUser, CustomNewsletterUserAdmin)
