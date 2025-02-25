import pathlib


class Report:
    def __init__(self, report_content: str):
        self.content = report_content
    def generate(self):
        return f"Report content: {self.content}"

class ReportSaver:
    def __init__(self, report: Report):
        self.report: Report = report
    def save_to_file(self, filename):
        self.file = pathlib.Path(filename)
        self.file.write_text(self.report.content)