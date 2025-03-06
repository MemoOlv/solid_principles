class AllInOnePrinter:
    def print_document(self):
        return "Printing"
    def scan_document(self):
        return "Scanning"
    def fax_document(self):
        return "Faxing"

class Printer(AllInOnePrinter):
    def print_document(self):
        return super().print_document()
