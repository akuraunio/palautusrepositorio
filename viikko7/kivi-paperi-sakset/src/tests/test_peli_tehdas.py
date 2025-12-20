import pytest
from peli_tehdas import luo_peli
from kps_peli import KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly


class TestPeliTehdas:
    """Tests for the game factory"""
    
    def test_create_player_vs_player_game(self):
        """Test creating a player vs player game"""
        game = luo_peli('a')
        assert game is not None
        assert isinstance(game, KPSPelaajaVsPelaaja)
    
    def test_create_player_vs_ai_game(self):
        """Test creating a player vs AI game"""
        game = luo_peli('b')
        assert game is not None
        assert isinstance(game, KPSTekoaly)
    
    def test_create_player_vs_advanced_ai_game(self):
        """Test creating a player vs advanced AI game"""
        game = luo_peli('c')
        assert game is not None
        assert isinstance(game, KPSParempiTekoaly)
    
    def test_create_game_invalid_mode(self):
        """Test creating a game with invalid mode"""
        game = luo_peli('invalid')
        assert game is None
    
    def test_create_game_empty_mode(self):
        """Test creating a game with empty mode"""
        game = luo_peli('')
        assert game is None
    
    def test_create_game_none_mode(self):
        """Test creating a game with None mode"""
        game = luo_peli(None)
        assert game is None


class TestKPSPelaajaVsPelaaja:
    """Tests for player vs player game"""
    
    def test_game_instance_creation(self):
        """Test that game instance is created correctly"""
        game = KPSPelaajaVsPelaaja()
        assert game is not None
    
    def test_move_validation_method_exists(self):
        """Test that move validation method exists"""
        game = KPSPelaajaVsPelaaja()
        assert hasattr(game, '_onko_ok_siirto')
        assert callable(game._onko_ok_siirto)


class TestKPSTekoaly:
    """Tests for player vs AI game"""
    
    def test_game_instance_creation(self):
        """Test that game instance is created correctly"""
        game = KPSTekoaly()
        assert game is not None
    
    def test_tekoaly_initialized(self):
        """Test that Tekoaly is initialized"""
        game = KPSTekoaly()
        assert hasattr(game, 'tekoaly')
        assert game.tekoaly is not None
    
    def test_game_has_required_methods(self):
        """Test that game has required methods"""
        game = KPSTekoaly()
        assert hasattr(game, '_tokan_siirto')
        assert callable(game._tokan_siirto)
        assert hasattr(game, '_onko_ok_siirto')
        assert callable(game._onko_ok_siirto)


class TestKPSParempiTekoaly:
    """Tests for player vs advanced AI game"""
    
    def test_game_instance_creation(self):
        """Test that game instance is created correctly"""
        game = KPSParempiTekoaly()
        assert game is not None
    
    def test_parannettu_tekoaly_initialized(self):
        """Test that TekoalyParannettu is initialized"""
        game = KPSParempiTekoaly()
        assert hasattr(game, 'tekoaly')
        assert game.tekoaly is not None
    
    def test_game_has_required_methods(self):
        """Test that game has required methods"""
        game = KPSParempiTekoaly()
        assert hasattr(game, '_tokan_siirto')
        assert callable(game._tokan_siirto)
        assert hasattr(game, '_onko_ok_siirto')
        assert callable(game._onko_ok_siirto)


class TestGameIntegration:
    """Integration tests for game creation and validation"""
    
    def test_all_valid_modes_create_games(self):
        """Test that all valid modes create game instances"""
        modes = ['a', 'b', 'c']
        for mode in modes:
            game = luo_peli(mode)
            assert game is not None, f"Mode {mode} should create a game"
    
    def test_invalid_modes_return_none(self):
        """Test that invalid modes return None"""
        invalid_modes = ['d', 'x', '1', 'abc']
        for mode in invalid_modes:
            game = luo_peli(mode)
            assert game is None, f"Mode {mode} should return None"
