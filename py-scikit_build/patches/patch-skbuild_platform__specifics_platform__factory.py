$NetBSD$

--- skbuild/platform_specifics/platform_factory.py.orig	2020-02-02 00:00:00.000000000 +0000
+++ skbuild/platform_specifics/platform_factory.py
@@ -34,7 +34,7 @@ def get_platform() -> abstract.CMakePlat
 
         return osx.OSXPlatform()
 
-    if this_platform in {"freebsd", "os400", "openbsd"}:
+    if this_platform in {"freebsd", "os400", "openbsd", "netbsd"}:
         from . import bsd
 
         return bsd.BSDPlatform()
