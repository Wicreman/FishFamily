from django.db import models


class BranchInfo(models.Model):
    branch_name = models.CharField(max_length=30)
    from_build = models.CharField(max_length=40)
    to_build = models.CharField(max_length=40)
    layer = models.CharField(max_length=60, default='SYP')

    class Meta:
        verbose_name = "branch"
        db_table = 'gi_branch'
        ordering = ['branch_name']

    def __str__(self):
        return self.branch_name


class ChangeInfo(models.Model):
    branch = models.ForeignKey(BranchInfo, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=230)
    current_version = models.CharField(max_length=30, default='#')

    class Meta:
        db_table = 'gi_change'

    def __str__(self):
        return self.file_name
