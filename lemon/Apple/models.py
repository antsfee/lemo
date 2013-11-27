from django.db import models

class User(models.Model):
    ''' '''
    userName = models.CharField(max_length=128)
    passWord = models.CharField(max_length=128)
    #0 -- female, 1 -- male
    gender = models.IntegerField(default=1,blank=True)
    mail = models.CharField(max_length=128,blank=True)
    registerTime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.userName
    
class Album(models.Model):
    ''' '''
    albumName = models.CharField(max_length=128)
    albumDescription = models.TextField(blank=True)
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
    
    
    
class Article(models.Model):
    ''' '''
    title = models.CharField(max_length=128)
    content = models.TextField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
    

class Tag(models.Model):
    ''' '''
    tagName = models.CharField(max_length=64)
    tagDesctription = models.CharField(max_length=128,null=True)
    
    def __unicode__(self):
        return self.tagName
    
    

class Map_Tab(models.Model) :
    """"""
    tabName = models.CharField(max_length=120)



class Map_Tag(models.Model):
    
    tag = models.ForeignKey(Tag)
    
    # description the tag relate the 'table' name id
    
    maptab = models.ForeignKey(Map_Tab)
    
    

    
    
        
        
    
    