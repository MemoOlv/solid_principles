from src.interface_segregation_principle import (
    AllInOnePrinter,
    Printer,
    do_the_print,
    Scaner,
    do_the_scan,
    Faxer,
    do_the_fax,
)


def test_do_everything():
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


def test_just_print():
    printer = Printer()
    obtained_print = do_the_print(printer)
    expected_print = "Printing"
    assert obtained_print == expected_print


def test_just_scan():
    scanner = Scaner()
    obtained_scanner = do_the_scan(scanner)
    expected_scanner = "Scanning"
    assert obtained_scanner == expected_scanner


def test_just_fac():
    faxer = Faxer()
    obtained_faxer = do_the_fax(faxer)
    expected_faxer = "Faxing"
    assert obtained_faxer == expected_faxer
