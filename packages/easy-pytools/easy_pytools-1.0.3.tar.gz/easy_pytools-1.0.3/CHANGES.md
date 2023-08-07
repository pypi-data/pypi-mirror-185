------
# CHANGELOG

## 1.0.1 -> 1.0.2:

**Backward compatible**

Affected:
- easy_pytools.sql
  - Table
    - Constraints more informative
  - DBase
    - connection and cursor close on __del__

## 1.0 -> 1.0.1:

**Backward compatible**

Affected:
- easy_pytools.sql.parsing
  - Affected entities:
    - map_to_schema
    - seq_to_schema
    - seq_to_table
    - map_to_base
  - What is it:
    - Now you can specify foreign fields in 'foreign_fields' parameter

----