import pytest
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class TestTekoaly:
    """Tests for the basic AI class"""
    
    def test_initialization(self):
        """Test that Tekoaly initializes correctly"""
        ai = Tekoaly()
        assert ai._siirto == 0
    
    def test_move_sequence(self):
        """Test that Tekoaly returns moves in the correct sequence"""
        ai = Tekoaly()
        
        # First call returns 'k' (rock)
        assert ai.anna_siirto() == 'k'
        
        # Second call returns 'p' (paper)
        assert ai.anna_siirto() == 'p'
        
        # Third call returns 's' (scissors)
        assert ai.anna_siirto() == 's'
        
        # Fourth call returns 'k' again (cycle repeats)
        assert ai.anna_siirto() == 'k'
    
    def test_move_cycle(self):
        """Test that the move sequence cycles correctly"""
        ai = Tekoaly()
        
        # Generate 10 moves and verify the cycle
        moves = [ai.anna_siirto() for _ in range(10)]
        
        # Expected pattern: k, p, s, k, p, s, k, p, s, k
        expected = ['k', 'p', 's'] * 3 + ['k']
        assert moves == expected
    
    def test_aseta_siirto_does_nothing(self):
        """Test that aseta_siirto doesn't affect the AI behavior"""
        ai = Tekoaly()
        
        move1 = ai.anna_siirto()
        ai.aseta_siirto('s')  # Set opponent's move to scissors
        move2 = ai.anna_siirto()
        
        # AI should continue its normal sequence regardless
        assert move1 == 'k'
        assert move2 == 'p'


class TestTekoalyParannettu:
    """Tests for the advanced AI with memory"""
    
    def test_initialization(self):
        """Test that TekoalyParannettu initializes correctly"""
        ai = TekoalyParannettu(5)
        assert ai._vapaa_muisti_indeksi == 0
        assert len(ai._muisti) == 5
    
    def test_first_moves_are_rock(self):
        """Test that the first moves are always rock"""
        ai = TekoalyParannettu(10)
        
        # First move should be rock
        assert ai.anna_siirto() == 'k'
        
        # Record opponent's move
        ai.aseta_siirto('p')
        
        # Second move should still be rock (not enough memory)
        assert ai.anna_siirto() == 'k'
    
    def test_memory_recording(self):
        """Test that opponent moves are recorded in memory"""
        ai = TekoalyParannettu(10)
        
        # Generate some moves and record opponent's responses
        ai.anna_siirto()  # Get move 1
        ai.aseta_siirto('p')  # Record opponent's response
        
        ai.anna_siirto()  # Get move 2
        ai.aseta_siirto('s')  # Record opponent's response
        
        ai.anna_siirto()  # Get move 3
        
        # Memory index should be at 2 (recorded 2 moves)
        assert ai._vapaa_muisti_indeksi == 2
        assert ai._muisti[0] == 'p'
        assert ai._muisti[1] == 's'
    
    def test_memory_full_behavior(self):
        """Test that memory cycles when full"""
        ai = TekoalyParannettu(3)
        
        # Fill the memory
        ai.anna_siirto()
        ai.aseta_siirto('p')
        
        ai.anna_siirto()
        ai.aseta_siirto('s')
        
        ai.anna_siirto()
        ai.aseta_siirto('k')
        
        # At this point memory is full
        assert ai._vapaa_muisti_indeksi == 3
        
        # Now add another move - should shift memory
        ai.anna_siirto()
        ai.aseta_siirto('p')
        
        # Memory should still have size 3 and be shifted
        assert len(ai._muisti) == 3
        assert ai._vapaa_muisti_indeksi == 3
    
    def test_strategy_rock_pattern(self):
        """Test that AI counters rock with paper"""
        ai = TekoalyParannettu(10)
        
        # Get first move
        ai.anna_siirto()
        
        # Record that opponent played rock repeatedly
        ai.aseta_siirto('k')
        ai.anna_siirto()
        
        ai.aseta_siirto('k')
        ai.anna_siirto()
        
        ai.aseta_siirto('k')
        ai.anna_siirto()
        
        ai.aseta_siirto('k')
        
        # AI should now counter with paper
        move = ai.anna_siirto()
        assert move == 'p'
    
    def test_strategy_paper_pattern(self):
        """Test that AI counters paper with scissors"""
        ai = TekoalyParannettu(10)
        
        # Get first move
        ai.anna_siirto()
        
        # Record that opponent played paper repeatedly
        ai.aseta_siirto('p')
        ai.anna_siirto()
        
        ai.aseta_siirto('p')
        ai.anna_siirto()
        
        ai.aseta_siirto('p')
        ai.anna_siirto()
        
        ai.aseta_siirto('p')
        
        # AI should now counter with scissors
        move = ai.anna_siirto()
        assert move == 's'
    
    def test_strategy_scissors_pattern(self):
        """Test that AI counters scissors with rock"""
        ai = TekoalyParannettu(10)
        
        # Get first move
        ai.anna_siirto()
        
        # Record that opponent played scissors repeatedly
        ai.aseta_siirto('s')
        ai.anna_siirto()
        
        ai.aseta_siirto('s')
        ai.anna_siirto()
        
        ai.aseta_siirto('s')
        ai.anna_siirto()
        
        ai.aseta_siirto('s')
        
        # AI should now counter with rock
        move = ai.anna_siirto()
        assert move == 'k'
    
    def test_default_to_rock_on_tie(self):
        """Test that AI defaults to rock when strategies are tied"""
        ai = TekoalyParannettu(10)
        
        # Get first move
        ai.anna_siirto()
        
        # Record mixed opponent moves
        ai.aseta_siirto('k')
        ai.anna_siirto()
        
        ai.aseta_siirto('p')
        ai.anna_siirto()
        
        ai.aseta_siirto('k')
        ai.anna_siirto()
        
        ai.aseta_siirto('p')
        
        # Should default to rock (all strategies equal)
        move = ai.anna_siirto()
        assert move == 'k'


class TestTekoalyIntegration:
    """Integration tests for AI classes"""
    
    def test_basic_vs_advanced_difference(self):
        """Test that advanced AI and basic AI behave differently"""
        basic_ai = Tekoaly()
        advanced_ai = TekoalyParannettu(10)
        
        # Get initial moves
        basic_move = basic_ai.anna_siirto()
        advanced_move = advanced_ai.anna_siirto()
        
        # Both should start with rock
        assert basic_move == 'k'
        assert advanced_move == 'k'
        
        # Simulate gameplay
        basic_ai.aseta_siirto('p')  # Ignored
        advanced_ai.aseta_siirto('p')  # Remembered
        
        # Get next moves
        basic_next = basic_ai.anna_siirto()
        advanced_next = advanced_ai.anna_siirto()
        
        # Basic AI follows sequence, advanced is still learning
        assert basic_next == 'p'
        assert advanced_next == 'k'  # Not enough data yet
