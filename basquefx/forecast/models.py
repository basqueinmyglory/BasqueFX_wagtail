from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.

class forecastIndex(Page):
    intro = RichTextField(blank = True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(forecastIndex, self).get_context(request)
        forecasts = self.get_children().live().order_by('-first_published_at')

        paginator = Paginator(forecasts, 1) # Show 1 resources per page

        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resources = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resources = paginator.page(paginator.num_pages)

        context['resources'] = resources
        return context



class forecast(Page):
    USD = 'USD'
    GBP = 'GBP'
    EUR = 'EUR'
    JPY = 'JPY'
    CAD = 'CAD'
    AUD = 'AUD'
    NZD = 'NZD'
    No_Option = '---'
    CURRENCY_OPTIONS = (
        (USD, 'USD'),
        (GBP, 'GBP'),
        (EUR, 'EUR'),
        (JPY, 'JPY'),
        (CAD, 'CAD'),
        (AUD, 'AUD'),
        (NZD, 'NZD'),
        (No_Option, '---'),
    )
    date = models.DateField("Post date")
    strong_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    strong_reason = RichTextField()
    weak_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    weak_reason = RichTextField()
    notes = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('strong_cur'),
        FieldPanel('strong_reason'),
        FieldPanel('weak_cur'),
        FieldPanel('weak_reason'),
        FieldPanel('notes', classname="full"),
    ]