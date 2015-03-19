! This is an advanced cheat sheet for FORTRAN 90
! Make sure you read the basic cheat sheet before this one.

! Function decleration 
type FUNCTION  function-name (arg1, arg2, ..., argn)
   IMPLICIT  NONE
   
   ![specification part]
   ! variables that are function parameters must be declared with INTENT(IN)
   ! These variables cannot be changed in the function!
   INTEGER, INTENT(IN) :: arg1, arg2, ..., argn

   
   ![execution part]
   
   ![subprogram part]
   
   ! To return a value, assign value to the name of the function
   function-name = expression
   
END FUNCTION  function-name


! Watch your scope. Variables are local to the entity (program or function)
! where they are declared. However, global variables are visible in all 
! containing entities - a veriable defined in the program is visible
! in a function the program contains, unless the function declares a variable
! of the same name, which in turn has local scope in the function.


! Functions can be added as internal function to [subprogram] part of programs.
PROGRAM main
    IMPLICIT NONE
    CONTAINS
        ![functions]
END PROGRAM main

! Functions can also be placed in a module and then reused in programs
! Modules contian specification part and can contain subprogram part:
MODULE MyModule
    IMPLICIT NONE
    ![specification part]
    CONTAINS
        ![functions]
END MODULE

! Modules can be "imported" into programs right after the program decleration
PROGRAM main
    USE MyModule
    USE AnotherModule, ONLY: function1, function1
    IMPLICIT NONE
    ...
END PROGRAM main

! To compile the above program as main.out, the line below should work.
! Modules with the lowest number of dependencies should be listed first.
f90 AnotherModule.f90 MyModule.f90 main.f90 -o main
! It is possible to compile modules one by one and the main program afterwards:
f90 -c AnotherModule.f90
f90 -c MyModule.f90
f90 -c main.f90 -o main
f90 AnotherModule.o MyModule.o main.o -o main

! Naming conflicts can be resolved using '=>', see help for details.

! The examples above cover so called internal functions.
! There are also external functions, which then require calling programs
! to define INTERFACE blocks, but I don't know if there is any benefit.


! Subroutines
! Functions in FORTRAN return one value, subroutines may return none or many.

SUBROUTINE  subroutine-name (arg1, arg2, ..., argn)
   IMPLICIT  NONE
   ![specification part]
   ![execution part]
   ![subprogram part]
END SUBROUTINE  subroutine-name

! Many values can be returned using the INTENT(OUT) and INTENT(INOUT) labels,
! INTENT(IN) indicates input parameter that cannot be changed in the subroutine.

! Subroutines must be executed using the CALL statement.



! Arrays
! To declare an array with 100 real numbers in it:
real, dimension(1:100) :: a

! You can refer to elements in an array by their 1-based index.
a(1) ! the first element if dimension is 1 to something
! but dirst element may not be at index 1
read, dimension(-10, 10) :: b
b(-10) = 0 ! assign zero to the first element of b.

! Fortran implements implied do loops, similar to python list comprehension.
! The following two blocks do the same thing.
integer, dimension(1:10) :: x
integer :: i, n=10
DO i = 1,n
    write(*, *) x(i) ! using full loop
END DO
write(*, *) (x(i), i = 1, 5) ! usnig an implied loop

! The generic form of an implied DO loop is
(item-1, item-2, …,item-n, v=initial initial,final,step)
! Implied DO loops can be nested

! Array size can be determined using the following functions:
SIZE(x) ! returns number of elements of array x
LBOUND(x) ! returns lower bound index of array x
UPPER(x) ! returns upper bound index of array x

! Note that passing arrays to functions and procedures is not straightforward.
! Because the size of arrays must be declared in the decleration parts,
! lower and upper bound indices must be passed in as parameters to functions.
! Often, however, this is simplified by declaring arrays with assumed shapes.
! See http://www.cs.mtu.edu/~shene/COURSES/cs201/NOTES/chap08/assumed.html

! Multidimensional arrays are declared by simply adding higher dimensions:
real, dimension(1:5,1:5) :: x ! 2d matrix of 5 x 5
real, dimension(5,5) :: x ! same as above
integer, dimension(10,10,10,10) :: xyzt ! fourdimensional array of integers.
! FORTRAN 90 allows maximum of 7 dimensions!!!

! If array dimensions are not known at decleration, it is possible to use
! the ALOCATABLE attribute if rank of the array is known.
! The ALLOCATE statement is then used once the dimensions become known.
integer, allocatable, dimension(:) :: a ! 1d array of unknown dimensions
real, allocatable, dimension(:,:) :: b ! 2d matrix of unknown dimensions
...
integer :: v
allocate (a(50), b(10,10), v)
IF (v /= 0) write(*,*) "At least one array did not get memory!"

! Arrays can be deallocated too.
deallocate (a, b, v)
IF (v /= 0) write(*,*) "At least one array was not deallocated sucessfully."

! It is possible to test whether an array has been alocated:
IF ALLOCATED(a) THEN
    write(*,*) "Array has been allocated"
ELSE
    write(*,*) "Array has not been allocated"
END IF

IF (v /= 0) write(*,*) "At least one array did not get memory!"


!! Notes from Coursera HPC

!! Multidimensional arrays can be declares and arrays can be reshaped
real (kind=8), dimension(3,2) :: A
A = reshape(/1.,2.,3.,4.,5.,6./, /3,2/)
A(1,:) !! i-th row of array A
tranpose(A) !! transposition
matmul(A, B) !! matrix multiplication
dot_procuct(A, A) !! vector multiplication

Fortran stores multidimensional arrays by columns, not by rows like Python or C.
Therefore, in Fortran, it is faster to work on data within columns,
that means like: for j in 1 to n_cols: for i in 1 to n_rows: do something.
The reshape function has a parameter that defines how the data is stored!
In Python, numpy.reshape can specify Fortran-like or C-like (default) storage:
numpy.reshape(A, (3,2), order='F')

gfortran has some debugging flags e.g.:
gfortran -fbounds-check mycode.f90

There is also a debugger for fortran (sudo apt-get install gdb)
Once installed, you can call your program with gdb
gdb a.out








