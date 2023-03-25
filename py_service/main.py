import logging
import argparse

VOLUME_PATH = '/var/vol_pywebs'

logging.basicConfig(
    filename=f'{VOLUME_PATH}/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )

def run_t1():
    logging.info("Main task")

def run_t2():
    logging.info('Secondary task')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run specific tasks.')
    parser.add_argument('-t1',action='store_true', required=False)
    parser.add_argument('-t2',action='store_true', required=False)
    args = parser.parse_args()

    if (args.t1):
        run_t1()
    elif (args.t2):
        run_t2()
    else:
        logging.info('Script ran without arguments.')
