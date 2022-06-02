import os
import random
from django import template

register = template.Library()

@register.simple_tag
def random_image(request):
    img = random.choice(os.listdir('blog/static/images'))
    return 'static/images/' + img