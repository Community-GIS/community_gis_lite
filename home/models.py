from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from streams import blocks

class HomePage(Page):
    template="home/home_page.html"
    content= StreamField(
        [ 
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True
    )
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        StreamFieldPanel("content"),   
    ]
    class Meta:
        verbose_name="home_page"
        verbose_name_plural="home_pages"

