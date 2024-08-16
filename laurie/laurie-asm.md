
---

Voici l'intégralité du code ASM pour le programme, y compris les six phases ainsi que la fonction `main` :

### Fonction `main`
```asm
(gdb) disas main
Dump of assembler code for function main:
   0x080489b0 <+0>:	push   %ebp
   0x080489b1 <+1>:	mov    %esp,%ebp
   0x080489b3 <+3>:	sub    $0x14,%esp
   0x080489b6 <+6>:	push   %ebx
   0x080489b7 <+7>:	mov    0x8(%ebp),%eax
   0x080489ba <+10>:	mov    0xc(%ebp),%ebx
   0x080489bd <+13>:	cmp    $0x1,%eax
   0x080489c0 <+16>:	jne    0x80489d0 <main+32>
   0x080489c2 <+18>:	mov    0x804b648,%eax
   0x080489c7 <+23>:	mov    %eax,0x804b664
   0x080489cc <+28>:	jmp    0x8048a30 <main+128>
   0x080489ce <+30>:	mov    %esi,%esi
   0x080489d0 <+32>:	cmp    $0x2,%eax
   0x080489d3 <+35>:	jne    0x8048a10 <main+96>
   0x080489d5 <+37>:	add    $0xfffffff8,%esp
   0x080489d8 <+40>:	push   $0x8049620
   0x080489dd <+45>:	mov    0x4(%ebx),%eax
   0x080489e0 <+48>:	push   %eax
   0x080489e1 <+49>:	call   0x8048880 <fopen@plt>
   0x080489e6 <+54>:	mov    %eax,0x804b664
   0x080489eb <+59>:	add    $0x10,%esp
   0x080489ee <+62>:	test   %eax,%eax
   0x080489f0 <+64>:	jne    0x8048a30 <main+128>
   0x080489f2 <+66>:	add    $0xfffffffc,%esp
   0x080489f5 <+69>:	mov    0x4(%ebx),%eax
   0x080489f8 <+72>:	push   %eax
   0x080489f9 <+73>:	mov    (%ebx),%eax
   0x080489fb <+75>:	push   %eax
   0x080489fc <+76>:	push   $0x8049622
   0x08048a01 <+81>:	call   0x8048810 <printf@plt>
   0x08048a06 <+86>:	add    $0xfffffff4,%esp
   0x08048a09 <+89>:	push   $0x8
   0x08048a0b <+91>:	call   0x8048850 <exit@plt>
   0x08048a10 <+96>:	add    $0xfffffff8,%esp
   0x08048a13 <+99>:	mov    (%ebx),%eax
   0x08048a15 <+101>:	push   %eax
   0x08048a16 <+102>:	push   $0x804963f
   0x08048a1b <+107>:	call   0x8048810 <printf@plt>
   0x08048a20 <+112>:	add    $0xfffffff4,%esp
   0x08048a23 <+115>:	push   $0x8
   0x08048a25 <+117>:	call   0x8048850 <exit@plt>
   0x08048a2a <+122>:	lea    0x0(%esi),%esi
   0x08048a30 <+128>:	call   0x8049160 <initialize_bomb>
   0x08048a35 <+133>:	add    $0xfffffff4,%esp
   0x08048a38 <+136>:	push   $0x8049660
   0x08048a3d <+141>:	call   0x8048810 <printf@plt>
   0x08048a42 <+146>:	add    $0xfffffff4,%esp
   0x08048a45 <+149>:	push   $0x80496a0
   0x08048a4a <+154>:	call   0x8048810 <printf@plt>
   0x08048a4f <+159>:	add    $0x20,%esp
   0x08048a52 <+162>:	call   0x80491fc <read_line>
   0x08048a57 <+167>:	add    $0xfffffff4,%esp
   0x08048a5a <+170>:	push   %eax
   0x08048a5b <+171>:	call   0x8048b20 <phase_1>
   0x08048a60 <+176>:	call   0x804952c <phase_defused>
   0x08048a65 <+181>:	add    $0xfffffff4,%esp
   0x08048a68 <+184>:	push   $0x80496e0
   0x08048a6d <+189>:	call   0x8048810 <printf@plt>
   0x08048a72 <+194>:	add    $0x20,%esp
   0x08048a75 <+197>:	call   0x80491fc <read_line>
   0x08048a7a <+202>:	add    $0xfffffff4,%esp
   0x08048a7d <+205>:	push   %eax
   0x08048a7e <+206>:	call   0x8048b48 <phase_2>
   0x08048a83 <+211>:	call   0x804952c <phase_defused>
   0x08048a88 <+216>:	add    $0xfffffff4,%esp
   0x08048a8b <+219>:	push   $0x8049720
   0x08048a90 <+224>:	call   0x8048810 <printf@plt>
   0x08048a95 <+229>:	add    $0x20,%esp
   0x08048a98 <+232>:	call   0x80491fc <read_line>
   0x08048a9d <+237>:	add    $0xfffffff4,%esp
   0x08048aa0 <+240>:	push   %eax
   0x08048aa1 <+241>:	call   0x8048b98 <phase_3>
   0x08048aa6 <+246>:	call   0x804952c <phase_defused>
   0x08048aab <+251>:	add    $0xfffffff4,%esp
   0x08048aae <+254>:	push   $0x804973f
   0x08048ab3 <+259>:	call   0x8048810 <printf@plt>
   0x08048ab8 <+264>:	add    $0x20,%esp
   0x08048abb <+267>:	call   0x80491fc <read_line>
   0x08048ac0 <+272>:	add    $0xfffffff4,%esp
   0x08048ac3 <+275>:	push   %eax
   0x08048ac4 <+276>:	call   0x8048ce0 <phase_4>
   0x08048ac9 <+281>:	call   0x804952c <phase_defused>
   0x08048ace <+286>:	add    $0xfffffff4,%esp
   0x08048ad1 <+289>:	push   $0x8049760
   0x08048ad6 <+294>:	call   0x8048810 <printf@plt>
   0x08048adb <+299>:	add    $0x20,%esp
   0x08048ade <+302>:	call   0x80491fc <read_line>
   0x08048ae3 <+307>:	add    $0xfffffff4,%esp
   0x08048ae6 <+310>:	push   %eax
   0x08048ae7 <+311>:	call

   0x8048d2c <phase_5>
   0x08048aec <+316>:	call   0x804952c <phase_defused>
   0x08048af1 <+321>:	add    $0xfffffff4,%esp
   0x08048af4 <+324>:	push   $0x80497a0
   0x08048af9 <+329>:	call   0x8048810 <printf@plt>
   0x08048afe <+334>:	add    $0x20,%esp
   0x08048b01 <+337>:	call   0x80491fc <read_line>
   0x08048b06 <+342>:	add    $0xfffffff4,%esp
   0x08048b09 <+345>:	push   %eax
   0x08048b0a <+346>:	call   0x8048d98 <phase_6>
   0x08048b0f <+351>:	call   0x804952c <phase_defused>
   0x08048b14 <+356>:	xor    %eax,%eax
   0x08048b16 <+358>:	mov    -0x18(%ebp),%ebx
   0x08048b19 <+361>:	mov    %ebp,%esp
   0x08048b1b <+363>:	pop    %ebp
   0x08048b1c <+364>:	ret
```

