from typing import Protocol

class PrinterProtocol(Protocol):
    def print_document(self):
        pass

class AllInOnePrinter:
    def print_document(self):
        return "Printing"
    def scan_document(self):
        return "Scanning"
    def fax_document(self):
        return "Faxing"

class Printer(PrinterProtocol):
    def print_document(self):
        return "Printing"

def do_the_print(printer: Printer):
    return printer.print_document()