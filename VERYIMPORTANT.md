# **PLEASE READ BEFORE CODING IN COLUMNS.ASM !!!!!!!!**
- Bits: 256x256 (for bitmap)
- Unit: 8x8 (for bitmap)
- Display and keyboard address and the ***colors*** array are IMMUTABLE. At no point in the code should their values be modified.
- We go by bytes, so multiply any index by 4. This will be a logical left shift (sll) of 2.
- $t0 reserved for ***display address*** and is set in `main` when the game is initialized, so TREAT AS IF IT IS IMMUTABLE.
- $s0 reserved for the address of index 0 of ***next_column*** after `get_random_column` is called. Treat the same as you should to $t0 (DO NOT CHANGE).
- $s1 reserved for the address of index 0 of ***column*** which is the current column. Treat same as above.
- $s2 reserved for the ***keyboard address*** which is IMMUTABLE.
- If you want to use the address of $t0 or any other I mentioned above and modify it later on, use (WLG/you can use any t register expect $t0)
  ``` assembly
  add $t1, $t0, $zero
  ```
- Aside from the `main` method, values (ex. $v0, $a1) should not be used to store variables due to `syscall`. Instead, use temporary (ex. $t1, $t2).
- BE VERY CAREFUL WHEN USING $sp because we need that to end the game
