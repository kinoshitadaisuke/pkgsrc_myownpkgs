$NetBSD: patch-setup.py,v 1.1 2024/08/05 20:38:39 adam Exp $

Allow cmake to find pybind11 config files.

--- setup.py.orig	2022-12-18 09:35:42.000000000 +0000
+++ setup.py
@@ -16,6 +16,7 @@
 
 import os
 import platform
+import site
 import shutil
 import subprocess
 import sys
@@ -86,9 +87,11 @@ class BuildCMakeExtension(build_ext.buil
     extension_dir = os.path.abspath(
         os.path.dirname(self.get_ext_fullpath(ext.name)))
     build_cfg = 'Debug' if self.debug else 'Release'
+    site_dir = site.getsitepackages()[0]
     cmake_args = [
         f'-DPython3_ROOT_DIR={sys.prefix}',
         f'-DPython3_EXECUTABLE={sys.executable}',
+        f'-Dpybind11_DIR={site_dir}/pybind11/share/cmake/pybind11',
         f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extension_dir}',
         f'-DCMAKE_BUILD_TYPE={build_cfg}'
     ]
@@ -108,7 +111,7 @@ class BuildCMakeExtension(build_ext.buil
     subprocess.check_call(
         ['cmake', ext.source_dir] + cmake_args, cwd=self.build_temp)
     subprocess.check_call(
-        ['cmake', '--build', '.', f'-j{os.cpu_count()}', '--config', build_cfg],
+        ['cmake', '--build', '.', '--config', build_cfg],
         cwd=self.build_temp)
 
     # Force output to <extension_dir>/. Amends CMake multigenerator output paths