### Phase 1
```asm
(gdb) disas phase_1
Dump of assembler code for function phase_1:
   0x08048b20 <+0>:	push   %ebp
   0x08048b21 <+1>:	mov    %esp,%ebp
   0x08048b23 <+3>:	sub    $0x8,%esp
   0x08048b26 <+6>:	mov    0x8(%ebp),%eax
   0x08048b29 <+9>:	add    $0xfffffff8,%esp
   0x08048b2c <+12>:	push   $0x80497c0
   0x08048b31 <+17>:	push   %eax
   0x08048b32 <+18>:	call   0x8049030 <strings_not_equal>
   0x08048b37 <+23>:	add    $0x10,%esp
   0x08048b3a <+26>:	test   %eax,%eax
   0x08048b3c <+28>:	je     0x8048b43 <phase_1+35>
   0x08048b3e <+30>:	call   0x80494fc <explode_bomb>
   0x08048b43 <+35>:	mov    %ebp,%esp
   0x08048b45 <+37>:	pop    %ebp
   0x08048b46 <+38>:	ret
```

### Phase 2
```asm
(gdb) disas phase_2
Dump of assembler code for function phase_2:
   0x08048b48 <+0>:	push   %ebp
   0x08048b49 <+1>:	mov    %esp,%ebp
   0x08048b4b <+3>:	sub    $0x20,%esp
   0x08048b4e <+6>:	push   %esi
   0x08048b4f <+7>:	push   %ebx
   0x08048b50 <+8>:	mov    0x8(%ebp),%edx
   0x08048b53 <+11>:	add    $0xfffffff8,%esp
   0x08048b56 <+14>:	lea    -0x18(%ebp),%eax
   0x08048b59 <+17>:	push   %eax
   0x08048b5a <+18>:	push   %edx
   0x08048b5b <+19>:	call   0x8048fd8 <read_six_numbers>
   0x08048b60 <+24>:	add    $0x10,%esp
   0x08048b63 <+27>:	cmpl   $0x1,-0x18(%ebp)
   0x08048b67 <+31>:	je     0x8048b6e <phase_2+38>
   0x08048b69 <+33>:	call   0x80494fc <explode_bomb>
   0x08048b6e <+38>:	mov    $0x1,%ebx
   0x08048b73 <+43>:	lea    -0x18(%ebp),%esi
   0x08048b76 <+46>:	lea    0x1(%ebx),%eax
   0x08048b79 <+49>:	imul   -0x4(%esi,%ebx,4),%eax
   0x08048b7e <+54>:	cmp    %eax,(%esi,%ebx,4)
   0x08048b81 <+57>:	je     0x8048b88 <phase_2+64>
   0x08048b83 <+59>:	call   0x80494fc <explode_bomb>
   0x08048b88 <+64>:	inc    %ebx
   0x08048b89 <+65>:	cmp    $0x5,%ebx
   0x08048b8c <+68>:	jle    0x8048b76 <phase_2+46>
   0x08048b8e <+70>:	lea    -0x28(%ebp),%esp
   0x08048b91 <+73>:	pop    %ebx
   0x08048b92 <+74>:	pop    %esi
   0x08048b93 <+75>:	mov    %ebp,%esp
   0x08048b95 <+77>:	pop    %ebp
   0x08048b96 <+78>:	ret
```

