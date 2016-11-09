from django.db import models

# Create your models here.
class Tag(models.Model):
    #Tags
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):

        
        return self.tag_name

class Author(models.Model):
    #Authors
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Blog(models.Model):
    #NEWS
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    content2 =models.TextField(blank=True)
    content3 =models.TextField(blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    
    pic = models.ImageField(upload_to = 'images/',blank = True )
    pic2 = models.ImageField(upload_to = 'images/',blank = True )
    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)

    class Meta:
        ordering=['-publish_time']



