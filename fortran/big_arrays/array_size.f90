!! What is the largest array I can allocate?

program bigarray
    implicit none
    
    integer, allocatable, dimension(:,:) :: a
    real(kind=8), allocatable, dimension(:,:) :: b
    
    !!integer :: n = 100000
    !!allocate(a(n,n))
    
    allocate(a(700000/3,130000/3)) !! 70000/3, 1300000/3 (UK at 3 m) integer
    allocate(b(700000/4,130000/4)) !! 70000/4, 1300000/4 (UK at 4 m) real8

end program bigarray