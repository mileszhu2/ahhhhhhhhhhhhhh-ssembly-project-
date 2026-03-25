################# CSC258 Assembly Final Project ###################
# This file contains our implementation of Columns.
#
# Student 1: Name, Student Number
# Student 2: Name, Student Number (if applicable)
#
# We assert that the code submitted here is entirely our own 
# creation, and will indicate otherwise when it is not.
#
######################## Bitmap Display Configuration ########################
# - Unit width in pixels:       8
# - Unit height in pixels:      8
# - Display width in pixels:    256
# - Display height in pixels:   256
# - Base Address for Display:   0x10008000 ($gp)
##############################################################################

    .data
##############################################################################
# Immutable Data
##############################################################################
# The address of the bitmap display. Don't forget to connect it!
ADDR_DSPL:
    .word 0x10008000
# The address of the keyboard. Don't forget to connect it!
ADDR_KBRD:
    .word 0xffff0000
    
colors: .word 0x00ff0000 # red
        .word 0x0000ff00 # green
        .word 0x000000ff # blue
        .word 0x00ffff00 # yellow
        .word 0x00ff00ff # magenta
        .word 0x0000ffff # cyan

##############################################################################
# Mutable Data
##############################################################################
column: .word 0:3
next_column: .word 0:3
current_pos: .word 0x10008004 # position logs the block on top of the column's top block
previous_pos: .word 0x10008004
col_hitbox: .word 0x10008184 # the bottom block of the column

##############################################################################
# Code
##############################################################################
	.text
	.globl main

    # Run the game.
main:
    # Initialize the game
    li $t9, 0x808080 #t9=gray
    lw $t0, ADDR_DSPL # $t0 = base address for display
    
    # Initialize the input values for the line drawing code.
    addi $a0, $zero, 0          # set the X coordinate to 0
    addi $a1, $zero, 0          # set the Y coordinate to 0
    addi $a2, $zero, 16         # set the length of the line to 16
    jal vline_draw              # calls the line drawing function
    
    addi $a0, $zero, 7          # set the X coordinate to 7
    addi $a1, $zero, 0          # set the Y coordinate to 0
    addi $a2, $zero, 16         # set the length of the line to 16
    jal vline_draw              # calls the line drawing function
    
    addi $a0, $zero, 9          # set the X coordinate to 9
    addi $a1, $zero, 0          # set the Y coordinate to 0
    addi $a2, $zero, 5          # set the length of the line to 5
    jal vline_draw              # calls the line drawing function
    
    addi $a0, $zero, 7          # set the X coordinate to 7
    addi $a1, $zero, 4          # set the Y coordinate to 4
    addi $a2, $zero, 3          # set the length of the line to 3
    jal hline_draw              # calls the line drawing function
    
    addi $a0, $zero, 0          # set the X coordinate to 0
    addi $a1, $zero, 0          # set the Y coordinate to 0
    addi $a2, $zero, 10         # set the length of the line to 10
    jal hline_draw              # calls the line drawing function
    
    addi $a0, $zero, 0          # set the X coordinate to 0
    addi $a1, $zero, 15         # set the Y coordinate to 15
    addi $a2, $zero, 8          # set the length of the line to 8
    jal hline_draw              # calls the line drawing function
    
    # Start the game
    jal get_random_column
    jal game_loop
    li $v0, 10                      # terminate the program gracefully
    syscall
    
    ###
    ###  Code for drawing a horizontal/vertical line.
    ###
    ###  $t0 = location of the top-left corner of the bitmap
    ###  $a0 = the X coordinate of the start of the line
    ###  $a1 = the Y coordinate of the start of the line
    ###  $a2 = the length of the line
    ###  $t1 = the horizontal offset to add to $t0
    ###  $t2 = the vertical offset to add to $t0
    ###  $t3 = the current location in memory of the pixel to draw
    ###  $t4 = the location of the last pixel in the line
    
    hline_draw:
    sll $t2, $a1, 7                 # Calculate the vertical offset (multiply Y input by 128)
    sll $t1, $a0, 2                 # Calculate the horizontal offset (multiply X input by 4)
    add $t3, $t0, $t2               # Add the vertical offset to $t0
    add $t3, $t3, $t1               # Add the horizontal offset to the location calculated above
    
    sll $a2, $a2, 2                 # Calculate the offset from $t3 for the last pixel in the line (multiply $a2 by 4)
    add $t4, $t3, $a2               # Calculate the position of the last pixel in the line
    # start of the line-drawing loop
    hline_loop:
    beq $t3, $t4, hline_loop_end    # If the current X and Y match the end location of the line, branch out of the loop.
    sw $t9, 0($t3)                  # Draw a single gray pixel at the current X and Y
    addi $t3, $t3, 4                # Move to the next pixel in the row
    j hline_loop                    # Jump to the start of the loop
    hline_loop_end:
    jr $ra                          # return statement
    
    vline_draw:
    sll $t2, $a1, 7                 # Calculate the vertical offset (multiply Y input by 128)
    sll $t1, $a0, 2                 # Calculate the horizontal offset (multiply X input by 4)
    add $t3, $t0, $t2               # Add the vertical offset to $t0
    add $t3, $t3, $t1               # Add the horizontal offset to the location calculated above
    
    sll $a2, $a2, 7                 # Calculate the offset from $t3 for the last pixel in the line (multiply $a2 by 128)
    add $t4, $t3, $a2               # Calculate the position of the last pixel in the line
    # start of the line-drawing loop
    vline_loop:
    beq $t3, $t4, hline_loop_end    # If the current X and Y match the end location of the line, branch out of the loop.
    sw $t9, 0($t3)                  # Draw a single gray pixel at the current X and Y
    addi $t3, $t3, 128              # Move to the next pixel in the column
    j vline_loop                    # Jump to the start of the loop
    vline_loop_end:
    jr $ra                          # return statement