### Phase 3
```asm
(gdb) disas phase_3
Dump of assembler code for function phase_3:
   0x08048b98 <+0>:	push   %ebp
   0x08048b99 <+1>:	mov    %esp,%ebp
   0x08048b9b <+3>:	sub    $0x14,%esp
   0x08048b9e <+6>:	push   %ebx
   0x08048b9f <+7>:	mov    0x8(%ebp),%edx
   0x08048ba2 <+10>:	add    $0xfffffff4,%esp
   0x08048ba5 <+13>:	lea    -0x4(%ebp),%eax
   0x08048ba8 <+16>:	push   %eax
   0x08048ba9 <+17>:	lea    -0x5(%ebp),%eax
   0x08048bac <+20>:	push   %eax
   0x08048bad <+21>:	lea    -0xc(%ebp),%eax
   0x08048bb0 <+24>:	push   %eax
   0x08048bb1 <+25>:	push   $0x80497de
   0x08048bb6 <+30>:	push   %edx
   0x08048bb7 <+31>:	call   0x8048860 <sscanf@plt>
   0x08048bbc <+36>:	add    $0x20,%esp
   0x08048bbf <+39>:	cmp    $0x2,%eax
   0x08048bc2 <+42>:	jg     0x8048bc9 <phase_3+49>
   0x08048bc4 <+44>:	call   0x80494fc <explode_bomb>
   0x08048bc9 <+49>:	cmpl   $0x7,-0xc(%ebp)
   0x08048bcd <+53>:	ja     0x8048c88 <phase_3+240>
   0x08048bd3 <+59>:	mov    -0xc(%ebp),%eax
   0x08048bd6 <+62>:	jmp    *0x80497e8(,%eax,4)
   0x08048bdd <+69>:	lea    0x0(%esi),%esi
   0x08048be0 <+72>:	mov    $0x71,%bl
   0x08048be2 <+74>:	cmpl   $0x309,-0

x4(%ebp)
   0x08048be9 <+81>:	je     0x8048c8f <phase_3+247>
   0x08048bef <+87>:	call   0x80494fc <explode_bomb>
   0x08048bf4 <+92>:	jmp    0x8048c8f <phase_3+247>
   0x08048bf9 <+97>:	lea    0x0(%esi,%eiz,1),%esi
   0x08048c00 <+104>:	mov    $0x62,%bl
   0x08048c02 <+106>:	cmpl   $0xd6,-0x4(%ebp)
   0x08048c09 <+113>:	je     0x8048c8f <phase_3+247>
   0x08048c0f <+119>:	call   0x80494fc <explode_bomb>
   0x08048c14 <+124>:	jmp    0x8048c8f <phase_3+247>
   0x08048c16 <+126>:	mov    $0x62,%bl
   0x08048c18 <+128>:	cmpl   $0x2f3,-0x4(%ebp)
   0x08048c1f <+135>:	je     0x8048c8f <phase_3+247>
   0x08048c21 <+137>:	call   0x80494fc <explode_bomb>
   0x08048c26 <+142>:	jmp    0x8048c8f <phase_3+247>
   0x08048c28 <+144>:	mov    $0x6b,%bl
   0x08048c2a <+146>:	cmpl   $0xfb,-0x4(%ebp)
   0x08048c31 <+153>:	je     0x8048c8f <phase_3+247>
   0x08048c33 <+155>:	call   0x80494fc <explode_bomb>
   0x08048c38 <+160>:	jmp    0x8048c8f <phase_3+247>
   0x08048c3a <+162>:	lea    0x0(%esi),%esi
   0x08048c40 <+168>:	mov    $0x6f,%bl
   0x08048c42 <+170>:	cmpl   $0xa0,-0x4(%ebp)
   0x08048c49 <+177>:	je     0x8048c8f <phase_3+247>
   0x08048c4b <+179>:	call   0x80494fc <explode_bomb>
   0x08048c50 <+184>:	jmp    0x8048c8f <phase_3+247>
   0x08048c52 <+186>:	mov    $0x74,%bl
   0x08048c54 <+188>:	cmpl   $0x1ca,-0x4(%ebp)
   0x08048c5b <+195>:	je     0x8048c8f <phase_3+247>
   0x08048c5d <+197>:	call   0x80494fc <explode_bomb>
   0x08048c62 <+202>:	jmp    0x8048c8f <phase_3+247>
   0x08048c64 <+204>:	mov    $0x76,%bl
   0x08048c66 <+206>:	cmpl   $0x30c,-0x4(%ebp)
   0x08048c6d <+213>:	je     0x8048c8f <phase_3+247>
   0x08048c6f <+215>:	call   0x80494fc <explode_bomb>
   0x08048c74 <+220>:	jmp    0x8048c8f <phase_3+247>
   0x08048c76 <+222>:	mov    $0x62,%bl
   0x08048c78 <+224>:	cmpl   $0x20c,-0x4(%ebp)
   0x08048c7f <+231>:	je     0x8048c8f <phase_3+247>
   0x08048c81 <+233>:	call   0x80494fc <explode_bomb>
   0x08048c86 <+238>:	jmp    0x8048c8f <phase_3+247>
   0x08048c88 <+240>:	mov    $0x78,%bl
   0x08048c8a <+242>:	call   0x80494fc <explode_bomb>
   0x08048c8f <+247>:	cmp    -0x5(%ebp),%bl
   0x08048c92 <+250>:	je     0x8048c99 <phase_3+257>
   0x08048c94 <+252>:	call   0x80494fc <explode_bomb>
   0x08048c99 <+257>:	mov    -0x18(%ebp),%ebx
   0x08048c9c <+260>:	mov    %ebp,%esp
   0x08048c9e <+262>:	pop    %ebp
   0x08048c9f <+263>:	ret
```

