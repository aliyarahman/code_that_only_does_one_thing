# This is the basic structure of a Python unittest testing file


# Section 0: Import modules
import unittest

# Section 1: The functionality/thing/code you want to test
# Note that if you have a separate tests.py file, you have
# to somehow point to the code you want to test rather than
# writing it here.
def sum_three(x):
	return x+3


# Section 2: The tests
# Section 2.a: Test sum three
class SumThree(unittest.TestCase):
# Test 2.a.1: Test to see if function correctly adds three and returns total
	def test(self):
		self.assertEqual(sum_three(3),6)


# Section 3: The line that runs the code
# Not everyone builds this right into the testing file, but since we aren't
# doing any CI and instead just running from the command line, we'll 
# do this for now.
if __name__ == '__main__':
	unittest.main()