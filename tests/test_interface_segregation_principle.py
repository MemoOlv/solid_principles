from src.interface_segregation_principle import AllInOnePrinter

def test_do_everithing():
    all_printer = AllInOnePrinter()
    obtained_print = all_printer.print_document()
    expected_print = "Printing"
    assert obtained_print == expected_print

    obtained_scan = all_printer.scan_document()
    expected_scan = "Scanning"
    assert obtained_scan == expected_scan

    obtained_fax = all_printer.fax_document()
    expected_fax = "Faxing"
    assert obtained_fax == expected_fax
