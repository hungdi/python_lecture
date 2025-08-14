from pathlib import Path
from functools import lru_cache
from PyQt5.QtGui import QPixmap

# 현재 파일: game/util/assets.py
# parents[0] = game/util
# parents[1] = game
# parents[2] = 프로젝트 루트(99_bonus_chapter02)
ROOT = Path(__file__).resolve().parents[2]
ASSETS_DIR = ROOT / "assets"

@lru_cache(maxsize=None)
def pix(name: str) -> QPixmap:
    p = ASSETS_DIR / name
    pm = QPixmap(str(p))
    if pm.isNull():
        raise FileNotFoundError(f"asset not found: {p}")
    return pm
