class DatabaseErrorException(Exception):
    def __init__(self, error: str):
        self.error = error
        self.detail = f"An error occurred while executing request: {error}"
        super().__init__(self.detail)
