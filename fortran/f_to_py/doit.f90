! bits of fortran to convert with f2py
! call f2py like this:
! f2py -m <output python module name> -c <intput fortran file>

real (kind=8) function doit(x)
    real (kind=8) :: x
    doit = x*x
end function

subroutine subit(a,b,c,d)
    real (kind=8), intent(in) :: a, b
    real (kind=8), intent(out) :: c,d
    c = a-b
    d = a+b
end subroutine subit