### Phase 4
```asm
(gdb) disas phase_4
Dump of assembler code for function phase_4:
   0x08048ce0 <+0>:	push   %ebp
   0x08048ce1 <+1>:	mov    %esp,%ebp
   0x08048ce3 <+3>:	sub    $0x18,%esp
   0x08048ce6 <+6>:	mov    0x8(%ebp),%edx
   0x08048ce9 <+9>:	add    $0xfffffffc,%esp
   0x08048cec <+12>:	lea    -0x4(%ebp),%eax
   0x08048cef <+15>:	push   %eax
   0x08048cf0 <+16>:	push   $0x8049808
   0x08048cf5 <+21>:	push   %edx
   0x08048cf6 <+22>:	call   0x8048860 <sscanf@plt>
   0x08048cfb <+27>:	add    $0x10,%esp
   0x08048cfe <+30>:	cmp    $0x1,%eax
   0x08048d01 <+33>:	jne    0x8048d09 <phase_4+41>
   0x08048d03 <+35>:	cmpl   $0x0,-0x4(%ebp)
   0x08048d07 <+39>:	jg     0x8048d0e <phase_4+46>
   0x08048d09 <+41>:	call   0x80494fc <explode_bomb>
   0x08048d0e <+46>:	add    $0xfffffff4,%esp
   0x08048d11 <+49>:	mov    -0x4(%ebp),%eax
   0x08048d14 <+52>:	push   %eax
   0x08048d15 <+53>:	call   0x8048ca0 <func4>
   0x08048d1a <+58>:	add    $0x10,%esp
   0x08048d1d <+61>:	cmp    $0x37,%eax
   0x08048d20 <+64>:	je     0x8048d27 <phase_4+71>
   0x08048d22 <+66>:	call   0x80494fc <explode_bomb>
   0x08048d27 <+71>:	mov    %ebp,%esp
   0x08048d29 <+73>:	pop    %ebp
   0x08048d2a <+74>:	ret
```

