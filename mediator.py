import services

class MessageBus(object):
    def __init__(self, *args, **kwargs):
        self.services = [services.DockService(), services.MainServiceUpdate()]# [services.Service(), services.MainService(), services.HelpService(), services.GoogleService(), services.MainServiceUpdate(), services.DockService()]

    def register_service(self, service):
        pass

    def remove_service(self, service):
        pass

    def notify(self, sender, message):
        for service in self.services:
            service.notify(sender, message)