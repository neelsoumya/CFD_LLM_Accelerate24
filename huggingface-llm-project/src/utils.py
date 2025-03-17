def validate_input(data):
    if not isinstance(data, str) or not data.strip():
        raise ValueError("Input must be a non-empty string.")

def format_response(response):
    return {
        "status": "success",
        "data": response
    }

def handle_error(error_message):
    return {
        "status": "error",
        "message": error_message
    }