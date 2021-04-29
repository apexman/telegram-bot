from bot import run_bot
from configs import Configs

if __name__ == "__main__":
    run_bot(Configs().get_token())
