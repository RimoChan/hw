from pathlib import Path
here = Path(__file__).parent

with open(here/'灵牌.txt') as f:
    灵牌 = f.read()
地址 = f'https://api.telegram.org/bot{灵牌}/'
