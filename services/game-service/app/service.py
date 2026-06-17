from sqlalchemy.orm import Session
from app import repository, schemas
from app.infrastructure.cache import set_game_summary

def add_game(db: Session, data: schemas.GameCreate) -> schemas.GameOut:
    game = repository.create_game(db, data)
    set_game_summary(game.id, {
        "id": game.id,
        "title": game.title,
        "genre": game.genre,
        "platform": game.platform,
        "cover_url": game.cover_url,
    })
    return schemas.GameOut.model_validate(game)

def fetch_game(db: Session, game_id: str) -> schemas.GameOut:
    game = repository.get_game(db, game_id)
    if game is None:
        raise ValueError("Game not found")
    return schemas.GameOut.model_validate(game)

def fetch_all_games(db: Session, limit: int = 20, offset: int = 0) -> schemas.GameList:
    items, total = repository.list_games(db, limit=limit, offset=offset)
    return schemas.GameList(
        items=[schemas.GameOut.model_validate(g) for g in items],
        total=total, limit=limit, offset=offset
    )

def find_games(db: Session, q: str, limit: int = 20, offset: int = 0) -> schemas.GameList:
    items, total = repository.search_games(db, q, limit=limit, offset=offset)
    return schemas.GameList(
        items=[schemas.GameOut.model_validate(g) for g in items],
        total=total, limit=limit, offset=offset
    )
