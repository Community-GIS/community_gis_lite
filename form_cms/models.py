from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

from wagtailleafletwidget.edit_handlers import GeoPanel


from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

class FormField(AbstractFormField):
    page = ParentalKey(
        'FormPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class FormPage(AbstractEmailForm):

    template = "form_cms/form_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "form/form_page_landing.html"

    # intro = RichTextField(blank=True)
    # thank_you_text = RichTextField(blank=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    content_panels = AbstractEmailForm.content_panels + [
        # FieldPanel('intro'),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label='Form Fields'),
        GeoPanel('location'),
        # FieldPanel('thank_you_text'),
        # MultiFieldPanel([
            # FieldRowPanel([
                # FieldPanel('from_address', classname="col6"),
                # FieldPanel('to_address', classname="col6"),
            # ]),
            # FieldPanel("subject"),
        # ], heading="Email Settings"),
    ]


