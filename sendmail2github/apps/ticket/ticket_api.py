from github import Github
from django.conf import settings


class TicketApi:
    """
    Class TicketApi
    """

    def __init__(self, git_hub=None):
        """
        Init class
        """
        if git_hub is not None:
            self.git_hub = git_hub
        else:
            self.git_hub = Github(base_url="https://api.github.com", login_or_token=settings.GITHUB_TOKEN)

        self.repo = self.git_hub.get_repo(settings.GITHUB_REPO)

    def get_label(self, name):
        """
        get label
        """

        try:
            return self.repo.get_label(
                name=name,
            )
        except:
            return None

    def get_or_create_label(self, name, color):
        """
        Get or Create label
        """

        label = self.get_label(name)

        if label is not None:
            return label
        else:
            return self.repo.create_label(
                name=name,
                color=color,
            )

    def get_or_create_label_user(self, mail):
        """
        Get or create label for user
        """

        return self.get_or_create_label(
            name='User: {mail}'.format(mail=mail.lower()),
            color='17a2b8')

    def get_or_create_label_status_new(self):
        """
        Get or create label status new
        """

        return self.get_or_create_label(
            name='Status: New',
            color='28a745'
        )

    def get_or_create_label_status_in_progress(self):
        """
        Get or create label status progress
        """

        return self.get_or_create_label(
            name='Status: In Progress',
            color='ffc107'
        )

    def create_issue(self, title, body, labels):
        """
        Create issue
        """

        return self.repo.create_issue(
            title=title,
            body=body,
            labels=labels
        )

    def search_labels(self, filter_name):
        """
        Search labels
        """

        user_labels = []
        labels = self.repo.get_labels()

        print(labels)
        for label in labels:
            if filter_name in label.name:
                user_labels.append(label)
        return user_labels

    def search_user_labels(self):
        """
        Search User Labels
        """
        return self.search_labels('User: ')

    def search_status_labels(self):
        """
        Search status labels
        """

        return self.search_labels('Status: ')

    def get_tickets(self, labels, state='open'):
        """
        get tickets
        """

        filter_labels = []
        for label_name in labels:
            filter_label = self.get_label(label_name)
            if filter_label is not None:
                filter_labels.append(filter_label)

        return {
            'repo': self.repo,
            'users': self.search_user_labels(),
            'status': self.search_status_labels(),
            'labels': self.repo.get_labels(),
            'assignees': self.repo.get_assignees(),
            'issues':
                self.repo.get_issues(
                    state=state,
                    labels=filter_labels
                ),

        }

    def get_ticket(self, number):
        """
        get ticket
        """

        return self.repo.get_issue(number=number)

    def create_comment(self, number, comment):
        """
        Create comment
        """
        return self.repo.get_issue(number=number).create_comment(body=comment)
