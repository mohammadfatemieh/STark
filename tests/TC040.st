// ********************************************************************************
// Expressions: NOT
// ********************************************************************************

FUNCTION_BLOCK TC040
  VAR
    x1 : BOOL := FALSE;
    x2 : BOOL;
  END_VAR

  x1:=NOT x1;
  x2 := TRUE;
END_FUNCTION_BLOCK