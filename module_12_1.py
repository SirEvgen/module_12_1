from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('runner')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("runner2")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('runner3')
        runner2 = Runner('runner4')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertEqual(runner1.distance != runner2.distance, True)


if __name__ == '__main__':
    unittest.main()
