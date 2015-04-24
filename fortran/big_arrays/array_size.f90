!! What is the largest array I can allocate?

program bigarray
    implicit none
    
    integer, allocatable, dimension(:,:) :: a
    real(kind=8), allocatable, dimension(:,:) :: b
    real(kind=8), allocatable, dimension(:) :: c
    
    !!integer :: n = 100000
    !!allocate(a(n,n))
    
    allocate(a(700000/10,1300000/10)) !! 70000/3, 1300000/3 (UK at 3 m) integer
    
    !!allocate(b(700000/20,1300000/20)) !! 70000/4, 1300000/4 (UK at 4 m) real8
    !!write(*,*) (700000/4) !*(1307000/4)
    !!integer :: n = (700000/4)*(130000/4)
    !!allocate(c(700000)) !! 70000/4*1300000/4

end program bigarray