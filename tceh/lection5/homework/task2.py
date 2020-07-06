class Printer(object):
    def __init__(self, values=[]):
        self.values = values

    def log(self, *values):
        self.values = values

        if self.values:
            for item in self.values:
                print(item)
        else:
            print('There are no values to print')


class FormattedPrinter(Printer):
    def log(self, *values):
        print('*' * 10)
        super().log(*values)
        print('*' * 10)


a = FormattedPrinter()
a.log(1, 2, 3, 4, 5)
