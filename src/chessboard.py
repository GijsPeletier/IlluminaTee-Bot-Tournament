from __future__ import annotations

from typing import Optional
from chess import Board
from torch import Tensor

from src.definitions import GameBoard


class BullyCoverMembersException(Exception):
    """
    Exception raised when cover members need to get off their ass.
    """

    def __init__(self, msg=""):
        self.msg = msg


class ChessBoard(Board, GameBoard):
    def winner(self) -> Optional[bool]:
        outcome = self.outcome()
        if outcome is None:
            return None
        return outcome.winner

    def get_state(self) -> Tensor:
        # So this is not implemented right now. It will be when the tournament is run, but
        # for both the mystery game and chess, you will not be provided the implementation
        # ahead of time.
        raise BullyCoverMembersException(
            "It is so much more fun if you implement this functionality yourself! :)"
        )
