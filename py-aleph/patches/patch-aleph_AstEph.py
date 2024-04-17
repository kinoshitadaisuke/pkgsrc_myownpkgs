$NetBSD$

--- aleph/AstEph.py.orig	2024-04-17 03:10:09.167128122 +0000
+++ aleph/AstEph.py
@@ -6,7 +6,7 @@ from astropy.time import Time
 import sqlite3, time, warnings, os
 import numpy as np
 import multiprocessing as mp
-from astropy.coordinates.angle_utilities import angular_separation
+from astropy.coordinates import angular_separation
 from .aleph_utils import *
 from astropy.table import QTable, Table, hstack
 
@@ -54,4 +54,4 @@ class AstEph:
             info = np.array(self.cursor.fetchall(), dtype=str)
             self.numbers_db = np.array([getint(num) for num in info[:,1]])
             self.names_db = np.array([nm.strip() for nm in info[:,0]])
-            self.H_db = info[:,2].astype(float); self.G_db = info[:,3].astype(float)
\ No newline at end of file
+            self.H_db = info[:,2].astype(float); self.G_db = info[:,3].astype(float)
