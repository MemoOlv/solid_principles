import pathlib

from src.single_responsability_principle import Report

def test_report():
    report_content = "This is the content of the report"
    report = Report(report_content)
    obtained_report_generation = report.generate()
    expected_report_generation = "Report content: This is the content of the report"
    assert obtained_report_generation == expected_report_generation

    output_file = "tests/report.txt"
    file = pathlib.Path(output_file)

    if file.exists():
        file.unlink()

    report.save_to_file(output_file)
    assert file.exists()

    if file.exists():
        file.unlink()
