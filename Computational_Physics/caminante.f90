program caminante
	implicit real*8(a-h,o-z)
	integer,parameter :: Npasos=15000 !Numero Maximo de Saltos
	integer,parameter :: Ntiemp=1   !Numero de trayectoria
	real*8 :: cuad(4) !acumulador para los cuadrantes por trayectoria
	real*8 ::  rN4(4) !acumulador para los cuadrantes ensamble
	real*8 ::  iiN4(4)
	real*8, allocatable :: rx(:),ry(:),suma(:)	
	external ran2

	open(20,file='saltos_rana.dat')
	open(30,file='varianza_posta.dat')
	open(50,file='convergente.dat')
	open(60,file='cuartos.dat')
	
	idum=123456 !semilla inicial
	
	allocate(rx(0:Npasos-1),ry(0:Npasos-1),suma(Npasos-1))
	
	dp=1.d0 !Salto de Rana
	
	suma=0.d0
	rN4=0.d0
	
	do ii=1,Ntiemp  !Numero de dif. trayectorias
	cuad=0.d0

	x=0.d0 ; rx(0)=x          !Posicion inicial en X 
	y=0.d0 ; ry(0)=y	  !Posicion inicial en Y
		
	do i=1,Npasos-1  !Numero de Saltos en la trayectoria
	 rho=ran2(idum)  !Numero aleatorio unif. distribuido
!---------------------------------------------------------	 
	 if(rho <= 0.25d0) then
	 x=x+dp                        !Este
	 else if(rho > 0.25d0 .and. rho <= 0.5d0) then
	 x=x-dp                        !Oeste
	 else if(rho > 0.5d0 .and. rho <= 0.75d0)then
	 y=y+dp                        !Norte		
 	 else if(rho > 0.75d0)then
	 y=y-dp                        !Sur	
	 end if
	 rx(i)=x;ry(i)=y         !Reasigno Posiciones
	 write(20,*)x,y
!-----------------------------------------------------------
!calculo el numero de veces que la rana visita un cuadrante
!-----------------------------------------------------------	 
	 if(x>0.d0)then
	 
	  if(y>0.d0)then
	  cuad(1)=cuad(1)+1.d0
	  else
	  cuad(4)=cuad(4)+1.d0
	  endif
	  
	 else
	 
	  if(y>0.d0)then
	  cuad(2)=cuad(2)+1.d0
	  else
	  cuad(3)=cuad(3)+1.d0
	  endif
	  
	 endif 	
!----------------------------------------------------------	
	end do
	
	do nn=1,4
	cuad(nn)=cuad(nn)/dfloat(Npasos-1)
	enddo
	!write(50,200)ii,cuad(1),cuad(2),cuad(3),cuad(4)
		
	i=0
	j=1	
	do while(i+j<=Npasos-1)
	 n=i+j               !el numero de saltos aumenta segun serie de fibonaci
	 kmax=Npasos-n-1     !
	 rr2=0.d0
	  do k=0,kmax
	    rrx2=(rx(n+k)-rx(k))*(rx(n+k)-rx(k))
	    rry2=(rx(n+k)-rx(k))*(rx(n+k)-rx(k))	   
	    rr2=rr2 + rrx2 + rry2
	  enddo
	  suma(n)=suma(n)+rr2/dfloat(Npasos-n)
 	 i=j
    	 j=n
	enddo            
        
        do nn=1,4
        rN4(nn)=rN4(nn)+ cuad(nn)
        enddo
        
        !---------------------
        !cuartos convergentes
        do nn=1,4
        iiN4(nn)=rN4(nn)/dfloat(ii)
        write(50,200)ii,iiN4(1),iiN4(2),iiN4(3),iiN4(4)
        enddo      
       !---------------------
        
        end do !Numero de trayectorias 
        
        do nn=1,4
        rN4(nn)=rN4(nn)/dfloat(Ntiemp)
        write(60,*)rN4(nn)
        enddo
        !write(*,*)rN4(1)+rN4(2)+rN4(3)+rN4(4)
        
        
        
        
        i=0
        j=1
        do while(i+j<=Npasos-1)
	 n=i+j
	 write(30,*)n,suma(n)/dfloat(Ntiemp)
	 i=j
	 j=n
        enddo  	 
        



200    format(i5,x,4(f10.6,x))

        end program

	FUNCTION ran2(idum)
      	INTEGER idum,IM1,IM2,IMM1,IA1,IA2,IQ1,IQ2,IR1,IR2,NTAB,NDIV
      	REAL*8 ran2,AMM,EPS,RNMX
      	PARAMETER (IM1=2147483563,IM2=2147483399,AMM=1./IM1,IMM1=IM1-1,&
        IA1=40014,IA2=40692,IQ1=53668,IQ2=52774,IR1=12211,IR2=3791,&
        NTAB=32,NDIV=1+IMM1/NTAB,EPS=1.2e-7,RNMX=1.-EPS)
      	INTEGER idum2,j,k,iv(NTAB),iy
      	SAVE iv,iy,idum2
      	DATA idum2/24453211/, iv/NTAB*0/, iy/0/
      	IF(idum.le.0)THEN
      	idum=max(-idum,1)
      	idum2=idum
      	DO 11 j=NTAB+8,1,-1
      	k=idum/IQ1
      	idum=IA1*(idum-k*IQ1)-k*IR1
      	IF(idum.lt.0) idum=idum+IM1
      	IF(j.le.NTAB) iv(j)=idum
11    	CONTINUE
      	iy=iv(1)
      	END IF
      	k=idum/IQ1
      	idum=IA1*(idum-k*IQ1)-k*IR1
      	IF(idum.lt.0) idum=idum+IM1
      	k=idum2/IQ2
      	idum2=IA2*(idum2-k*IQ2)-k*IR2
      	IF(idum2.lt.0) idum2=idum2+IM2
      	j=1+iy/NDIV
      	iy=iv(j)-idum2
      	iv(j)=idum
      	IF(iy.lt.1)iy=iy+IMM1
      	ran2=min(AMM*iy,RNMX)
      	RETURN
      	END FUNCTION
      	
      	
      	


