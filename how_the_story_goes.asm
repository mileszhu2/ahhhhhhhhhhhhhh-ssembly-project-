.data
length_of_16th: .word 50 # time length of a 16th note in miliseconds
guitar_index: .word 0
guitar_note: .word 0
guitar_save_location: .word 0
guitar_loop_counter: .word -1234567
voice_index: .word 0
voice_note: .word 0
voice_save_location: .word 0
voice_loop_counter: .word -1234567
bass_index: .word 0
bass_note: .word 0
bass_save_location: .word 0
bass_loop_counter: .word -1234567

guitar: .word 1500
        .word -1
        .word 354, 359, 362, 359, 355, 359, 362, 359
        .word -7
        .word 354, 357, 362, 357, 352, 357, 361, 357
        .word -1
        .word 354, 359, 362, 359, 355, 359, 362, 359, 354, 359, 362, 359, 355, 359, 362, 359, 354, 359, 362, 359, 355, 359, 362, 359, 354, 357, 362, 357, 352, 357, 361, 357
        .word -2
        .word 354, 359, 362, 359, 355, 359, 362, 359, 354, 357, 362, 357, 352, 357, 361, 357
        .word -8
        .word 1500, 1500, 1500, 1500
        .word -1
        .word 354, 359, 362, 359, 355, 359, 362, 359, 354, 357, 362, 357, 352, 357, 361, 357
        .word -3
        .word 354, 359, 362, 359, 355, 359, 362, 359
        .word -3
        .word 354, 357, 362, 357, 352, 357, 361, 357
        .word -1
        .word 354, 359, 362, 359, 355, 359, 362, 359, 354, 357, 362, 357, 352, 357, 361, 357
        .word -10
        .word 300
        .word 1500
        .word 1500
        .word -1
        .word -1234567
       
voice: .word 1500
       .word -1 
       .word 1500, 300, 371, 371, 371, 369, 366, 766, 364, 364, 362, 364, 766, 300, 364, 366, 366, 362, 364, 366, 100, 562, 364, 366, 100, 562, 364, 766
       .word 700, 366, 366, 362, 364, 366, 366, 362, 364, 366, 100, 562, 364, 1166, 300, 366, 366, 362, 364, 366, 366, 362, 364, 366, 100, 562, 364, 362
       .word -1
       .word 1500, 371, 371, 171, 569, 369, 369, 369, 369, 362, 362, 164, 766, 100, 1100, 366, 366, 166, 564, 364, 364, 364, 364, 366, 364, 362, 759, 1100
       .word 371, 371, 371, 171, 169, 769, 374, 374, 362, 362, 364, 766, 1500, 366, 166, 566, 364, 364, 364, 364, 366, 364, 362, 359
       .word -1
       .word 300, 1500, 371, 1169, 371, 1169, 367, 1166, 1100, 359, 366, 1164, 366, 1164, 362, 1166, 1500, 371, 1169, 371, 1169, 367, 1166, 300, 367, 369
       .word 374, 378, 1176, 378, 1176, 374, 771
       .word -1
       .word 1500, 371, 371, 371, 369, 366, 766, 364, 364, 362, 364, 766, 300, 364, 366, 366, 362, 364, 366, 100, 562, 364, 366, 100, 562, 364, 766, 700, 366
       .word 366, 362, 364, 366, 366, 362, 364, 366, 100, 562, 364, 1166, 300, 366, 366, 362, 364, 366, 366, 362, 364, 366, 100, 562, 364, 362
       .word -1
       .word 300, 371, 371, 371, 300, 369, 369, 369, 300, 374, 374, 374, 300, 362, 364, 366, 300, 366, 366, 367, 366, 366, 366, 764, 364, 364, 364, 366, 364, 162, 559
       .word 1500, 371, 371, 171, 571, 369, 369, 374, 374, 362, 362, 364, 766, 1100, 366, 366, 166, 567, 366, 364, 364, 364, 366, 364, 162, 559
       .word -1
       .word 300, 1500, 371, 1169, 371, 1169, 367, 1166, 1100, 359, 366, 1164, 366, 1164, 362, 1166, 1500, 371, 1169, 371, 1169, 367, 1166, 300, 367, 369
       .word 374, 378, 1176, 378, 1176, 374, 771
       .word -1
       .word 1500, 371, 371, 371, 369, 366, 766, 364, 364, 362, 364, 766, 300, 364, 366, 366, 362, 364, 366, 100, 562, 364, 366, 100, 562, 364, 766, 700, 366
       .word 366, 362, 364, 366, 366, 362, 364, 366, 100, 562, 364, 1166, 300, 366, 366, 362, 364, 366, 366, 362, 364, 366, 100, 562, 364, 362
       .word -1
       .word 300, 1500, 371, 1169, 371, 1169, 367, 1166, 1100, 359, 366, 1164, 366, 1164, 362, 1166, 1500, 371, 1169, 371, 1169, 367, 1166, 300, 367, 369
       .word 374, 378, 1176, 378, 1176, 374, 771
       .word 1500
       .word 1500
       .word -1
       .word -1234567

