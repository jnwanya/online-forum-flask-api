class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class BadRequestException(Exception):
    def __init__(self, message):
        self.message = message


class BusinessLogicConflictException(Exception):
    def __init__(self, message):
        self.message = message


class UnauthorisedAccessException(Exception):
    def __init__(self, message):
        self.message = message


error_description_dict = {
    # 200: 'Processed successfully',
    400: 'Bad Request, Check request details',
    401: 'Unauthorised request, invalid credential',
    404: 'Requested resource not found.',
    409: 'Business Logic Conflict. Error due to unfulfilled business rules',
    501: 'Internal server error occurred while processing your request'
}



