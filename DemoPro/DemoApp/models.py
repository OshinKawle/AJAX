from django.db import models
STATUS = ((0, 'Started'), (1, 'Done'))

from datetime import datetime

class Banner(models.Model):
    b_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='',  default='path/to/my/default/image.jpg')
    status = models.SmallIntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #deleted_at = models.DateTimeField(blank=True, default=None)
    deleted_at = models.BooleanField( verbose_name="Is Deleted",default=True)
    contents = models.TextField()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()


'''
    def delete(self, *args, **kwargs):
        if self.is_deleted: return
        self.is_deleted = True
        self.save()

'''

class University(models.Model):

    uni_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='', default='path/to/my/default/image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)
    contents = models.TextField()
    def __str__(self):
        return self.name
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    uni_id = models.ForeignKey(University,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)
    contents = models.TextField()
    def __str__(self):
        return str(self.course_id)

class Specialization(models.Model):
    s_id = models.AutoField(primary_key=True)
    uni_id = models.ForeignKey(University, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course_id_specialization_set")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)
    contents = models.TextField()