bass: .word 1500
      .word -1
      .word 1535, 1531
      .word -7
      .word 1538, 1533
      .word -1
      .word 1535, 1131, 300, 1500, 1531, 1535, 1531, 1526, 1533, 1535, 1531, 1135, 300, 1531, 1535, 1531, 1526, 1533
      .word -1
      .word 1535, 1531, 1538, 1533
      .word -8
      .word 735, 700, 731, 700, 726, 700, 733, 700, 1535, 1531, 1526, 1533, 1535, 1531, 1538, 1533, 1535, 1531, 1526, 1533
      .word -1
      .word 735, 735, 731, 731
      .word -3
      .word 726, 726, 733, 733
      .word -1
      .word 735, 735, 731, 731, 726, 726, 733, 733
      .word 335, 335, 335, 335, 331, 331, 331, 331, 338, 338, 338, 338, 333, 333, 333, 321
      .word -1
      .word -1
      .word 323, 323, 323, 323, 331, 331, 331, 331, 326, 326, 326, 326, 333, 333, 333, 333
      .word 323, 323, 323, 323, 331, 331, 331, 331, 338, 338, 338, 338, 333, 333, 333, 333
      .word -1
      .word 1523, 1531, 1526, 1533, 1523, 1531, 1538, 1533
      .word -1
      .word 1535, 1531, 1538, 1533
      .word -2
      .word 735, 735, 731, 731, 726, 726, 733, 733
      .word 335, 335, 335, 335, 331, 331, 331, 331, 326, 326, 326, 326, 721, 700, 335
      .word 1500
      .word 1500
      .word -1
      .word -1234567

.text
.globl main
main:
    # guitar
    la $t1, guitar
    sw $t1, guitar_index
    sw $t1, guitar_save_location
    lw $t1, guitar_index
    lw $t2, 0($t1)
    sw $t2, guitar_note
    
    # voice
    la $t1, voice
    sw $t1, voice_index
    sw $t1, voice_save_location
    lw $t1, voice_index
    lw $t2, 0($t1)
    sw $t2, voice_note
    
    # bass
    la $t1, bass
    sw $t1, bass_index
    sw $t1, bass_save_location
    lw $t1, bass_index
    lw $t2, 0($t1)
    sw $t2, bass_note
    
    music_loop:
    li $v0, 31 # to play note
    # note: pitch=$a0  dur=$a1  inst=$a2  vol=$a3
    
    # guitar
    la $t1, guitar_index
    lw $t2, guitar_note
    la $s3, guitar_note
    la $s4, guitar_save_location
    la $t4, guitar_loop_counter
    li $a2, 90 # guitar
    li $a3, 35 # how loud is the guitar??
    jal read_note
 
    # voice
    la $t1, voice_index
    lw $t2, voice_note
    la $s3, voice_note
    la $s4, voice_save_location
    la $t4, voice_loop_counter
    li $a2, 87 # piano
    li $a3, 25 # how loud is the piano??
    jal read_note
    
    # bass
    la $t1, bass_index
    lw $t2, bass_note
    la $s3, bass_note
    la $s4, bass_save_location
    la $t4, bass_loop_counter
    li $a2, 33 # bass
    li $a3, 85 # how loud is the bass??
    jal read_note
    
    # sleep 50 ms (16th note)
    li $v0, 32
    lw $a0, length_of_16th
    syscall
    j music_loop


