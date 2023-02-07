import datetime
import unittest

def NextDate(date_string):
    date = datetime.datetime.strptime(date_string, '%d/%m/%Y')
    date += datetime.timedelta(days=1)
    return date.strftime('%d/%m/%Y')

class TestNextDate(unittest.TestCase):
    def test_normaldate(self):
        self.assertEqual(NextDate("01/01/2023"), "02/01/2023")
    def test_lastdayofmonth(self):
        self.assertEqual(NextDate("28/02/2002"), "01/03/2002")
    def test_lastdayofyear(self):
        self.assertEqual(NextDate("31/12/2020"), "01/01/2021")

suite = unittest.TestLoader().loadTestsFromTestCase(TestNextDate)
unittest.TextTestRunner(verbosity=2).run(suite)