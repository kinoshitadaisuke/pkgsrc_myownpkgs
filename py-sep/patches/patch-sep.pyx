$NetBSD$

--- sep.pyx.orig	2024-10-09 16:07:03.958975386 +0000
+++ sep.pyx
@@ -552,12 +552,12 @@ cdef class Background:
 # This needs to match the result from extract
 cdef packed struct Object:
     np.float64_t thresh
-    np.int_t npix
-    np.int_t tnpix
-    np.int_t xmin
-    np.int_t xmax
-    np.int_t ymin
-    np.int_t ymax
+    np.int64_t npix
+    np.int64_t tnpix
+    np.int64_t xmin
+    np.int64_t xmax
+    np.int64_t ymin
+    np.int64_t ymax
     np.float64_t x
     np.float64_t y
     np.float64_t x2
@@ -576,11 +576,11 @@ cdef packed struct Object:
     np.float64_t errx2
     np.float64_t erry2
     np.float64_t errxy
-    np.int_t xcpeak
-    np.int_t ycpeak
-    np.int_t xpeak
-    np.int_t ypeak
-    np.int_t flag
+    np.int64_t xcpeak
+    np.int64_t ycpeak
+    np.int64_t xpeak
+    np.int64_t ypeak
+    np.int64_t flag
 
 default_kernel = np.array([[1.0, 2.0, 1.0],
                            [2.0, 4.0, 2.0],
