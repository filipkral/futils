! This is a basic cheat sheet for FORTRAN 90

! Comments are marked by an exlamation mark.
! Each statement must be on one line, continuation character is '&'
! Special characters: ' " ( ) * + - / : = _ ! & $ ; < > % ? , . space

! Character strings can use double quotes or single quotes
! Mixing of single and double quotes is allowed as in "Python's"

! Identifiers can have <= 31 characters, first is letter, then letters, numbers, underscores.
! Itentifier names are case insensitive. Fortran is case insensitive.

! Basic variable types: INTEGER, REAL, COMPLEX, LOGICAL, CHARACTER
! Logical values are either .TRUE. or .FALSE.
! Variable decleration: type-specifier :: list of variable names
INTEGER :: i, j, k
REAL :: area, width, height
! Declaration of character strings must include length, default is 1.
CHARACTER(20) :: first_name, last_name    ! strings of length 20
CHARACTER(10) :: a, b, c*20, d*2          ! strings of length 10, 10, 20, 2
CHARACTER(LEN=*) :: title, description    ! length will be elsewhere

! Variables can be initialized at decleration,
! right hand expressions must contain only constants and raw values:
REAL :: epsilon = 1e-7, r = 6378.0
CHARACTER(10) :: a = "hello" ! a now contains "hello     "


! Contstants can be declared for example like this:
REAL, PARAMETER :: PI = 3.141592, E = 2.71828

! Operators:
! Arithmetic: **, *, /, +, -
! Relational: <, <=, >, >=, ==, /=
! Logical: .NOT., .AND., .OR., .EQV., .NEQV.
! The exponential operator ** has the highest priority, -3**2 == (-3**2) == 9.

! Watch out for types of results of arithmetic operations:
! 15/4 is 3, 15.0/4.0 is 3.75, 15.0/4 is 3.75, 15/4.0 is 3.75

! String concatenation operator is //
! Substrings: charvar(start,end), first charater has index 1
CHARACTER a = 'abcdefg'
a(2:4) ! 'bcd'
a(:4)  ! 'abcd'
a(4:)  ! 'defg'
a(2:4) = 'BCD' ! a is now 'aBCDefg'


! Intrinsic (i.e. builtin) functions:
ABS, SQRT, SIN, COS, TAN, ASIN, ACOS, ATAN, EXP, LOG
INT (integer part), NINT (nearest integer), FLOOR, FRACTION, REAL
MAX(x1,x2,..., xN), MIN(x1,x2,..., xN), MOD(x, y)


! The READ statement can be used to read data from console input.
! To read string and two reals separated by space(s) or blank lines:
CHARACTER(10) :: Title
REAL :: a, b
READ(*,*) Title, a, b
READ(*,*)    ! without a list of variables skips a line of input.
! To read into LOGICAL variable, use T for .TRUE. and F for .FALSE.

! The WRITE statement can be used to print data to console.
WRITE(*,*) 'Iteration = ', i
WRITE(*,*) ! display blank line
WRITE(*,*) area, length


! If statements

! Complicated
IF (logical-expression-1) THEN
    statement-1
ELSE IF  (logical-expression-2) THEN
    statement-2
ELSE IF  (logical-expression-3) THEN
    statement-3
ELSE
    statement-4
END IF

! Basic
IF (logical-expression) THEN
    statement-1
ELSE
    statement-2
END IF

! Simple
IF (logical-expression) THEN
    statements
END IF

! Simplest
IF (logical-expression) statement


! Select case statement is another selective execution statement.
! See help for more complex examples.
SELECT CASE(selector)
    CASE (1)
        WRITE(*,*) "Selector is 1"
    CASE (2)
        WRITE(*,*) "Selector is 2"
    CASE DEFAULT
        WRITE(*,*) "Selector is not 1 or 2"
END SELECT



! Loops
! General DO-loop needs an EXIT statement to stop
DO
   statements-1
   IF (logical-expression) THEN
      statements-THEN
      EXIT
   END IF
   statements-2
END DO

! It is often easier to use loop that looks like a for loop
DO control-var = initial-value, final-value, [step-size]
   statements
END DO

! EXIT and CYCLE are like break and continue in Python.

! A typical program structure is:

PROGRAM program-name
    IMPLICIT NONE
    [specification part]
    [execution part]
    [subprogram part]
END PROGRAM program-name