read_note:
    # params: 
    # $t1 for the array to read
    # $t2 is the note to play
    # $s3 the save note address (ex. guitar_note address) 
    # $s4 is the location to jump to (for reset_music)
    # $t4 is to count loops
    addi $sp, $sp, -4
    sw $ra, 0($sp)
    
    play_note:
    beq $t2, -1234567, main
    blt $t2, 1500, no_whole_note
    jal play_whole_note
    j end_note
    no_whole_note:
    blt $t2, 700, no_half_note
    bge $t2, 1200, no_play
    blt $t2, 1100, half_note
    jal play_dotted_half_note
    j end_note
    half_note:
    bge $t2, 800, no_play
    jal play_half_note
    j end_note
    no_half_note:
    blt $t2, 300, no_quarter_note
    bge $t2, 600, no_play
    blt $t2, 500, quarter_note
    jal play_dotted_quarter_note
    j end_note
    quarter_note:
    bge $t2, 400, no_play
    jal play_quarter_note
    j end_note
    no_quarter_note:
    blt $t2, 100, no_eighth_note
    bge $t2, 200, dotted_eighth_note
    jal play_eighth_note
    j end_note
    dotted_eighth_note:
    jal play_dotted_eighth_note
    j end_note
    no_eighth_note:
    blt $t2, 0, reset_music
    jal play_sixteenth_note
    j end_note
   
    no_play:
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
   
    end_note:
    lw $ra, 0($sp)
    addi $sp, $sp, 4
    jr $ra
    
    reset_music:
    # get the loop_counter
    lw $t3, 0($t4)
    bgt $t2, $t3, update_loop_counter
    j loop_counter_else
    update_loop_counter:
    sw $t2, 0($t4) # update loop_counter
    move $t3, $t2
    loop_counter_else:
    beq $t3, -1, go_next
    add $t3, $t3, 1
    sw $t3, 0($t4) # store the changed $t3
    lw $s4, 0($s4) # get the loop destination
    sw $s4, 0($t1) # store the new destination
    lw $t2, 0($s4) # next note
    sw $t2, 0($s3) # store it
    j play_note # on the next one it should NOT be another reset
    
    go_next:
    # reset loop_counter
    li $t3, -1234567
    sw $t3, 0($t4)
    # get the array address
    lw $t3, 0($t1)
    addi $t3, $t3, 4
    sw $t3, 0($s4) # set as new loop destination
    sw $t3, 0($t1)
    lw $t2, 0($t3) # next note
    sw $t2, 0($s3) # store it
    j play_note
    
 
 play_whole_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 1500
    beq $a0, 0, skip_whole # don't syscall if nothing to play
    lw $a1, length_of_16th 
    sll $a1, $a1, 4 # duration 16 times of length_of_16th
    syscall
    
    skip_whole:
    # update $t2
    sub $t2, $t2, $a0 # just 1500 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra   
    
 play_dotted_half_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 1100
    beq $a0, 0, skip_dottedh # don't syscall if nothing to play
    lw $a1, length_of_16th 
    sll $t3, $a1, 2
    sll $a1, $a1, 3 
    add $a1, $a1, $t3 # duration 12 times of length_of_16th
    syscall
    
    skip_dottedh:
    # update $t2
    sub $t2, $t2, $a0 # just 1100 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra   
    
 play_half_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 700
    beq $a0, 0, skip_half # don't syscall if nothing to play
    lw $a1, length_of_16th 
    sll $a1, $a1, 3 # duration 8 times of length_of_16th
    syscall
    
    skip_half:
    # update $t2
    sub $t2, $t2, $a0 # just 700 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra   
    
 play_dotted_quarter_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 500
    beq $a0, 0, skip_dottedq # don't syscall if nothing to play
    lw $a1, length_of_16th 
    sll $t3, $a1, 1
    sll $a1, $a1, 2 
    add $a1, $a1, $t3 # duration 6 times of length_of_16th
    syscall
    
    skip_dottedq:
    # update $t2
    sub $t2, $t2, $a0 # just 500 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra   
    
play_quarter_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 300
    beq $a0, 0, skip_quarter # don't syscall if nothing to play
    lw $a1, length_of_16th 
    sll $a1, $a1, 2 # duration 4 times of length_of_16th
    syscall
    
    skip_quarter:
    # update $t2
    sub $t2, $t2, $a0 # just 300 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra
    
play_dotted_eighth_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 200
    beq $a0, 0, skip_dottede # don't syscall if nothing to play
    lw $a1, length_of_16th
    add $t3, $a1, $a1
    add $a1, $a1, $t3 # duration 3 times of length_of_16th
    syscall
    
    skip_dottede:
    # update $t2
    sub $t2, $t2, $a0 # just 200 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra

play_eighth_note:
    # $t2 as param (note in question)
    
    # play the note
    sub $a0, $t2, 100
    beq $a0, 0, skip_eighth # don't syscall if nothing to play
    lw $a1, length_of_16th
    sll $a1, $a1, 1 # duration 2 times of length_of_16th
    syscall
    
    skip_eighth:
    # update $t2
    sub $t2, $t2, $a0 # just 100 now
    sub $t2, $t2, 100
    sw $t2, 0($s3) # store it
    
    jr $ra

play_sixteenth_note:
    # $t1 is the array address (current index)
    # $t2 as param (note in question)
    
    # play the note
    move $a0, $t2
    beq $a0, 0, skip_sixteenth # don't syscall if nothing to play
    lw $a1, length_of_16th # duration 1 time of length_of_16th
    syscall
    
    skip_sixteenth:
    # increment and load the next note
    # get the array address
    lw $t3, 0($t1)
    addi $t3, $t3, 4
    sw $t3, 0($t1)
    lw $t2, 0($t3) # next note 
    sw $t2, 0($s3) # store it
    
    jr $ra