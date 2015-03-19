program square
    implicit none
    
    real (kind=8) :: y, z
    real (kind=8), external :: f
    
    read(*,*) y
    z = f(y)
    print *, "z=", z

end program square

!! function defined in the same file
real (kind=8) function f(x)
    implicit none
    real (kind=8), intent(in) :: x
    f = x**2
end function f

