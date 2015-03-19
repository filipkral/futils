program squareit
    implicit none
    
    real (kind=8), dimension(3) :: y, z
    integer :: n
    
    y = (/2., 3., 4./)
    n = size(y)
    call square(y, n, z)
    
    print *, "z=", z
    
end program squareit

subroutine square(y,n,f)
    implicit none
    
    integer, intent(in) :: n
    real (kind=8), dimension(n), intent(in) :: y
    real (kind=8), dimension(n), intent(out) :: f

    f = y**2
    
end subroutine square