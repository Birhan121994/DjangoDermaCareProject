from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import BlogPost , LatestNews

class BlogPostFeed(Feed):
    title = "My Blog"
    link = "/blog/"
    description = "The latest news from my blog."
    def items(self):
        return BlogPost.objects.order_by('-date_posted')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('DermaBlogDetailsPage', args=[item.pk])



