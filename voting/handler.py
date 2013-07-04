from rapidsms.contrib.handlers import KeywordHandler
from voting.models import Choice
from django.db.models import F


class ResultHandler(KeywordHandler):
    keyword = 'results'

    def help(self):
        parts = []
        for choice in Choice.objects.all():
            part = "%s, %d" % (choice.name, choice.votes)
            parts.append(part)
        msg = '; '.join(parts)
        self.respond(msg)

    def handle(self, text):
        self.help()


class VoteHandler(KeywordHandler):
    keyword = 'vote'

    def help(self):
        choices='|'.join(Choice.objects.value_list('name', flat=True))
        self.respond("Valid commands: VOTE <%s>" % choices)


    def handle(self, text):
        text = text.strip()
        try:
            choice = Choice.objects.get(name__iexact=text)
        except Choice.DoesNotExist:
            #send help
            self.help()
        else:
            # Count the vote. Use update to do it in a single query
            # to avoid race conditions.
            Choice.objects.filter(name__iexact=text).update(votes=F('votes')+1)
            self.respond("Your vote for %s has been counted" % text)
        