from antidote import world,LifeTime,LifetimeType

class ScopeMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):

        request_lifetime:LifetimeType= LifeTime.SCOPED
        response = self.get_response(request)
    
        return response