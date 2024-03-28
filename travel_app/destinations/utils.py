from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if response.status_code == 201:
            response.data = {'detail':'Record added successfully'}
            return response
        
        if response.status_code == 500:
            response.data = {'detail':'Url not specified clearly'}
            return response
        
        if response.status_code == 405:
            response.data = {'detail':'Method not allowed'}
            return response
        
        if response.status_code == 200:
            response.data = {'detail':'success'}
            return response
        
        if response.status_code == 404:
            response.data = {'detail':'record not found'}
            return response
        
        if response.status_code == 204:
            response.data = {'detail':'successfully deleted'}
            return response
        

        
    return response