pip install wget
import subprocess
import sys
sys.path
python -V

import wget


def runcmd(cmd, verbose=False, *args, **kwargs):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass


runcmd('echo "Hello, World!"', verbose=True)
runcmd("wget https://www.scrapingbee.com/images/logo-small.png", verbose = True)