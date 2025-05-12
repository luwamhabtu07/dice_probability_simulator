import unittest
from dice_simulator import roll_dice_once, simulate_rolls, calculate_distribution

class TestDiceSimulator(unittest.TestCase):

    def test_roll_once_normal(self):
        result = roll_dice_once(2, 6)
        self.assertTrue(2 <= result <= 12)

    def test_simulate_rolls_length(self):
        results = simulate_rolls(2, 6, 100)
        self.assertEqual(len(results), 100)

    def test_edge_zero_dice(self):
        result = roll_dice_once(0, 6)
        self.assertEqual(result, 0)

    def test_distribution_total_probability(self):
        results = simulate_rolls(1, 2, 1000)
        dist = calculate_distribution(results, 1000)
        total_prob = sum(dist.values())
        self.assertAlmostEqual(total_prob, 1.0, places=1)

if __name__ == '__main__':
    unittest.main()