game_loop:
    # TODO check if should end the game
    # New column turn setup
    sw $ra, 0($sp)
    la $t3, current_pos
    li $t1, 0x10008004
    sw $t1, 0($t3) # reset current_pos to top-left of playing map
    jal transfer_next_to_col
    jal spawn_column # Spawn previously generated column
    jal get_random_column # Generate next column and display
    la $s0, column
    # Check if key has been pressed
    key_loop:
	li $v0, 32
	li $a0, 1
	syscall

    lw $t0, ADDR_KBRD               # $t0 = base address for keyboard
    lw $t8, 0($t0)                  # Load first word from keyboard
    beq $t8, 1, keyboard_input      # If first word 1, key is pressed
    b key_loop

    # Check which key has been pressed
    keyboard_input:                     # A key is pressed
        lw $a0, 4($t0)                  # Load second word from keyboard
        beq $a0, 0x71, respond_to_Q     # Check if the key q was pressed
        beq $a0, 0x77, respond_to_W     # Check if the key w was pressed
        beq $a0, 0x61, respond_to_A     # Check if the key a was pressed
        beq $a0, 0x73, respond_to_S     # Check if the key s was pressed
        beq $a0, 0x64, respond_to_D     # Check if the key d was pressed
        li $v0, 1                       # ask system to print $a0
        syscall
        b key_loop
    
    respond_to_Q:
    	li $v0, 10                      # Quit gracefully
    	syscall
    	
    respond_to_W:
    	li $t1, 0
        li $t2, 3
        lw $t4, 8($s0)
        swap_loop:
        beq $t1, $t2, swap_end
        sll $t6, $t1, 2
        add $t5, $s0, $t6
        lw $a0, 0($t5)
        sw $t4, 0($t5)
        move $t4, $a0
        addi $t1, $t1, 1
        j swap_loop
        swap_end:
        jal spawn_column
        j key_loop
        
    respond_to_A:
    	lw $t1, current_pos # param for collision_checker
    	lw $t2, col_hitbox # param for collision_checker
    	li $a0, -4 # offset to move left (param for collision_checker)
    	jal collision_checker # check collision and update location if applicable
    	beq $a1, 1, detected
    	detected:
    	j key_loop
    respond_to_S:
    	li $v0, 10                      # Quit gracefully
    	syscall
    respond_to_D:
    	lw $t1, current_pos # param for collision_checker
    	lw $t2, col_hitbox # param for collision_checker
    	li $a0, 4 # offset to move right (param for collision_checker)
    	jal collision_checker # check collision and update location if applicable
    	beq $a1, 1, detected
    	
    
    # 2a. Check for collisions
	# 2b. Update locations (capsules)
	# 3. Draw the screen
	# 4. Sleep

    # 5. Go back to Step 1
    j game_loop
    end_game:
    lw $ra, 0($sp) # Assuming that after every cycle in the game loop that $sp points to where it originally pointed to
    jr $ra

