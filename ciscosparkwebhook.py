from errbot import BotPlugin, webhook

class MyCiscoSparkWebhook(BotPlugin):
    @webhook('/errbot/spark')
    def test(self, request):
        self.log.debug(repr(request))
        return "OK"
