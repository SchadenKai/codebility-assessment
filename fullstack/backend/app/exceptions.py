class InternalServerException(Exception):
    def __init__(
        self,
        message: str = "Something went wrong",
        exception_message: Exception | None = None,
    ):
        self.message = f"{message}: {exception_message}"
        super.__init__(self.message)
