class InvalidFormat(BaseException):
    def __str__(self) -> str:
        return "Invalid commit message format"