"""CSC148 Assignment 1

CSC148 Winter 2025
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jonathan Calver, Diane Horton, Sophia Huynh,
        Sadia Sharmin, & Marina Tawfik

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Sadia Sharmin,
              Marina Tawfik, Ian Berlot-Attwell, Pan Chen, & Saba Sadatamin

Module Description:

This module contains all classes necessary for a1_game.py to run.

Note: We will run pyTA on this file when grading your assignment for the final submission.
      We will not be running pyTA on this file for the initial early submission deadline.

"""

from __future__ import annotations

from random import shuffle

from a1_pyta_config import pyta_config, python_ta, check_contracts

# Each raccoon moves every this many turns
RACCOON_TURN_FREQUENCY = 20

# Directions dx, dy
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]


def get_shuffled_directions() -> list[tuple[int, int]]:
    """
    Provided helper that returns a shuffled copy of DIRECTIONS.
    You should use this where appropriate in your code.
    """
    to_return = DIRECTIONS[:]
    shuffle(to_return)
    return to_return


def neighbours(x: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Return the four coordinates adjacent to x.

    Note: this function does NOT do any checking for whether the
          four adjacent coordinates are actually on a board or not though,
          so the client of this function would need to confirm that for themselves.

    This function may be used whenever you find it helpful.
    For example, you may find it helpful when
    implementing GameBoard.adjacent_bin_score.

    >>> ns = set(neighbours((2, 3)))
    >>> {(2, 2), (2, 4), (1, 3), (3, 3)} == ns
    True
    """
    rslt = []
    for direction in DIRECTIONS:
        rslt.append((x[0] + direction[0], x[1] + direction[1]))
    return rslt


@check_contracts
class GameBoard:
    """A game board on which the game is played.

    Public Attributes:
    - ended: whether this game has ended or not
    - turns: how many turns have passed in the game
    - width: how many squares wide this board is
    - height: how many squares high this board is

    Private Attributes:
    - _player: the player of the game.
    - _raccoons: a list of all raccoons on the board.
    - _board: a list of lists where each inner list is a row of the gameboard
    and each inner list is a list of lists where each inner list represents a
    square and contains the characters on that square.

    Representation Invariants:
    - self.turns >= 0
    - self.width > 0
    - self.height > 0
    - self.ended is True if and only if the game has ended
    - No tile in the game contains more than 1 character, except that a tile
      may contain both a Raccoon and an open GarbageCan.
    - At most one Player can be on the board; self._player is None if there is
      no Player on the board.


    Sample Usage:
    See examples in individual method docstrings.
    """

    ended: bool
    turns: int
    width: int
    height: int
    _player: Player | None
    _raccoons: list[Raccoon]
    _board: list[list[list[Character]]]

    def __init__(self, w: int, h: int) -> None:
        """Initialize this Board to be of the given width <w> and height <h> in
        squares. A board is initially empty (no characters) and no turns have
        been taken.

        >>> b = GameBoard(3, 3)
        >>> b.width == 3
        True
        >>> b.height == 3
        True
        >>> b.turns == 0
        True
        >>> b.ended
        False
        """

        self.ended = False
        self.turns = 0

        self.width = w
        self.height = h

        self._player = None
        self._raccoons = []
        self._board = [[[] for i in range(w)] for j in range(h)]

    def place_character(self, c: Character) -> None:
        """Record that character <c> is on this board.

        Note: This method should only be called from Character.__init__.

        IMPORTANT:
        The decisions you made about new private attributes for class GameBoard
        will determine what you do here.

        Preconditions:
        - c.board == self
        - self.on_board(c.x, c.y)
        - If <c> is a Player, then there must not be any other players on this
        board yet.
        - Character <c> has not already been placed on this board.
        - The tile (c.x, c.y) does not already contain a character, with the
        exception being that a raccoon can be placed on the same tile where
        an unlocked GarbageCan is already present.

        Note: The testing will depend on this method to set up the board,
        as the Character.__init__ method calls this method.

        >>> b = GameBoard(3, 2)
        >>> r = Raccoon(b, 1, 1)  # when a Raccoon is created, it is placed on b
        >>> b.at(1, 1)[0] == r  # requires GameBoard.at be implemented to work
        True
        """
        self._board[c.y][c.x].append(c)
        if isinstance(c, Player):
            self._player = c
        if isinstance(c, Raccoon):
            self._raccoons.append(c)

    def update_pos(self, x: int, y: int, c: Character) -> None:
        """Update the position of Character <c> on the gameboard to
        tile (x,y).

        Preconditions:
        - c.board == self
        - c in self.at(c.x, c.y)
        - The tile (x, y) is empty or c is a Raccoon and the tile contains an
        unlocked and unoccupied GarbageCan.

        >>> b = GameBoard(3, 2)
        >>> r = RecyclingBin(b, 1, 1)
        >>> b.update_pos(2, 1, r)
        >>> b.at(1, 1) == []
        True
        >>> b.at(2, 1)[0] == r
        True
        """
        if len(self._board[c.y][c.x]) == 1 and self._board[c.y][c.x][0] == c:
            self._board[c.y][c.x].remove(c)
            self._board[y][x].append(c)

    def at(self, x: int, y: int) -> list[Character]:
        """Return the characters at tile (x, y).

        If there are no characters or if the (x, y) coordinates are not
        on the board, return an empty list.

        Note: There may be as many as two characters at one tile,
        since a raccoon can climb into a garbage can.

        Note: The testing will depend on this method to allow us to
        access the Characters on your board, since we don't know how
        you have chosen to store them in your private attributes,
        so make sure this method is working properly!

        >>> b = GameBoard(3, 2)
        >>> r = Raccoon(b, 1, 1)
        >>> b.at(1, 1)[0] == r
        True
        >>> p = Player(b, 0, 1)
        >>> b.at(0, 1)[0] == p
        True
        """
        x = self._board[y][x][:]
        return x

    def to_grid(self) -> list[list[str]]:
        """
        Return the game state as a list of lists of letters where:

        'R' = Raccoon
        'S' = SmartRaccoon
        'P' = Player
        'C' = closed GarbageCan
        'O' = open GarbageCan
        'B' = RecyclingBin
        '@' = Raccoon in GarbageCan
        '-' = Empty tile

        Each inner list represents one row of the game board.

        >>> b = GameBoard(3, 2)
        >>> _ = Player(b, 0, 0)
        >>> _ = Raccoon(b, 1, 1)
        >>> _ = GarbageCan(b, 2, 1, True)
        >>> b.to_grid()
        [['P', '-', '-'], ['-', 'R', 'C']]
        """
        new_list = []
        for row in self._board:
            row_list = []
            for tile in row:
                if not tile:
                    row_list.append('-')
                elif len(tile) == 2:
                    row_list.append('@')
                else:
                    row_list.append(tile[0].get_symbol())
            new_list.append(row_list)
        return new_list

    def __str__(self) -> str:
        """
        Return a string representation of this board.

        The format is the same as expected by the setup_from_grid method.

        >>> b = GameBoard(3, 2)
        >>> _ = Raccoon(b, 1, 1)
        >>> print(b)
        ---
        -R-
        >>> _ = Player(b, 0, 0)
        >>> _ = GarbageCan(b, 2, 1, False)
        >>> print(b)
        P--
        -RO
        >>> str(b)
        'P--\\n-RO'
        """
        s = ''
        lst = self.to_grid()
        for row in lst:
            for tile in row:
                s = s + tile
            s = s + '\n'
        return s.rstrip()

    def setup_from_grid(self, grid: str) -> None:
        """
        Set the state of this GameBoard to correspond to the string <grid>,
        which represents a game board using the following symbols:

        'R' = Raccoon not in a GarbageCan
        'P' = Player
        'C' = closed GarbageCan
        'O' = open GarbageCan
        'B' = RecyclingBin
        '@' = Raccoon in GarbageCan
        '-' = Empty tile

        Note: There is a newline character between each board row.
              This character appears as '\\nn' in the doctest example below.

              Visually, the board is as shown below.
              P-B-
              -BRB
              --BB
              -C--

        >>> b = GameBoard(4, 4)
        >>> b.setup_from_grid('P-B-\\n-BRB\\n--BB\\n-C--')
        >>> str(b)
        'P-B-\\n-BRB\\n--BB\\n-C--'
        >>> print(b)
        P-B-
        -BRB
        --BB
        -C--
        """
        lines = grid.split('\n')
        width = len(lines[0])
        height = len(lines)
        self.__init__(width, height)  # reset the board to an empty board
        y = 0
        for line in lines:
            x = 0
            for char in line:
                if char == 'R':
                    Raccoon(self, x, y)
                elif char == 'S':
                    SmartRaccoon(self, x, y)
                elif char == 'P':
                    Player(self, x, y)
                elif char == 'O':
                    GarbageCan(self, x, y, False)
                elif char == 'C':
                    GarbageCan(self, x, y, True)
                elif char == 'B':
                    RecyclingBin(self, x, y)
                elif char == '@':
                    GarbageCan(self, x, y, False)
                    Raccoon(self, x, y)  # Note: assumes not a SmartRaccoon.
                    # Note: the order mattered above, as we have to place the
                    # GarbageCan before the Raccoon!
                    # (see the place_character method precondition)
                x += 1
            y += 1

    # a helper method you may find useful in places
    def on_board(self, x: int, y: int) -> bool:
        """Return True iff the position x, y is within the boundaries of this
        board (based on its width and height), and False otherwise.
        """
        return 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1

    def give_turns(self) -> None:
        """Give every turn-taking character one turn in the game.

        The Player should take their turn first and the number of turns
        should be incremented by one. Then each other TurnTaker
        should be given a turn if RACCOON_TURN_FREQUENCY turns have occurred
        since the last time the TurnTakers were given their turn.

        After all turns are taken, check_game_ended should be called to
        determine if the game is over.

        Precondition:
        self._player is not None

        >>> b = GameBoard(4, 3)
        >>> p = Player(b, 0, 0)
        >>> r = Raccoon(b, 1, 1)
        >>> b.turns
        0
        >>> for _ in range(RACCOON_TURN_FREQUENCY - 1):
        ...     b.give_turns()
        >>> b.turns == RACCOON_TURN_FREQUENCY - 1  # confirm b.turns is correct
        True
        >>> (r.x, r.y) == (1, 1)  # Raccoon hasn't had a turn yet
        True
        >>> (p.x, p.y) == (0, 0)  # Player hasn't had any inputs
        True
        >>> p.record_event(RIGHT)
        >>> b.give_turns()
        >>> (r.x, r.y) != (1, 1)  # Raccoon has had a turn, so must have moved!
        True
        >>> (p.x, p.y) == (1, 0)  # Player moved right!
        True
        """
        self._player.take_turn()
        self.turns += 1  # PROVIDED, DO NOT CHANGE

        if self.turns % RACCOON_TURN_FREQUENCY == 0:  # PROVIDED, DO NOT CHANGE
            for raccoon in self._raccoons:
                raccoon.take_turn()

        self.check_game_ended()  # PROVIDED, DO NOT CHANGE

    def handle_event(self, event: tuple[int, int]) -> None:
        """Handle a user-input event.

        The board's Player records the event that happened, so that when the
        Player gets a turn, it can make the move that the user input indicated.

        Preconditions:
        - event in DIRECTIONS
        """
        self._player.record_event(event)

    def check_game_ended(self) -> int | None:
        """Check if this game has ended. A game ends when all the raccoons on
        this game board are either inside a can or trapped.

        If the game has ended:
        - update the ended attribute to be True
        - Return the score, where the score is given by:
            (number of raccoons trapped) * 10 + the adjacent_bin_score
            - Note: Any raccoons inside a garbage can do not contribute
            to the above score

        If the game has not ended:
        - update the ended attribute to be False
        - return None

        >>> b = GameBoard(3, 2)
        >>> _ = Raccoon(b, 1, 0)
        >>> _ = Player(b, 0, 0)
        >>> _ = RecyclingBin(b, 1, 1)
        >>> b.check_game_ended() is None
        True
        >>> b.ended
        False
        >>> _ = RecyclingBin(b, 2, 0)
        >>> b.check_game_ended()
        11
        >>> b.ended
        True
        """
        ended = []
        trapped = []
        for raccoon in self._raccoons:
            if raccoon.check_trapped():
                ended.append(True)
                trapped.append(raccoon)
            elif raccoon.inside_can:
                ended.append(True)
            else:
                ended.append(False)
        if False not in ended and len(self._raccoons) > 0:
            self.ended = True
            score = (len(trapped) * 10) + self.adjacent_bin_score()
            return score
        return None

    def adjacent_bin_score(self) -> int:
        """
        Return the size of the largest cluster of adjacent recycling bins
        on this board.

        Two recycling bins are adjacent when they are directly beside each other
        in one of the four directions (up, down, left, right).

        >>> b = GameBoard(3, 3)
        >>> _ = RecyclingBin(b, 1, 1)
        >>> _ = RecyclingBin(b, 0, 0)
        >>> _ = RecyclingBin(b, 2, 2)
        >>> print(b)
        B--
        -B-
        --B
        >>> b.adjacent_bin_score()
        1
        >>> _ = RecyclingBin(b, 2, 1)
        >>> print(b)
        B--
        -BB
        --B
        >>> b.adjacent_bin_score()
        3
        >>> _ = RecyclingBin(b, 0, 1)
        >>> print(b)
        B--
        BBB
        --B
        >>> b.adjacent_bin_score()
        5
        """
        checked = []
        size = []
        for i in range(self.height):
            for j in range(self.width):
                coord = (j, i)
                if coord not in checked:
                    n = self._cluster_size(coord, checked)
                    size.append(n)
        return max(size)

    def _cluster_size(self, c: tuple[int, int], x: list[tuple[int, int]]) -> int:
        """Find the size of the cluster of RecyclingBins containing the tile
        <c>. Update <x> with all the tiles checked to find the cluster size.

        >>> b = GameBoard(3, 3)
        >>> _ = RecyclingBin(b, 0, 0)
        >>> _ = RecyclingBin(b, 0, 2)
        >>> _ = RecyclingBin(b, 1, 2)
        >>> _ = RecyclingBin(b, 2, 2)
        >>> _ = RecyclingBin(b, 2, 1)
        >>> lst = []
        >>> b._cluster_size((2, 2), lst)
        4
        >>> coords = [(2, 2), (1, 2), (0, 2), (2, 1), (0, 1), (1, 1), (2, 0)]
        >>> set(lst) == set(coords)
        True
        >>> len(lst) == len(coords)
        True
        """
        if not self.on_board(c[0], c[1]):
            return 0
        if c in x:
            return 0
        x.append(c)
        count = 0
        t = self.at(c[0], c[1])
        if len(t) == 1 and isinstance(t[0], RecyclingBin):
            count += 1
            for tile in neighbours(c):
                if self.on_board(tile[0], tile[1]):
                    count += self._cluster_size(tile, x)
        return count


@check_contracts
class Character:
    """A character that has (x,y) coordinates and is associated with a given
    board.

    This class is abstract and should not be directly instantiated.

    NOTE: To reduce the amount of documentation in subclasses, we have chosen
    not to repeat information about the public attributes in each subclass.
    Remember that the attributes are not inherited, but only exist once we call
    the __init__ of the parent class.

    Attributes:
    - board: the game board that this Character is on
    - x: the x-coordinate of this Character on the board
    - y: the y-coordinate of this Character on the board

    Representation Invariants:
    - self.board.on_board(x, y)
    - self is on self.board
    """
    board: GameBoard
    x: int
    y: int

    def __init__(self, board: GameBoard, x: int, y: int) -> None:
        """Initialize this Character on the given <board>, and
        at tile (<x>, <y>).

        When a Character is initialized, it is placed on <board>
        by calling the board's place_character method.

        Preconditions:
        - board.on_board(x, y)
        - If self is a Player, then there must not be any other players on <board> yet.
        - The tile (x, y) of <board> does not already contain a character, with the
        exception being that a raccoon can be placed on the same tile where
        an empty, unlocked GarbageCan is already present.
        """
        self.board = board
        self.x, self.y = x, y
        self.board.place_character(self)  # this associates self with the board!

    def move(self, direction: tuple[int, int]) -> bool:
        """
        If possible, move this character to the tile:

        (self.x + direction[0], self.y + direction[1]).

        Note: Each child class defines its own version of what is possible.

        Return True if the move was successful and False otherwise.
        """
        raise NotImplementedError

    def get_symbol(self) -> str:
        """
        Return a single letter representing this Character.
        """
        raise NotImplementedError


@check_contracts
class TurnTaker(Character):
    """
    A Character that can take a turn in the game.

    This class is abstract and should not be directly instantiated.
    """

    def take_turn(self) -> None:
        """
        Take a turn in the game. This method must be implemented in any subclass.
        """
        raise NotImplementedError


@check_contracts
class RecyclingBin(Character):
    """A recycling bin in the game.

    === Sample Usage ===
    >>> rb = RecyclingBin(GameBoard(4, 4), 2, 1)
    >>> rb.x, rb.y
    (2, 1)
    """

    def move(self, direction: tuple[int, int]) -> bool:
        """Move this recycling bin to tile:
                (self.x + direction[0], self.y + direction[1])
        if possible and return whether this move was successful.

        If the new tile is occupied by another RecyclingBin, push
        that RecyclingBin one tile away in the same direction and take
        its tile (as described in the Assignment 1 handout).

        If the new tile is occupied by any other Character or if it
        is beyond the boundaries of the board, do nothing and return False.

        Preconditions:
        - direction in DIRECTIONS

        >>> b = GameBoard(4, 2)
        >>> rb = RecyclingBin(b, 0, 0)
        >>> rb.move(UP)
        False
        >>> rb.move(DOWN)
        True
        >>> b.at(0, 1) == [rb]
        True
        """
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]
        if self.board.on_board(new_x, new_y):
            tile = self.board.at(new_x, new_y)
        else:
            return False
        if self.board.on_board(new_x, new_y) and not tile:
            self.board.update_pos(new_x, new_y, self)
            self.x = new_x
            self.y = new_y
            return True
        elif self.board.on_board(new_x, new_y) and tile[0].get_symbol() == 'B':
            m = tile[0].move(direction)
            if m:
                self.board.update_pos(new_x, new_y, self)
                self.x = new_x
                self.y = new_y
                return True
            return False
        else:
            return False

    def get_symbol(self) -> str:
        """
        Return the character 'B' representing a RecyclingBin.
        """
        return 'B'


@check_contracts
class Player(TurnTaker):
    """The Player of this game.

    Attributes:
    - _last_event: The direction corresponding to the last keypress event that
    the user made, or None if there is currently no keypress event to process.

    Sample Usage:
    >>> b = GameBoard(3, 1)
    >>> p = Player(b, 0, 0)
    >>> p.record_event(RIGHT)
    >>> p.take_turn()
    >>> (p.x, p.y) == (1, 0)
    True
    >>> g = GarbageCan(b, 0, 0, False)
    >>> p.move(LEFT)
    True
    >>> g.locked
    True
    """

    _last_event: tuple[int, int] | None

    def __init__(self, b: GameBoard, x: int, y: int) -> None:
        """Initialize this Player with board <b>,
        and at tile (<x>, <y>).

        Preconditions:
        - the parameters are consistent with the preconditions of Character.__init__
        """

        TurnTaker.__init__(self, b, x, y)
        self._last_event = None

    def record_event(self, direction: tuple[int, int]) -> None:
        """Record that <direction> is the last direction that the user
        has specified for this Player to move. Next time take_turn is called,
        this direction will be used.
        Preconditions:
        - direction in DIRECTIONS
        """
        self._last_event = direction

    def take_turn(self) -> None:
        """Take a turn in the game.

        For a Player, this means responding to the last user input recorded
        by a call to record_event.
        """
        if self._last_event is not None:
            self.move(self._last_event)
            self._last_event = None

    def move(self, direction: tuple[int, int]) -> bool:
        """Attempt to move this Player to the tile:
                (self.x + direction[0], self.y + direction[1])
        if possible and return True if the move is successful.

        If the new tile is occupied by a Racooon, a locked GarbageCan, or if it
        is beyond the boundaries of the board, do nothing and return False.

        If the new tile is occupied by a movable RecyclingBin, the player moves
        the RecyclingBin and moves to the new tile.

        If the new tile is unoccupied, the player moves to that tile.

        If a Player attempts to move towards an empty, unlocked GarbageCan, the
        GarbageCan becomes locked. The player's position remains unchanged in
        this case. Also return True in this case, as the Player has performed
        the action of locking the GarbageCan.

        Preconditions:
        - direction in DIRECTIONS

        >>> b = GameBoard(4, 2)
        >>> p = Player(b, 0, 0)
        >>> p.move(UP)
        False
        >>> p.move(DOWN)
        True
        >>> b.at(0, 1) == [p]
        True
        >>> _ = RecyclingBin(b, 1, 1)
        >>> p.move(RIGHT)
        True
        >>> b.at(1, 1) == [p]
        True
        """
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]
        if self.board.on_board(new_x, new_y):
            tile = self.board.at(new_x, new_y)
        else:
            return False
        if self.board.on_board(new_x, new_y) and not tile:
            self.board.update_pos(new_x, new_y, self)
            self.x = new_x
            self.y = new_y
            return True
        elif self.board.on_board(new_x, new_y) and tile[0].get_symbol() == 'B':
            m = tile[0].move(direction)
            if m:
                self.board.update_pos(new_x, new_y, self)
                self.x = new_x
                self.y = new_y
                return True
            return False
        elif self.board.on_board(new_x, new_y) and len(tile) == 1 and tile[0].get_symbol() == 'O':
            tile[0].locked = True
            return True
        else:
            return False

    def get_symbol(self) -> str:
        """
        Return the character 'P' representing this Player.
        """
        return 'P'


@check_contracts
class Raccoon(TurnTaker):
    """A raccoon in the game.

    Attributes:
    - inside_can: whether this Raccoon is inside a garbage can

    Representation Invariants:
    - inside_can is True iff this Raccoon is on the same tile as an open
    GarbageCan.

    Sample Usage:
    >>> r = Raccoon(GameBoard(11, 11), 5, 10)
    >>> r.x, r.y
    (5, 10)
    >>> r.inside_can
    False
    """
    inside_can: bool

    def __init__(self, b: GameBoard, x: int, y: int) -> None:
        """Initialize this Raccoon with board <b>, and
        at tile (<x>, <y>). Initially a Raccoon is not inside a GarbageCan,
        unless it is placed directly inside an open GarbageCan.

        Preconditions:
        - the parameters are consistent with the preconditions of Character.__init__

        >>> b = GameBoard(5, 5)
        >>> r = Raccoon(b, 4, 3)
        >>> r.x == 4 and r.y == 3
        True
        >>> r.board is b
        True
        """
        TurnTaker.__init__(self, b, x, y)
        self.inside_can = False
        if len(b.at(x, y)) == 2:
            self.inside_can = True

    def check_trapped(self) -> bool:
        """Return True iff this raccoon is trapped. A trapped raccoon is
        surrounded on 4 sides (diagonals don't matter) by recycling bins, other
        raccoons (including ones in garbage cans), the player, and/or board
        edges. Said another way, a raccoon is trapped when it has nowhere it
        could move.

        Reminder: A racooon cannot move diagonally.

        >>> b = GameBoard(3, 3)
        >>> r = Raccoon(b, 2, 1)
        >>> _ = Raccoon(b, 2, 2)
        >>> _ = Player(b, 2, 0)
        >>> r.check_trapped()
        False
        >>> _ = RecyclingBin(b, 1, 1)
        >>> r.check_trapped()
        True
        """
        trap = []
        for direction in DIRECTIONS:
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]
            if self.board.on_board(new_x, new_y):
                tile = self.board.at(new_x, new_y)
                if not tile or (len(tile) == 1 and isinstance(tile[0], GarbageCan)):
                    trap.append(False)
                else:
                    trap.append(True)
        return False not in trap

    def move(self, direction: tuple[int, int]) -> bool:
        """Attempt to move this Raccoon in <direction> and return whether
        this was successful.

        If the tile one tile over in that direction is occupied by the Player,
        a RecyclingBin, or another Raccoon, OR if the tile is not within the
        boundaries of the board, do nothing and return False.

        If the tile is occupied by an unlocked GarbageCan that has no Raccoon
        in it, this Raccoon moves there, and we have two characters on one tile
        (the GarbageCan and the Raccoon). If the GarbageCan is locked, this
        Raccoon uses this turn to unlock it and return True.

        If a Raccoon is inside a GarbageCan, it will not move (note that
        this does not mean that the raccoon is necessarily 'trapped'; it just chooses not
        to move, even if there are available spots beside it). In this case, do
        nothing and return False.

        Return True if the Raccoon unlocks a GarbageCan or moves from its
        current tile.

        Preconditions:
        - direction in DIRECTIONS

        >>> b = GameBoard(4, 2)
        >>> r = Raccoon(b, 0, 0)
        >>> r.move(UP)
        False
        >>> r.move(DOWN)
        True
        >>> b.at(0, 1) == [r]
        True
        >>> g = GarbageCan(b, 1, 1, True)
        >>> r.move(RIGHT)
        True
        >>> r.x, r.y  # Raccoon didn't change its position
        (0, 1)
        >>> not g.locked  # Raccoon unlocked the garbage can!
        True
        >>> r.move(RIGHT)
        True
        >>> r.inside_can
        True
        >>> len(b.at(1, 1)) == 2  # Raccoon and GarbageCan are both at (1, 1)!
        True
        """
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]
        if self.board.on_board(new_x, new_y):
            tile = self.board.at(new_x, new_y)
        else:
            return False
        if self.board.on_board(new_x, new_y) and not tile:
            self.board.update_pos(new_x, new_y, self)
            self.x = new_x
            self.y = new_y
            return True
        elif self.board.on_board(new_x, new_y) and len(tile) == 1 and tile[0].get_symbol() == 'O':
            self.board.update_pos(new_x, new_y, self)
            self.x = new_x
            self.y = new_y
            self.inside_can = True
            return True
        elif self.board.on_board(new_x, new_y) and tile[0].get_symbol() == 'C':
            tile[0].locked = False
            return True
        else:
            return False

    def take_turn(self) -> None:
        """Take a turn in the game.

        If a Raccoon is in a GarbageCan, it happily stays where it is.

        Otherwise, it will move in one of the four directions which aren't
        blocked. If multiple directions aren't blocked, a Raccoon will move in
        one of these directions with equal probability.

        If a Raccoon can't move, then it remains at the same position.

        >>> b = GameBoard(3, 4)
        >>> r1 = Raccoon(b, 0, 0)
        >>> r1.take_turn()
        >>> (r1.x, r1.y) in [(0, 1), (1, 0)]  # will have moved to one of these.
        True
        >>> r2 = Raccoon(b, 2, 1)
        >>> _ = RecyclingBin(b, 2, 0)
        >>> _ = RecyclingBin(b, 1, 1)
        >>> _ = RecyclingBin(b, 2, 2)
        >>> r2.take_turn()  # Raccoon is trapped is won't move
        >>> r2.x, r2.y
        (2, 1)
        """
        directions = get_shuffled_directions()
        x = self.x
        y = self.y
        if not self.inside_can and not self.check_trapped():
            i = 0
        else:
            i = len(directions)
        while self in self.board.at(x, y) and i < len(directions):
            x1 = self.x + directions[i][0]
            y1 = self.y + directions[i][1]
            if self.board.on_board(x1, y1):
                tile = self.board.at(x1, y1)
                open_can = len(tile) == 1 and isinstance(tile[0], GarbageCan)
                if not tile or open_can:
                    self.move(directions[i])
                if open_can:
                    self.inside_can = True
            i += 1

    def get_symbol(self) -> str:
        """
        Return '@' to represent that this Raccoon is inside a garbage can
        or 'R' otherwise.
        """
        if self.inside_can:
            return '@'
        return 'R'


@check_contracts
class SmartRaccoon(Raccoon):
    """A smart raccoon in the game.

    Behaves like a Raccoon, but when it takes a turn, it will move towards
    a GarbageCan if it can see that GarbageCan in its line of sight.
    See the take_turn method for details.

    SmartRaccoons move in the same way as Raccoons.

    Sample Usage:
    >>> b = GameBoard(8, 1)
    >>> s = SmartRaccoon(b, 4, 0)
    >>> s.x, s.y
    (4, 0)
    >>> s.inside_can
    False
    """

    def _line_of_sight(self, direction: tuple[int, int]) -> int:
        """Return the distance from the SmartRaccoon to a non-occupied
        GarbageCan in the direction specified by <direction>. If there is no
        GarbageCan, or it is blocked by a RecyclingBin, Raccoon, or occupied
        GarbageCan, then return a distance larger than the board.

        Preconditions:
        - direction in DIRECTIONS

        >>> b = GameBoard(5, 5)
        >>> s = SmartRaccoon(b, 2, 2)
        >>> g = GarbageCan(b, 0, 2, True)
        >>> g1 = GarbageCan (b, 2, 0, False)
        >>> r = Raccoon(b, 2, 0)
        >>> rb = RecyclingBin(b, 4, 2)
        >>> p = Player(b, 2, 4)
        >>> s._line_of_sight(LEFT)
        2
        >>> s._line_of_sight(RIGHT)
        6
        >>> s._line_of_sight(UP)
        6
        >>> s._line_of_sight(DOWN)
        6
        """
        counter = 1
        x = self.x + direction[0]
        y = self.y + direction[1]
        if self.board.on_board(x, y):
            tile = self.board.at(x, y)
        else:
            return max(self.board.height + 1, self.board.width + 1)
        empty = not tile or isinstance(tile[0], Player)
        while self.board.on_board(x, y) and empty:
            counter += 1
            x += direction[0]
            y += direction[1]
            if self.board.on_board(x, y):
                tile = self.board.at(x, y)
            else:
                tile = self.board.at(self.x, self.y)
            empty = not tile or isinstance(tile[0], Player)
        if self.board.on_board(x, y) and len(tile) == 1:
            if isinstance(tile[0], GarbageCan):
                return counter
        return max(self.board.height + 1, self.board.width + 1)

    def take_turn(self) -> None:
        """Take a turn in the game.

        If a SmartRaccoon is in a GarbageCan, it stays where it is.

        A SmartRaccoon checks along the four directions for
        the closest non-occupied GarbageCan in its "line of sight".

        Note about line of sight:
        A GarbageCan is in the SmartRaccoon's line of sight if there are no other
        raccoons, RecyclingBins, or other GarbageCans between this SmartRaccoon
        and the non-occupied GarbageCan. The Player may be between this SmartRaccoon and the
        GarbageCan though, as the SmartRaccoon knows that eventually the Player
        will have to move.

        If there is a tie for the closest GarbageCan, a SmartRaccoon
        will prioritize the directions in the order indicated in DIRECTIONS.

        If there are no GarbageCans in its line of sight along one of the four
        directions, it moves exactly like a Raccoon.

        >>> b = GameBoard(8, 2)
        >>> s = SmartRaccoon(b, 4, 0)
        >>> _ = GarbageCan(b, 3, 1, False)
        >>> _ = GarbageCan(b, 0, 0, False)
        >>> _ = GarbageCan(b, 7, 0, False)
        >>> s.take_turn()
        >>> s.x == 5
        True
        >>> s.take_turn()
        >>> s.x == 6
        True
        """
        if not self.check_trapped() or not self.inside_can:
            distances = []
            for direction in DIRECTIONS:
                d = self._line_of_sight(direction)
                distances.append(d)
            m = min(distances)
            if m < max(self.board.height + 1, self.board.width + 1):
                i = distances.index(m)
                self.move(DIRECTIONS[i])
            else:
                Raccoon.take_turn(self)

    def get_symbol(self) -> str:
        """
        Return '@' to represent that this SmartRaccoon is inside a Garbage Can
        and 'S' otherwise.
        """
        if self.inside_can:
            return '@'
        return 'S'


@check_contracts
class GarbageCan(Character):
    """A garbage can in the game.

    Attributes:
    - locked: whether this GarbageCan is locked.

    === Sample Usage ===
    >>> b = GameBoard(2, 2)
    >>> g = GarbageCan(b, 0, 0, False)
    >>> g.x, g.y
    (0, 0)
    >>> g.locked
    False
    """
    locked: bool

    def __init__(self, b: GameBoard, x: int, y: int, locked: bool) -> None:
        """Initialize this GarbageCan to be at tile (<x>, <y>) and store
        whether it is locked or not based on <locked>.

        Preconditions:
        - the parameters are consistent with the preconditions of Character.__init__
        """
        Character.__init__(self, b, x, y)
        self.locked = locked

    def get_symbol(self) -> str:
        """
        Return 'C' to represent a closed garbage can and 'O' to represent
        an open (unlocked) garbage can.
        """
        if self.locked:
            return 'C'
        return 'O'

    def move(self, direction: tuple[int, int]) -> bool:
        """
        Garbage cans cannot move, so always return False.
        """
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    check_pyta = True  # set to False if you don't want to run pyTA
    if check_pyta:
        python_ta.check_all(config=pyta_config)
