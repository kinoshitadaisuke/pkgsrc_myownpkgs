$NetBSD$

--- build-tools/generate-version-h.sh.orig	2026-08-25 15:43:54.069152635 +0000
+++ build-tools/generate-version-h.sh
@@ -1,4 +1,4 @@
-#!/bin/bash
+#!/usr/pkg/bin/bash
 #
 # (Re)Generate the contents of version.h with the version given on the
 # command line.  Output to stdout. Called from build/Makefile.
