for I in[I:=input]*int(I()):
 N,R=int(I())+1,I()
 for l in range(1,N):
  if len({R[b:b+l]for b in range(N-l)})==N-l:break
 print(l)