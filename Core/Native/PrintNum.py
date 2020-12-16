printfuncs = """
pr_num:         st      A, resA	
                clear   R7	
                ld      R3, #-1	
                push    R3	
                compr   A, R7	
                jlt     minuss
                mov     R2, A		
plus:	        ld	    R3,#10	
                divr	R2, R3	
                mulr	R3, R2
                subr	A, R3	
                add	    A, #48	
                push	A
                compr	R2, R7	
                jeq	    outN	
                mov	    A, R2
                jmp	    plus		
			
outN:           ld	    R3, #-1	
nextN:	        pop	    A	
	            compr	A, R3	
	            jeq	    backNum	
	            wd	    #0	
	            jmp	    nextN	
backNum:        ld	    A, resA	
                ret		
minuss:	        clear	R2	
	            subr	R2, A		
	            ld	    A, #45	
	            wd	    #0	
                mov	    A, R2	
	            jmp	    plus	
"""