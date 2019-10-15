import logging

def log(msg, *args, **kwargs):
    logging.info("[GONGLOG][Launchpad_Pro95] %s", msg.format(*args, **kwargs))
