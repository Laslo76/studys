import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_one = runner.Runner('one')
        for i in range(10):
            test_one.walk()
        self.assertEqual(test_one.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_two = runner.Runner('two')
        for i in range(10):
            test_two.run()
        self.assertEqual(test_two.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        one_challenge = runner.Runner('one')
        two_challenge = runner.Runner('two')

        for i in range(10):
            one_challenge.walk()
            two_challenge.run()
        self.assertNotEqual(one_challenge.distance, two_challenge.distance)


if __name__ == "__main__":
    unittest.main()
