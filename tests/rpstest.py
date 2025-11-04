import pytest
from nimbuscasino import rps 
from unittest.mock import patch


class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #
    @pytest.fixture
        def example_fixture(self):
        
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """
        # Store the active patches to clean them up later
        self.active_patches = []
        
        def mock_random_choice(option):
            """
            A mock function to replace random.choice for testing purposes.
            Always returns the specified option for predictable outcomes.
            """
            # Patch random.choice in the nimbuscasino.rps module specifically
            patcher = patch("nimbuscasino.rps.random.choice")
            mock_choice = patcher.start()
            mock_choice.return_value = option
            self.active_patches.append(patcher)
            return mock_choice
        
        self.mock_random_choice = mock_random_choice
    
        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at the yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed
        # Clean up all active patches
        for patcher in self.active_patches:
            patcher.stop()

    #
    # Test functions
    #


        def test_tie_check(self, example_fixture):
            """
            Test debugging... making sure that we can run a simple test that always passes.
            Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
            From the main project directory, run the `python3 -m pytest` command to run all tests.
            """
            
            self.mock_random_choice('scissors')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('scissors')
            assert winorlose == "tie"
            assert bet == 0
            self.mock_random_choice('paper')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('paper')
            assert winorlose == "tie"
            assert bet == 0
            self.mock_random_choice('rock')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('rock')
            assert winorlose == "tie"
            assert bet == 0

        def test_win_check(self, example_fixture):
            """
            Test debugging... making sure that we can run a simple test that always passes.
            Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
            From the main project directory, run the `python3 -m pytest` command to run all tests.
            """
            self.mock_random_choice('scissors')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('rock')
            assert winorlose == "win"
            assert bet == 1
            self.mock_random_choice('rock')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('paper')
            assert winorlose == "win"
            assert bet == 1
            self.mock_random_choice('paper')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('scissors')
            assert winorlose == "win"
            assert bet == 1

        def test_lose_check(self, example_fixture):
            """
            Test debugging... making sure that we can run a simple test that always passes.
            Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
            From the main project directory, run the `python3 -m pytest` command to run all tests.
            """
            self.mock_random_choice('scissors')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('paper')
            assert winorlose == "lose"
            assert bet == -1
            self.mock_random_choice('rock')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('scissors')
            assert winorlose == "lose"
            assert bet == -1
            self.mock_random_choice('paper')  # use the fixture to mock random.choice
            winorlose, bet = rps.rps('rock')
            assert winorlose == "lose"
            assert bet == -1

    def test_invalid_choice(self, example_fixture):
            """
            Test that an invalid choice raises a ValueError.
            """
            with pytest.raises(ValueError):
                rps.rps('invalid_choice')    