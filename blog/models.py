from datetime import datetime, timezone
from django.db import models
from django.conf import settings
from django.utils.text import slugify
import pytz

class Blog(models.Model):
    CATEGORY = (
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Lifestyle', 'Lifestyle'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Entertainment', 'Entertainment'),
        ('Sports', 'Sports'),
        ('Fashion', 'Fashion'),
        ('Science', 'Science'),
        ('Politics', 'Politics'),
        ('Art', 'Art'),
        ('History', 'History'),
        ('Music', 'Music'),
        ('Other', 'Other')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORY,blank=True, null=True)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)  # Ensure slugify works
        slug = base_slug
        num = 1  

        while Blog.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{num}'
            num += 1

        self.slug = slug  # Set the final slug correctly

        if not self.is_draft and self.published_date is None:
            india_tz = pytz.timezone('Asia/Kolkata')
            current_time = datetime.now(india_tz)
            self.published_date = current_time

        super().save(*args, **kwargs)
