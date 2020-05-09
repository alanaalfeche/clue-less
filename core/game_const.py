# Declare constants for Game
PLUM ='Prof. Plum'
WHITE = 'Mrs. White'
MUSTARD = 'Col. Mustard'
SCARLET = 'Miss Scarlet'
PEACOCK = 'Mrs. Peacock'
GREEN = 'Mr. Green'
CHARACTERS = (PLUM, WHITE, MUSTARD, SCARLET, PEACOCK, GREEN)

REVOLVER = 'Revolver'
DAGGER = 'Dagger'
PIPE = 'Lead Pipe'
ROPE = 'Rope'
CANDLESTICK = 'Candlestick'
WRENCH = 'Wrench'
WEAPONS = (REVOLVER, DAGGER, PIPE, ROPE, CANDLESTICK, WRENCH)

STUDY = 'Study'
HALL = 'Hall'
LOUNGE = 'Lounge'
LIBRARY = 'Library'
BILLIARD = 'Billiard Room'
DINING = 'Dining Room'
BALLROOM = 'Ballroom'
KITCHEN = 'Kitchen'
CONSERVATORY = 'Conservatory'
ROOMS = (STUDY, HALL, LOUNGE, LIBRARY, BILLIARD, DINING, BALLROOM, KITCHEN, CONSERVATORY)

HALLWAY = 'test'
EMPTY = ''
ROOMS_LAYOUT = (
    STUDY,                   (STUDY, HALL),            HALL,                 (HALL, LOUNGE),      LOUNGE,
    (STUDY, LIBRARY),        EMPTY,                    (HALL, BILLIARD),     EMPTY,               (LOUNGE, DINING),
    LIBRARY,                 (LIBRARY, BILLIARD),      BILLIARD,             (DINING, BILLIARD),  DINING, 
    (CONSERVATORY, LIBRARY), EMPTY,                    (BALLROOM, BILLIARD), EMPTY,               (DINING, KITCHEN),
    CONSERVATORY,            (BALLROOM, CONSERVATORY), BALLROOM,             (KITCHEN, BALLROOM), KITCHEN)

HALLWAYS = (
    (STUDY, HALL),
    (STUDY, LIBRARY),
    (HALL, BILLIARD),
    (HALL, LOUNGE),
    (LOUNGE, DINING),
    (DINING, BILLIARD),
    (DINING, KITCHEN),
    (KITCHEN, BALLROOM),
    (BALLROOM, CONSERVATORY),
    (BALLROOM, BILLIARD),
    (CONSERVATORY, LIBRARY),
    (LIBRARY, BILLIARD),
)

SECRET_PASSAGES = (
    (STUDY, KITCHEN),
    (CONSERVATORY, LOUNGE)
)

START_HALLWAY = {
    PLUM: (STUDY, LIBRARY),
    WHITE: (KITCHEN, BALLROOM),
    MUSTARD: (LOUNGE, DINING),
    SCARLET: (HALL, LOUNGE),
    PEACOCK: (CONSERVATORY, LIBRARY),
    GREEN: (BALLROOM, CONSERVATORY),
}