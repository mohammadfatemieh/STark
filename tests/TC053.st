// ********************************************************************************
// Expressions: EXPT Macro
// ********************************************************************************

FUNCTION_BLOCK TC053
  VAR
    x1 : REAL := 1.0;
    x2 : REAL := 2.0;
	x3 : REAL;
  END_VAR

  x3:=EXPT(x1,x2);
END_FUNCTION_BLOCK