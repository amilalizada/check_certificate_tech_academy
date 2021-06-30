from django.db import models

# Create your models here.
class Certificate(models.Model):



    """This field is for category types like: food,desert and others"""
    title = models.CharField('Title',max_length=60)
    certificade_number =models.IntegerField()
    fullname = models.CharField('Fullname',max_length=50)
    image = models.FileField('Image',upload_to = 'certificate_images')
    description = models.TextField('Description')
    instructor = models.CharField('Instructor',max_length=50)
    training_session=models.CharField('Session',max_length=120)
    started_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(auto_now=True)

    #moderations
    is_published = models.BooleanField('is published', default=True)
    order = models.PositiveIntegerField('Order',default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
    def __str__(self):
        return self.title