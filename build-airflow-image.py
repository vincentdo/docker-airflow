from shutil import copy2, copytree, rmtree
from subprocess import check_call
from os import remove

TOP_LEVEL_FILES = [ 'requirements.txt', 'index.py', 'config.py', '.env' ]
CURRENT_DIR = './';

def copyFiles():
    # Copy top level files
    for file in TOP_LEVEL_FILES:
        copy2('../' + file, CURRENT_DIR)

    # Copy Offer.json from static
    copy2('../static/ethereum/build/contracts/Offer.json', CURRENT_DIR)

    # Copy specific folders from application
    copytree('../application', CURRENT_DIR + '/application')

def removeFiles():
    # Delete copied application folder
    rmtree('./application')

    # Delete Offer.json
    remove('Offer.json')

    # Delete top level files
    for file in TOP_LEVEL_FILES:
        remove(file)

try:
    copyFiles()
    # Build the docker image
    # docker build --rm -t puckel/docker-airflow .
    check_call(['docker', 'build', '--rm', '-t', 'puckel/docker-airflow', '.'])
finally:
    removeFiles()

