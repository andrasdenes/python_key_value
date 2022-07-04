from abc import ABC, abstractmethod

class RequestHandler(ABC):

    @abstractmethod
    def handle(request):
        raise NotImplementedError