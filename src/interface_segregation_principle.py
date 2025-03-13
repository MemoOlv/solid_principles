from typing import Protocol


class PrinterProtocol(Protocol):
    def print_document(self):
        pass


class ScannerProtocol(Protocol):
    def scan_document(self):
        pass

class FaxerProtocol(Protocol):
    def fax_document(self):
        pass


class AllInOnePrinter:
    def __init__(self):
        self.printer = Printer()
        self.scanner = Scaner()
        self.faxer = Faxer()

    def print_document(self):
        return do_the_print(self.printer)

    def scan_document(self):
        return do_the_scan(self.scanner)

    def fax_document(self):
        return do_the_fax(self.faxer)


class Printer(PrinterProtocol):
    def print_document(self):
        return "Printing"


class Scaner(PrinterProtocol):
    def scan_document(self):
        return "Scanning"


class Faxer(PrinterProtocol):
    def fax_document(self):
        return "Faxing"


def do_the_print(printer: Printer):
    return printer.print_document()


def do_the_scan(scanner: Scaner):
    return scanner.scan_document()

def do_the_fax(faxer: Faxer):
    return faxer.fax_document()
