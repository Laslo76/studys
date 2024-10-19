import unittest
import runner


class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = []

    def setUp(self):
        self.runner_one = runner.Runner('Усэйн', 10)
        self.runner_two = runner.Runner('Андрей', 9)
        self.runner_thr = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tour in TournamentTest.all_results:
            print(tour)
            for place, runner in tour.items():
                print(f'{place}: {runner}', end=',')
            print()

    def test_tournament(self):
        runners_list = [self.runner_one, self.runner_thr]
        tour1 = runner.Tournament(90, *runners_list)
        TournamentTest.all_results.append(tour1.start())
        for current_runner in runners_list:
            self.assertEqual(current_runner.distance, 0)

        runners_list = [self.runner_two, self.runner_thr]
        tour2 = runner.Tournament(90, *runners_list)
        TournamentTest.all_results.append(tour2.start())
        for current_runner in runners_list:
            self.assertEqual(current_runner.distance, 0)

        runners_list = [self.runner_one, self.runner_two, self.runner_thr]
        tour3 = runner.Tournament(90, *runners_list)
        TournamentTest.all_results.append(tour3.start())
        for current_runner in runners_list:
            self.assertEqual(current_runner.distance, 0)


if __name__ == "__main__":
    unittest.main()