get_random_column:
    # Random seed (system time)
    # li $v0, 30 
    # syscall # gets system time $a0 = low 32 bits, $a1 = high 32 bits
    # move $a1, $a0       # Move low 32 bits of time into $a1 (the seed)
    # li $a0, 0           # Set Generator ID to 0
    # li $v0, 40          # Syscall 40: Set Seed
    # syscall

    # Generate color combo
    la $s0, next_column
    la $t9, colors
    addi $t6, $t0, 160
    li $t1, 0
    li $t2, 3
    li $v0, 42
    li $a1, 6
    generate_loop:
    beq $t1, $t2, generate_end
    li $a0, 0
    syscall # number in $a0
    move $t3, $a0
    sll $t3, $t3, 2 # multiply by 4 (offset)
    add $t4, $t9, $t3 # store the index in $t4 (index)
    lw $t3, 0($t4) # load the index value of colors and store in $t3
    sll $t5, $t1, 2 # multiply by 4 (offset)
    add $t4, $s0, $t5 # store the index in $t4 (index)
    sw $t3, 0($t4) # store the color in $t3 to the index in column
    sw $t3, 0($t6) # display on bitmap
    addi $t6, $t6, 128 
    addi $t1, $t1, 1
    j generate_loop
    generate_end:
    jr $ra                          # return statement
    
spawn_column:
    la $s0, column
    li $a0, 0x00000000 # black
    li $t1, 0
    li $t2, 3
    lw $t3, current_pos
    lw $t7, previous_pos
    spawn_loop:
    beq $t1, $t2, spawn_end
    sll $t6, $t1, 2
    add $t5, $s0, $t6 # color index in colors
    lw $t4, 0($t5) # get the color
    addi $t3, $t3, 128 # color in position
    addi $t7, $t7, 128 # color out position
    sw $a0, 0($t7) # color out
    sw $t4, 0($t3) # color in
    addi $t1, $t1, 1 # increment
    j spawn_loop
    spawn_end:
    lw $t3, current_pos
    jr $ra
    
transfer_next_to_col:
    la $t1, next_column
    la $t2, column
    
    # Copy all 3 elements without loop
    lw $t3, 0($t1)
    sw $t3, 0($t2)
    
    lw $t3, 4($t1)
    sw $t3, 4($t2)
    
    lw $t3, 8($t1)
    sw $t3, 8($t2)
    jr $ra
    
collision_checker: 
# Parameters:
# $t1 is the current_pos of the column
# $t2 is the col_hitbox (used to check collision)
# $a0 to determine whether the intended move is left or right
    li $a1, 0 # black
    add $t3, $t2, $a0 # location to the right or left of the hitbox
    lw $t5, 0($t3) # color right or left of hitbox
    beq $t5, $a1, no_collision
    li $a1, 1 # to indicate collision
    jr $ra
    no_collision:
    addi $sp, $sp, -4
    sw $ra, 0($sp)
    la $t2 current_pos
    add $t1, $t1, $a0
    sw $t1, 0($t2) # update current_pos for spawn_column
    jal spawn_column
    lw $ra, 0($sp)
    addi $sp, $sp, 4