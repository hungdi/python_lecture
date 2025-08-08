class ImageLoadError(Exception):
    def __init__(self, number, message="이미지 로드 실패"):
        self.number = number
        super().__init__(message)

    def is_critical(self):
        if self.number > 100:
            return True
        return False


