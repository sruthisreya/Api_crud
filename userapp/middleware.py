class CustomMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print(f"request method:{request.method} request path:{request.path}")
        response = self.get_response(request)
        print(f"Response Status Code: {response.status_code}")
        return response
        
    