### Phase 5
```asm
(gdb) disas phase_5
Dump of assembler code for function phase_5:
   0x08048d2c <+0>:	push   %ebp
   0x08048d2d <+1>:	mov    %esp,%ebp
   0x08048d2f <+3>:	sub    $0x10,%esp
   0x08048d32 <+6>:	push   %esi
   

 0x08048d33 <+7>:	push   %ebx
   0x08048d34 <+8>:	mov    0x8(%ebp),%ebx
   0x08048d37 <+11>:	add    $0xfffffff4,%esp
   0x08048d3a <+14>:	push   %ebx
   0x08048d3b <+15>:	call   0x8049018 <string_length>
   0x08048d40 <+20>:	add    $0x10,%esp
   0x08048d43 <+23>:	cmp    $0x6,%eax
   0x08048d46 <+26>:	je     0x8048d4d <phase_5+33>
   0x08048d48 <+28>:	call   0x80494fc <explode_bomb>
   0x08048d4d <+33>:	xor    %edx,%edx
   0x08048d4f <+35>:	lea    -0x8(%ebp),%ecx
   0x08048d52 <+38>:	mov    $0x804b220,%esi
   0x08048d57 <+43>:	mov    (%edx,%ebx,1),%al
   0x08048d5a <+46>:	and    $0xf,%al
   0x08048d5c <+48>:	movsbl %al,%eax
   0x08048d5f <+51>:	mov    (%eax,%esi,1),%al
   0x08048d62 <+54>:	mov    %al,(%edx,%ecx,1)
   0x08048d65 <+57>:	inc    %edx
   0x08048d66 <+58>:	cmp    $0x5,%edx
   0x08048d69 <+61>:	jle    0x8048d57 <phase_5+43>
   0x08048d6b <+63>:	movb   $0x0,-0x2(%ebp)
   0x08048d6f <+67>:	add    $0xfffffff8,%esp
   0x08048d72 <+70>:	push   $0x804980b
   0x08048d77 <+75>:	lea    -0x8(%ebp),%eax
   0x08048d7a <+78>:	push   %eax
   0x08048d7b <+79>:	call   0x8049030 <strings_not_equal>
   0x08048d80 <+84>:	add    $0x10,%esp
   0x08048d83 <+87>:	test   %eax,%eax
   0x08048d85 <+89>:	je     0x8048d8c <phase_5+96>
   0x08048d87 <+91>:	call   0x80494fc <explode_bomb>
   0x08048d8c <+96>:	lea    -0x18(%ebp),%esp
   0x08048d8f <+99>:	pop    %ebx
   0x08048d90 <+100>:	pop    %esi
   0x08048d91 <+101>:	mov    %ebp,%esp
   0x08048d93 <+103>:	pop    %ebp
   0x08048d94 <+104>:	ret
```

