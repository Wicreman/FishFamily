from django.db import models


class Issues(models.Model):
    titile = models.CharField(max_length = 100)
    description = models.TextField(null=True, blank= True)
    created_by = models.CharField(max_length= 30)
    created_date = models.DateTimeField()

    class Meta:
        db_table = 'gi_issue'

    def __str__(self):
        return self.titile

class Solutions(models.Model):
    issue = models.ForeignKey(Issues, on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(default=0)
    resolved_by = models.CharField(max_length= 30)
    resolved_date = models.DateTimeField()

    class Meta:
        db_table = 'gi_solution'

    def __str__(self):
        return self.content
