$NetBSD$

--- build-tools/fix-rpath.sh.orig	2026-08-25 15:43:38.638730375 +0000
+++ build-tools/fix-rpath.sh
@@ -1,4 +1,4 @@
-#!/bin/bash
+#!/usr/pkg/bin/bash
 #
 # If conda's gfortran compiler has been used, convert the relative linker
 # paths that it inserts into absolute paths.  This makes the as-built binary
