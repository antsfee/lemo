from django.db import models

class User(models.Model):
    ''' '''
    userName = models.CharField(max_length=128)
    passWord = models.CharField(max_length=128)
    #0 -- female, 1 -- male
    gender = models.IntegerField()
    mail = models.CharField(max_length=128)
    registerTime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.userName
    
class Album(models.Model):
    ''' '''
    albumName = models.CharField(max_length=128)
    albumDescription = models.TextField()
    albumCreateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.albumName
    
    
class Photo(models.Model):
    ''' '''
    photoName = models.CharField(max_length=128)
    photoPath = models.CharField(max_length=128)
    album = models.ForeignKey(Album)
    
    def __unicode__(self):
        return self.photoName
    
    
class Tag(models.Model):
    ''' '''
    tagName = models.CharField(max_length=64)
    tagDesctription = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.tagName
    
    
class Article(models.Model):
    ''' '''
    title = models.CharField(max_length=128)
    content = models.TextField()
    tag = models.ForeignKey(Tag)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
