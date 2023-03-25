from datetime import datetime
import logging
VOLUME_PATH = '/var/vol_pywebs'
logging.basicConfig(
    filename=f'{VOLUME_PATH}/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
logging.warning('This will get logged to a file')

def run():
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    logging.warning("Logging test")

if __name__ == "__main__":
    run()