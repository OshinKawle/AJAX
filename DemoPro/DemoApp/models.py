from django.db import models
STATUS = ((0, 'Started'), (1, 'Done'))



class Banner(models.Model):
    b_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='',  default='path/to/my/default/image.jpg')
    status = models.SmallIntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    #is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")
    contents = models.TextField()
'''
    def delete(self, *args, **kwargs):
        if self.is_deleted: return
        self.is_deleted = True
        self.save()

'''

class University(models.Model):

    uni_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='Images', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    contents = models.TextField()
    def __str__(self):
        return self.name
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    uni_id = models.ForeignKey(University,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
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
    deleted_at = models.DateTimeField(auto_now=True)
    contents = models.TextField()






