from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    title=blocks.CharBlock(required=True, help_text="Add your title")
    cards=blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("description",blocks.CharBlock(required=True, max_length=140)),
                ("url",blocks.CharBlock(required=True, max_length=150)),
                ("button_page_name",blocks.CharBlock(required=True, max_length=40)),    
                ]
                  
        )
    )
    class Meta:
        template = "streams/demo.html"
        icon="placeholder"
        label="staff cards"

