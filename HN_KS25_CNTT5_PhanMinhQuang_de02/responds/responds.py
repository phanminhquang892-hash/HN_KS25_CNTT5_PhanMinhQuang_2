from fastapi.responses import JSONResponse

def response(status, message, data=None, error=None):
    return JSONResponse(status_code=status, content={'statusCode': status, 'error': error, 'message': message, 'data': data})
