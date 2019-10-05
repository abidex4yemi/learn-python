class GitHubApiError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code

        if self.status_code == 403:
            message = f"Rate limit reached status code {status_code}"
        else:
            message = f"Status code was {self.status_code}"

        super().__init__(message)


raise GitHubApiError(403)
