import unittest


def max_number(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

class TestNumLib(unittest.TestCase):

    def test_max(self):
        numbers = [10, 25, 5, 7, 23, 170, 12, 5]
        self.assertEqual(max_number(numbers), 170)

if __name__ == '__main__':
     unittest.main()


# Assignments:
#1. Yahoo login test: write it using unittest framework
#2. one more script: write it using unitest framework
#3. Compose a message in yahoomail and send a test mail to your email id using selenium
#4. Handling checkbox
#- goto http://selenium-examples.nichethyself.com
#- click on customized tour link
#- Check the England checkbox
#*. Henceforth, in all scripts, try to use unittest framework