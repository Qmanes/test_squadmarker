class NotFoundException(Exception):
    
    def __init__(self, title):

        self.message = "{title} Not Found".format(title = title)
        super().__init__(self.message)

class UrlNotValidException(Exception):
    
    def __init__(self, title):

        self.message = "{title} isn't a url valid".format(title = title)
        super().__init__(self.message)

class NotChangeException(Exception):
    
    def __init__(self, title):

        self.message = "Field {title} not has change".format(title = title)
        super().__init__(self.message)

class LiteralFormatException(Exception):
    
    def __init__(self, title):

        self.message = "The format {title} isn't valid".format(title = title)
        super().__init__(self.message)

class RepeatException(Exception):
    
    def __init__(self, title):

        self.message = "{title} name exist in db".format(title = title)
        super().__init__(self.message)

class RequiredException(Exception):
    
    def __init__(self, title):

        self.message = "The field {title} is required".format(title = title)
        super().__init__(self.message)