def api_response(data=None, message="", status=200):
    return {
        "data": data,
        "message": message,
        "status": status
    }