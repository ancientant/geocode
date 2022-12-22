import pytest

import bowling


class TestGroup:
    """
    given:
    when:
    then:
    """

    @pytest.fixture
    def fixture1(self):
        return 1

    def test_new_game(self):
        with pytest.raises(Exception) as e_info:
            g = Game()

        g = bowling.Game()
        assert g is not None

    def test_game_all_gutters_score(self):
        """
        given: 20 rolls
        when: all are 0
        then: score is 0
        """
        g = bowling.Game()

        # twenty rolls
        for _ in range(20):
            g.roll(0)
        assert g.score() == 0

    def test_game_all_ones_score(self):
        """
        given: 20 rolls
        when: all are 1
        then: score is 1
        """
        g = bowling.Game()

        # twenty rolls
        for _ in range(20):
            g.roll(1)
        assert g.score() == 20


