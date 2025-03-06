from typing import Protocol

class PrinterProtocol(Protocol):
    def print_document(self):
        pass

class AllInOnePrinter:
    def __init__(self):
        self.printer = Printer()

    def print_document(self):
        return do_the_print(self.printer)
    def scan_document(self):
        return "Scanning"
    def fax_document(self):
        return "Faxing"

class Printer(PrinterProtocol):
    def print_document(self):
        return "Printing"

def do_the_print(printer: Printer):
    return printer.print_document()