### Phase 6
```asm
(gdb) disas phase_6
Dump of assembler code for function phase_6:
   0x08048d98 <+0>:	push   %ebp
   0x08048d99 <+1>:	mov    %esp,%ebp
   0x08048d9b <+3>:	sub    $0x4c,%esp
   0x08048d9e <+6>:	push   %edi
   0x08048d9f <+7>:	push   %esi
   0x08048da0 <+8>:	push   %ebx
   0x08048da1 <+9>:	mov    0x8(%ebp),%edx
   0x08048da4 <+12>:	movl   $0x804b26c,-0x34(%ebp)
   0x08048dab <+19>:	add    $0xfffffff8,%esp
   0x08048dae <+22>:	lea    -0x18(%ebp),%eax
   0x08048db1 <+25>:	push   %eax
   0x08048db2 <+26>:	push   %edx
   0x08048db3 <+27>:	call   0x8048fd8 <read_six_numbers>
   0x08048db8 <+32>:	xor    %edi,%edi
   0x08048dba <+34>:	add    $0x10,%esp
   0x08048dbd <+37>:	lea    0x0(%esi),%esi
   0x08048dc0 <+40>:	lea    -0x18(%ebp),%eax
   0x08048dc3 <+43>:	mov    (%eax,%edi,4),%eax
   0x08048dc6 <+46>:	dec    %eax
   0x08048dc7 <+47>:	cmp    $0x5,%eax
   0x08048dca <+50>:	jbe    0x8048dd1 <phase_6+57>
   0x08048dcc <+52>:	call   0x80494fc <explode_bomb>
   0x08048dd1 <+57>:	lea    0x1(%edi),%ebx
   0x08048dd4 <+60>:	cmp    $0x5,%ebx
   0x08048dd7 <+63>:	jg     0x8048dfc <phase_6+100>
   0x08048dd9 <+65>:	lea    0x0(,%edi,4),%eax
   0x08048de0 <+72>:	mov    %eax,-0x38(%ebp)
   0x08048de3 <+75>:	lea    -0x18(%ebp),%esi
   0x08048de6 <+78>:	mov    -0x38(%ebp),%edx
   0x08048de9 <+81>:	mov    (%edx,%esi,1),%eax
   0x08048dec <+84>:	cmp    (%esi,%ebx,4),%eax
   0x08048def <+87>:	jne    0x8048df6 <phase_6+94>
   0x08048df1 <+89>:	call   0x80494fc <explode_bomb>
   0x08048df6 <+94>:	inc    %ebx
   0x08048df7 <+95>:	cmp    $0x5,%ebx
   0x08048dfa <+98>:	jle    0x8048de6 <phase_6+78>
   0x08048dfc <+100>:	inc    %edi
   0x08048dfd <+101>:	cmp    $0x5,%edi
   0x08048e00 <+104>:	jle    0x8048dc0 <phase_6+40>
   0x08048e02 <+106>:	xor    %edi,%edi
   0x08048e04 <+108>:	lea    -0x18(%ebp),%ecx
   0x08048e07 <+111>:	lea    -0x30(%ebp),%eax
   0x08048e0a <+114>:	mov    %eax,-0x3c(%ebp)
   0x08048e0d <+117>:	lea    0x0(%esi),%esi
   0x08048e10 <+120>:	mov    -0x34(%ebp),%esi
   0x08048e13 <+123>:	mov    $0x1,%ebx
   0x08048e18 <+128>:	lea    0x0(,%edi,4),%eax
   0x08048e1f <+135>:	mov    %eax,%edx
   0x08048e21 <+137>:	cmp    (%eax,%ecx,1),%ebx
   0x08048e24 <+140>:	jge    0x8048e38 <phase_6+160>
   0x08048e

26 <+142>:	mov    (%edx,%ecx,1),%eax
   0x08048e29 <+145>:	lea    0x0(%esi,%eiz,1),%esi
   0x08048e30 <+152>:	mov    0x8(%esi),%esi
   0x08048e33 <+155>:	inc    %ebx
   0x08048e34 <+156>:	cmp    %eax,%ebx
   0x08048e36 <+158>:	jl     0x8048e30 <phase_6+152>
   0x08048e38 <+160>:	mov    -0x3c(%ebp),%edx
   0x08048e3b <+163>:	mov    %esi,(%edx,%edi,4)
   0x08048e3e <+166>:	inc    %edi
   0x08048e3f <+167>:	cmp    $0x5,%edi
   0x08048e42 <+170>:	jle    0x8048e10 <phase_6+120>
   0x08048e44 <+172>:	mov    -0x30(%ebp),%esi
   0x08048e47 <+175>:	mov    %esi,-0x34(%ebp)
   0x08048e4a <+178>:	mov    $0x1,%edi
   0x08048e4f <+183>:	lea    -0x30(%ebp),%edx
   0x08048e52 <+186>:	mov    (%edx,%edi,4),%eax
   0x08048e55 <+189>:	mov    %eax,0x8(%esi)
   0x08048e58 <+192>:	mov    %eax,%esi
   0x08048e5a <+194>:	inc    %edi
   0x08048e5b <+195>:	cmp    $0x5,%edi
   0x08048e5e <+198>:	jle    0x8048e52 <phase_6+186>
   0x08048e60 <+200>:	movl   $0x0,0x8(%esi)
   0x08048e67 <+207>:	mov    -0x34(%ebp),%esi
   0x08048e6a <+210>:	xor    %edi,%edi
   0x08048e6c <+212>:	lea    0x0(%esi,%eiz,1),%esi
   0x08048e70 <+216>:	mov    0x8(%esi),%edx
   0x08048e73 <+219>:	mov    (%esi),%eax
   0x08048e75 <+221>:	cmp    (%edx),%eax
   0x08048e77 <+223>:	jge    0x8048e7e <phase_6+230>
   0x08048e79 <+225>:	call   0x80494fc <explode_bomb>
   0x08048e7e <+230>:	mov    0x8(%esi),%esi
   0x08048e81 <+233>:	inc    %edi
   0x08048e82 <+234>:	cmp    $0x4,%edi
   0x08048e85 <+237>:	jle    0x8048e70 <phase_6+216>
   0x08048e87 <+239>:	lea    -0x58(%ebp),%esp
   0x08048e8a <+242>:	pop    %ebx
   0x08048e8b <+243>:	pop    %esi
   0x08048e8c <+244>:	pop    %edi
   0x08048e8d <+245>:	mov    %ebp,%esp
   0x08048e8f <+247>:	pop    %ebp
   0x08048e90 <+248>:	ret
```

Ce code ASM représente l'intégralité des six phases du programme ainsi que la fonction principale `main`. Chaque phase correspond à une fonction distincte qui est appelée successivement dans le flux d'exécution de `main`.

---