.data
displayaddress:     .word       0x10008000

colors: 
.word 0x00ffffca
.word 0x00ffffcb
.word 0x00ffffcc
.word 0x00ffffcd
.word 0x00ffffce
.word 0x00ffffcf

# ...

.text
lw $t0, displayaddress
la $t9, colors
lw $t1, 0($t9)
sw $t1, 0($t0)
lw $t1, 4($t9)
sw $t1, 4($t0)
lw $t1, 8($t9)
sw $t1, 8($t0)
lw $t1, 12($t9)
sw $t1, 12($t0)
lw $t1, 16($t9)
sw $t1, 16($t0)
lw $t1, 20($t9)
sw $t1, 20($t0)