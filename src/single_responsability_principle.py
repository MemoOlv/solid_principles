class Report:
    def __init__(self, report_content: str):
        self.content = report_content
    def generate(self):
        return f"Report content: {self.content}"
