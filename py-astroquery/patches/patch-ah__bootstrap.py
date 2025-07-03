$NetBSD$

--- ah_bootstrap.py.orig	2024-08-09 17:25:38.070419800 +0000
+++ ah_bootstrap.py
@@ -53,7 +53,7 @@ from configparser import ConfigParser, R
 import pkg_resources
 
 from setuptools import Distribution
-from setuptools.package_index import PackageIndex
+#from setuptools.package_index import PackageIndex
 
 # This is the minimum Python version required for astropy-helpers
 __minimum_python_version__ = (3, 5)
@@ -596,12 +596,12 @@ class _Bootstrapper(object):
         req = pkg_resources.Requirement.parse(
             '{0}>{1},<{2}'.format(DIST_NAME, dist.version, next_version))
 
-        package_index = PackageIndex(index_url=self.index_url)
+#        package_index = PackageIndex(index_url=self.index_url)
 
-        upgrade = package_index.obtain(req)
+#        upgrade = package_index.obtain(req)
 
-        if upgrade is not None:
-            return self._do_download(version=upgrade.version)
+#        if upgrade is not None:
+#            return self._do_download(version=upgrade.version)
 
     def _check_submodule(self):
         """
