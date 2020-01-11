from rest.imports import models

class TimeTrack(models.Model):
    date_coding = models.DateField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    timezone = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_coding']
