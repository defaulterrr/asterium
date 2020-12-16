# pr_num:       st            A, resA	
#               clear         R7	
#               ld            R3, #-1	
#               push          R3	
#               compr         A, R7	
#               jlt           minuss	; если число отрицательное 
#               mov           R2, A	
			
# ; Вывод положительного числа		
# plus:	ld	R3,#10	
# 	divr	R2, R3	
# 	mulr	R3, R2
# 	subr	A, R3	
# 	add	A, #48	
# 	push	A
# 	compr	R2, R7	
# 	jeq	outN	
# 	mov	A, R2
# 	jmp	plus		
			
# outN:         ld	R3, #-1	
# nextN:	pop	A	
# 	compr	A, R3	
# 	jeq	backNum	
# 	wd	#0	
# 	jmp	nextN
	
# ; Выход из подпрограммы		
# backNum:      ld	A, resA	
#               ret		
			
	
# ; Вывод минуса и переход к положительному числу	
# minuss:	clear	R2	
# 	subr	R2, A
			
# 	ld	A, #45	
# 	wd	#0	
# 	mov	A, R2	
# 	jmp	plus	


# Print class should create calls to native print functions and enable print function import to the file
class Print():
    def __init__(self, var):
        self.var = var
        pass