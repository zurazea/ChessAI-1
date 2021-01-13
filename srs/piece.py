class Square:
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return 'hello'

class Piece(Square):
    def __init__(self, is_white, location):
        super().__init__(location)
        self.is_white = is_white


class Knight(Piece):
    def __init__(self, is_white, location):
        super().__init__(is_white, location)

    def move(self, location):
        pass


class King(Piece):
    def __init__(self, is_white, location):
        super().__init__(is_white, location)

    def move(self, location):
        pass
    
class Queen(Piece):
    def __init__(self, is_white, location):
        super().__init__(is_white, location)

    def move(self, location):
        pass

class Rook(Piece):
    def __init__(self, is_white, location):
        super().__init__(is_white, location)

    def move(self, location):
        pass

class Bishop(Piece):
    def __init__(self, is_white, location):
        super().__init__(is_white, location)

    def move(self, location):
        pass

class Pawn(Piece):
    def __init__(self, is_white, location):
        super().__init__(is_white, location)

    def move(self, location):
        pass  
