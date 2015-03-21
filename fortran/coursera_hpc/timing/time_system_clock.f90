program time_system_clock
    integer(kind=8), parameter ::  n=1000
    integer(kind=8) :: i, t1, t2, clock_rate
    real(kind=8), dimension(n) :: x
    real(kind=8) :: elapsed_time, t1cpu, t2cpu
    
    !! remember start time
    call system_clock(t1)
    call cpu_time(t1cpu)
    
    !! do some worh
    do i = 1,size(x)
        x = i**2
    end do
    
    !! remember end time and clock rate
    call system_clock(t2, clock_rate)
    call cpu_time(t2cpu)
    
    elapsed_time = (t2 - t1) / clock_rate
    write(*,*) "Total system time elapsed: ", elapsed_time
    write(*,*) "Total CPU time elapsed: ", t2cpu - t1cpu

end program time_system_clock