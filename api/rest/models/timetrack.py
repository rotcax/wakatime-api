from rest.imports import models

class TimeTrack(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    timezone = models.CharField(max_length=150)

    class Meta:
        ordering = ['created_at']
