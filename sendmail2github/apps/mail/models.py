from django.db import models


class MailTicket(models.Model):

    githubIssueNumber = models.IntegerField(null=False, db_index=True)
    mailMessageId = models.CharField(null=False, max_length=1024)
    mailSenderAddress = models.CharField(null=False, max_length=1024)
    mailTitle = models.CharField(null=False, max_length=1024)
