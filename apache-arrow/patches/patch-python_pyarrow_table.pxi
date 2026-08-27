$NetBSD$

--- python/pyarrow/table.pxi.orig	2026-08-27 16:38:53.910562857 +0000
+++ python/pyarrow/table.pxi
@@ -6293,8 +6293,8 @@ def concat_tables(tables, MemoryPool mem
     else:
         raise ValueError(f"Invalid promote options: {promote_options}")
 
+    options.unify_schemas = promote_options != "none"
     with nogil:
-        options.unify_schemas = promote_options != "none"
         c_result_table = GetResultValue(
             ConcatenateTables(c_tables, options, pool))
 
