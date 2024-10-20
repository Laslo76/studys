import unittest
# RunnerTest
import module_12_1 as RunTest
# TournamentTest
import module_12_2 as TourTest

total_test = unittest.TestSuite()
total_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunTest.RunnerTest))
total_test.addTest(unittest.TestLoader().loadTestsFromTestCase(TourTest.TournamentTest))


test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(total_test)
