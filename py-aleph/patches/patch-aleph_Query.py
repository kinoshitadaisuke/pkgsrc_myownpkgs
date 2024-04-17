$NetBSD$

--- aleph/Query.py.orig	2024-04-17 03:10:20.047918715 +0000
+++ aleph/Query.py
@@ -6,7 +6,7 @@ from astropy.time import Time
 import sqlite3, time, warnings, os
 import numpy as np
 import multiprocessing as mp
-from astropy.coordinates.angle_utilities import angular_separation
+from astropy.coordinates import angular_separation
 from .aleph_utils import *
 from astropy.table import QTable, Table, hstack
 import pandas as pd
