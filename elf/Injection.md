# .so injection

# build/lua_test_32_clang_o0
## readelf
```plain
ELF Header:
  Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF32
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Intel 80386
  Version:                           0x1
  Entry point address:               0x730
  Start of program headers:          52 (bytes into file)
  Start of section headers:          7648 (bytes into file)
  Flags:                             0x0
  Size of this header:               52 (bytes)
  Size of program headers:           32 (bytes)
  Number of program headers:         9
  Size of section headers:           40 (bytes)
  Number of section headers:         36
  Section header string table index: 35

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] .interp           PROGBITS        00000154 000154 000013 00   A  0   0  1
  [ 2] .note.ABI-tag     NOTE            00000168 000168 000020 00   A  0   0  4
  [ 3] .hash             HASH            00000188 000188 0000ac 04   A  4   0  4
  [ 4] .dynsym           DYNSYM          00000234 000234 000180 10   A  5   1  4
  [ 5] .dynstr           STRTAB          000003b4 0003b4 000162 00   A  0   0  1
  [ 6] .gnu.version      VERSYM          00000516 000516 000030 02   A  4   0  2
  [ 7] .gnu.version_r    VERNEED         00000548 000548 000040 00   A  5   1  4
  [ 8] .rel.dyn          REL             00000588 000588 000050 08   A  4   0  4
  [ 9] .rel.plt          REL             000005d8 0005d8 000058 08  AI  4  22  4
  [10] .init             PROGBITS        00000630 000630 000023 00  AX  0   0  4
  [11] .plt              PROGBITS        00000660 000660 0000c0 04  AX  0   0 16
  [12] .plt.got          PROGBITS        00000720 000720 000008 08  AX  0   0  8
  [13] .text             PROGBITS        00000730 000730 0003b2 00  AX  0   0 16
  [14] .fini             PROGBITS        00000ae4 000ae4 000014 00  AX  0   0  4
  [15] .rodata           PROGBITS        00000af8 000af8 00000c 00   A  0   0  4
  [16] .eh_frame_hdr     PROGBITS        00000b04 000b04 000034 00   A  0   0  4
  [17] .eh_frame         PROGBITS        00000b38 000b38 0000d4 00   A  0   0  4
  [18] .init_array       INIT_ARRAY      00001edc 000edc 000004 04  WA  0   0  4
  [19] .fini_array       FINI_ARRAY      00001ee0 000ee0 000004 04  WA  0   0  4
  [20] .dynamic          DYNAMIC         00001ee4 000ee4 000100 08  WA  5   0  4
  [21] .got              PROGBITS        00001fe4 000fe4 00001c 04  WA  0   0  4
  [22] .got.plt          PROGBITS        00002000 001000 000038 04  WA  0   0  4
  [23] .data             PROGBITS        00002038 001038 000008 00  WA  0   0  4
  [24] .bss              NOBITS          00002040 001040 000004 00  WA  0   0  1
  [25] .comment          PROGBITS        00000000 001040 000061 01  MS  0   0  1
  [26] .debug_pubnames   PROGBITS        00000000 0010a1 00001b 00      0   0  1
  [27] .debug_info       PROGBITS        00000000 0010bc 0000a1 00      0   0  1
  [28] .debug_abbrev     PROGBITS        00000000 00115d 00007e 00      0   0  1
  [29] .debug_line       PROGBITS        00000000 0011db 000109 00      0   0  1
  [30] .debug_str        PROGBITS        00000000 0012e4 00008f 01  MS  0   0  1
  [31] .debug_macinfo    PROGBITS        00000000 001373 000001 00      0   0  1
  [32] .debug_pubtypes   PROGBITS        00000000 001374 000031 00      0   0  1
  [33] .symtab           SYMTAB          00000000 0013a8 000600 10     34  62  4
  [34] .strtab           STRTAB          00000000 0019a8 0002ea 00      0   0  1
  [35] .shstrtab         STRTAB          00000000 001c92 00014e 00      0   0  1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset   VirtAddr   PhysAddr   FileSiz MemSiz  Flg Align
  PHDR           0x000034 0x00000034 0x00000034 0x00120 0x00120 R E 0x4
  INTERP         0x000154 0x00000154 0x00000154 0x00013 0x00013 R   0x1
      [Requesting program interpreter: /lib/ld-linux.so.2]
  LOAD           0x000000 0x00000000 0x00000000 0x00c0c 0x00c0c R E 0x1000
  LOAD           0x000edc 0x00001edc 0x00001edc 0x00164 0x00168 RW  0x1000
  DYNAMIC        0x000ee4 0x00001ee4 0x00001ee4 0x00100 0x00100 RW  0x4
  NOTE           0x000168 0x00000168 0x00000168 0x00020 0x00020 R   0x4
  GNU_EH_FRAME   0x000b04 0x00000b04 0x00000b04 0x00034 0x00034 R   0x4
  GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RW  0x10
  GNU_RELRO      0x000edc 0x00001edc 0x00001edc 0x00124 0x00124 R   0x1

 Section to Segment mapping:
  Segment Sections...
   00
   01     .interp
   02     .interp .note.ABI-tag .hash .dynsym .dynstr .gnu.version .gnu.version_r .rel.dyn .rel.plt .init .plt .plt.got .text .fini .rodata .eh_frame_hdr .eh_frame
   03     .init_array .fini_array .dynamic .got .got.plt .data .bss
   04     .dynamic
   05     .note.ABI-tag
   06     .eh_frame_hdr
   07
   08     .init_array .fini_array .dynamic .got

Dynamic section at offset 0xee4 contains 28 entries:
  Tag        Type                         Name/Value
 0x00000001 (NEEDED)                     Shared library: [liblua.so.5.3]
 0x00000001 (NEEDED)                     Shared library: [libm.so.6]
 0x00000001 (NEEDED)                     Shared library: [libc.so.6]
 0x0000000c (INIT)                       0x630
 0x0000000d (FINI)                       0xae4
 0x00000019 (INIT_ARRAY)                 0x1edc
 0x0000001b (INIT_ARRAYSZ)               4 (bytes)
 0x0000001a (FINI_ARRAY)                 0x1ee0
 0x0000001c (FINI_ARRAYSZ)               4 (bytes)
 0x00000004 (HASH)                       0x188
 0x00000005 (STRTAB)                     0x3b4
 0x00000006 (SYMTAB)                     0x234
 0x0000000a (STRSZ)                      354 (bytes)
 0x0000000b (SYMENT)                     16 (bytes)
 0x00000015 (DEBUG)                      0x0
 0x00000003 (PLTGOT)                     0x2000
 0x00000002 (PLTRELSZ)                   88 (bytes)
 0x00000014 (PLTREL)                     REL
 0x00000017 (JMPREL)                     0x5d8
 0x00000011 (REL)                        0x588
 0x00000012 (RELSZ)                      80 (bytes)
 0x00000013 (RELENT)                     8 (bytes)
 0x6ffffffb (FLAGS_1)                    Flags: PIE
 0x6ffffffe (VERNEED)                    0x548
 0x6fffffff (VERNEEDNUM)                 1
 0x6ffffff0 (VERSYM)                     0x516
 0x6ffffffa (RELCOUNT)                   4
 0x00000000 (NULL)                       0x0

Relocation section '.rel.dyn' at offset 0x588 contains 10 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
00001edc  00000008 R_386_RELATIVE
00001ee0  00000008 R_386_RELATIVE
00001ff8  00000008 R_386_RELATIVE
0000203c  00000008 R_386_RELATIVE
00001fe4  00000206 R_386_GLOB_DAT    00000000   _ITM_deregisterTMClone
00001fe8  00000306 R_386_GLOB_DAT    00000000   stderr@GLIBC_2.0
00001fec  00000b06 R_386_GLOB_DAT    00000000   __cxa_finalize@GLIBC_2.1.3
00001ff0  00000d06 R_386_GLOB_DAT    00000000   __gmon_start__
00001ff4  00001106 R_386_GLOB_DAT    00000000   stdin@GLIBC_2.0
00001ffc  00001506 R_386_GLOB_DAT    00000000   _ITM_registerTMCloneTa

Relocation section '.rel.plt' at offset 0x5d8 contains 11 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
0000200c  00000107 R_386_JUMP_SLOT   00000000   lua_settop
00002010  00000407 R_386_JUMP_SLOT   00000000   lua_close
00002014  00000507 R_386_JUMP_SLOT   00000000   fgets@GLIBC_2.0
00002018  00000607 R_386_JUMP_SLOT   00000000   lua_tolstring
0000201c  00000907 R_386_JUMP_SLOT   00000000   __stack_chk_fail@GLIBC_2.4
00002020  00000a07 R_386_JUMP_SLOT   00000000   luaL_openlibs
00002024  00000c07 R_386_JUMP_SLOT   00000000   luaL_newstate
00002028  00000f07 R_386_JUMP_SLOT   00000000   __libc_start_main@GLIBC_2.0
0000202c  00001007 R_386_JUMP_SLOT   00000000   fprintf@GLIBC_2.0
00002030  00001407 R_386_JUMP_SLOT   00000000   luaL_loadstring
00002034  00001707 R_386_JUMP_SLOT   00000000   lua_pcallk

The decoding of unwind sections for machine type Intel 80386 is not currently supported.

Symbol table '.dynsym' contains 24 entries:
   Num:    Value  Size Type    Bind   Vis      Ndx Name
     0: 00000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_settop
     2: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
     3: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stderr@GLIBC_2.0 (2)
     4: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_close
     5: 00000000     0 FUNC    GLOBAL DEFAULT  UND fgets@GLIBC_2.0 (2)
     6: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_tolstring
     7: 00002040     0 NOTYPE  GLOBAL DEFAULT   23 _edata
     8: 00000ae4     0 FUNC    GLOBAL DEFAULT   14 _fini
     9: 00000000     0 FUNC    GLOBAL DEFAULT  UND __stack_chk_fail@GLIBC_2.4 (3)
    10: 00000000     0 FUNC    GLOBAL DEFAULT  UND luaL_openlibs
    11: 00000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@GLIBC_2.1.3 (4)
    12: 00000000     0 FUNC    GLOBAL DEFAULT  UND luaL_newstate
    13: 00000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    14: 00000afc     4 OBJECT  GLOBAL DEFAULT   15 _IO_stdin_used
    15: 00000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.0 (2)
    16: 00000000     0 FUNC    GLOBAL DEFAULT  UND fprintf@GLIBC_2.0 (2)
    17: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stdin@GLIBC_2.0 (2)
    18: 00002044     0 NOTYPE  GLOBAL DEFAULT   24 _end
    19: 00002040     0 NOTYPE  GLOBAL DEFAULT   24 __bss_start
    20: 00000000     0 FUNC    GLOBAL DEFAULT  UND luaL_loadstring
    21: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    22: 00000630     0 FUNC    GLOBAL DEFAULT   10 _init
    23: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_pcallk

Symbol table '.symtab' contains 96 entries:
   Num:    Value  Size Type    Bind   Vis      Ndx Name
     0: 00000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 00000154     0 SECTION LOCAL  DEFAULT    1
     2: 00000168     0 SECTION LOCAL  DEFAULT    2
     3: 00000188     0 SECTION LOCAL  DEFAULT    3
     4: 00000234     0 SECTION LOCAL  DEFAULT    4
     5: 000003b4     0 SECTION LOCAL  DEFAULT    5
     6: 00000516     0 SECTION LOCAL  DEFAULT    6
     7: 00000548     0 SECTION LOCAL  DEFAULT    7
     8: 00000588     0 SECTION LOCAL  DEFAULT    8
     9: 000005d8     0 SECTION LOCAL  DEFAULT    9
    10: 00000630     0 SECTION LOCAL  DEFAULT   10
    11: 00000660     0 SECTION LOCAL  DEFAULT   11
    12: 00000720     0 SECTION LOCAL  DEFAULT   12
    13: 00000730     0 SECTION LOCAL  DEFAULT   13
    14: 00000ae4     0 SECTION LOCAL  DEFAULT   14
    15: 00000af8     0 SECTION LOCAL  DEFAULT   15
    16: 00000b04     0 SECTION LOCAL  DEFAULT   16
    17: 00000b38     0 SECTION LOCAL  DEFAULT   17
    18: 00001edc     0 SECTION LOCAL  DEFAULT   18
    19: 00001ee0     0 SECTION LOCAL  DEFAULT   19
    20: 00001ee4     0 SECTION LOCAL  DEFAULT   20
    21: 00001fe4     0 SECTION LOCAL  DEFAULT   21
    22: 00002000     0 SECTION LOCAL  DEFAULT   22
    23: 00002038     0 SECTION LOCAL  DEFAULT   23
    24: 00002040     0 SECTION LOCAL  DEFAULT   24
    25: 00000000     0 SECTION LOCAL  DEFAULT   25
    26: 00000000     0 SECTION LOCAL  DEFAULT   26
    27: 00000000     0 SECTION LOCAL  DEFAULT   27
    28: 00000000     0 SECTION LOCAL  DEFAULT   28
    29: 00000000     0 SECTION LOCAL  DEFAULT   29
    30: 00000000     0 SECTION LOCAL  DEFAULT   30
    31: 00000000     0 SECTION LOCAL  DEFAULT   31
    32: 00000000     0 SECTION LOCAL  DEFAULT   32
    33: 00000000     0 FILE    LOCAL  DEFAULT  ABS init.c
    34: 00000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    35: 00000780     0 FUNC    LOCAL  DEFAULT   13 deregister_tm_clones
    36: 000007c0     0 FUNC    LOCAL  DEFAULT   13 register_tm_clones
    37: 00000810     0 FUNC    LOCAL  DEFAULT   13 __do_global_dtors_aux
    38: 00002040     1 OBJECT  LOCAL  DEFAULT   24 completed.6880
    39: 00001ee0     0 OBJECT  LOCAL  DEFAULT   19 __do_global_dtors_aux_fin
    40: 00000860     0 FUNC    LOCAL  DEFAULT   13 frame_dummy
    41: 00001edc     0 OBJECT  LOCAL  DEFAULT   18 __frame_dummy_init_array_
    42: 00000000     0 FILE    LOCAL  DEFAULT  ABS src/lua.cpp
    43: 00000000     0 NOTYPE  LOCAL  DEFAULT   30
    44: 0000002d     0 NOTYPE  LOCAL  DEFAULT   30
    45: 00000039     0 NOTYPE  LOCAL  DEFAULT   30
    46: 00000061     0 NOTYPE  LOCAL  DEFAULT   30
    47: 00000066     0 NOTYPE  LOCAL  DEFAULT   30
    48: 0000006a     0 NOTYPE  LOCAL  DEFAULT   30
    49: 0000006f     0 NOTYPE  LOCAL  DEFAULT   30
    50: 00000074     0 NOTYPE  LOCAL  DEFAULT   30
    51: 0000007d     0 NOTYPE  LOCAL  DEFAULT   30
    52: 00000083     0 NOTYPE  LOCAL  DEFAULT   30
    53: 00000085     0 NOTYPE  LOCAL  DEFAULT   30
    54: 00000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    55: 00000c08     0 OBJECT  LOCAL  DEFAULT   17 __FRAME_END__
    56: 00000000     0 FILE    LOCAL  DEFAULT  ABS
    57: 00001ee0     0 NOTYPE  LOCAL  DEFAULT   18 __init_array_end
    58: 00001ee4     0 OBJECT  LOCAL  DEFAULT   20 _DYNAMIC
    59: 00001edc     0 NOTYPE  LOCAL  DEFAULT   18 __init_array_start
    60: 00000b04     0 NOTYPE  LOCAL  DEFAULT   16 __GNU_EH_FRAME_HDR
    61: 00002000     0 OBJECT  LOCAL  DEFAULT   22 _GLOBAL_OFFSET_TABLE_
    62: 00000ae0     2 FUNC    GLOBAL DEFAULT   13 __libc_csu_fini
    63: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_settop
    64: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    65: 00000770     4 FUNC    GLOBAL HIDDEN    13 __x86.get_pc_thunk.bx
    66: 00002038     0 NOTYPE  WEAK   DEFAULT   23 data_start
    67: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stderr@@GLIBC_2.0
    68: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_close
    69: 00000000     0 FUNC    GLOBAL DEFAULT  UND fgets@@GLIBC_2.0
    70: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_tolstring
    71: 00002040     0 NOTYPE  GLOBAL DEFAULT   23 _edata
    72: 00000ae4     0 FUNC    GLOBAL DEFAULT   14 _fini
    73: 00000000     0 FUNC    GLOBAL DEFAULT  UND __stack_chk_fail@@GLIBC_2
    74: 00000000     0 FUNC    GLOBAL DEFAULT  UND luaL_openlibs
    75: 00000869     0 FUNC    GLOBAL HIDDEN    13 __x86.get_pc_thunk.dx
    76: 00000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.1
    77: 00002038     0 NOTYPE  GLOBAL DEFAULT   23 __data_start
    78: 00000000     0 FUNC    GLOBAL DEFAULT  UND luaL_newstate
    79: 00000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    80: 0000203c     0 OBJECT  GLOBAL HIDDEN    23 __dso_handle
    81: 00000afc     4 OBJECT  GLOBAL DEFAULT   15 _IO_stdin_used
    82: 00000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@@GLIBC_
    83: 00000000     0 FUNC    GLOBAL DEFAULT  UND fprintf@@GLIBC_2.0
    84: 00000a80    93 FUNC    GLOBAL DEFAULT   13 __libc_csu_init
    85: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stdin@@GLIBC_2.0
    86: 00002044     0 NOTYPE  GLOBAL DEFAULT   24 _end
    87: 00000730     0 FUNC    GLOBAL DEFAULT   13 _start
    88: 00000af8     4 OBJECT  GLOBAL DEFAULT   15 _fp_hw
    89: 00002040     0 NOTYPE  GLOBAL DEFAULT   24 __bss_start
    90: 00000870   521 FUNC    GLOBAL DEFAULT   13 main
    91: 00000000     0 FUNC    GLOBAL DEFAULT  UND luaL_loadstring
    92: 00002040     0 OBJECT  GLOBAL HIDDEN    23 __TMC_END__
    93: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    94: 00000630     0 FUNC    GLOBAL DEFAULT   10 _init
    95: 00000000     0 FUNC    GLOBAL DEFAULT  UND lua_pcallk

Histogram for bucket list length (total of 17 buckets):
 Length  Number     % of total  Coverage
      0  12         ( 70.6%)
      1  1          (  5.9%)      9.1%
      2  2          ( 11.8%)     45.5%
      3  2          ( 11.8%)    100.0%

Version symbols section '.gnu.version' contains 24 entries:
 Addr: 0000000000000516  Offset: 0x000516  Link: 4 (.dynsym)
  000:   0 (*local*)       0 (*local*)       0 (*local*)       2 (GLIBC_2.0)
  004:   0 (*local*)       2 (GLIBC_2.0)     0 (*local*)       1 (*global*)
  008:   1 (*global*)      3 (GLIBC_2.4)     0 (*local*)       4 (GLIBC_2.1.3)
  00c:   0 (*local*)       0 (*local*)       1 (*global*)      2 (GLIBC_2.0)
  010:   2 (GLIBC_2.0)     2 (GLIBC_2.0)     1 (*global*)      1 (*global*)
  014:   0 (*local*)       0 (*local*)       1 (*global*)      0 (*local*)

Version needs section '.gnu.version_r' contains 1 entries:
 Addr: 0x0000000000000548  Offset: 0x000548  Link: 5 (.dynstr)
  000000: Version: 1  File: libc.so.6  Cnt: 3
  0x0010:   Name: GLIBC_2.1.3  Flags: none  Version: 4
  0x0020:   Name: GLIBC_2.4  Flags: none  Version: 3
  0x0030:   Name: GLIBC_2.0  Flags: none  Version: 2

Displaying notes found in: .note.ABI-tag
  Owner                 Data size	Description
  GNU                  0x00000010	NT_GNU_ABI_TAG (ABI version tag)
    OS: Linux, ABI: 3.2.0
```

## objdump

```plain
build/lua_test_32_clang_o0:     file format elf32-i386


Disassembly of section .init:

00000630 <_init>:
 630:	53                   	push   %ebx
 631:	83 ec 08             	sub    $0x8,%esp
 634:	e8 37 01 00 00       	call   770 <__x86.get_pc_thunk.bx>
 639:	81 c3 c7 19 00 00    	add    $0x19c7,%ebx
 63f:	8b 83 f0 ff ff ff    	mov    -0x10(%ebx),%eax
 645:	85 c0                	test   %eax,%eax
 647:	74 05                	je     64e <_init+0x1e>
 649:	e8 d2 00 00 00       	call   720 <__gmon_start__@plt>
 64e:	83 c4 08             	add    $0x8,%esp
 651:	5b                   	pop    %ebx
 652:	c3                   	ret

Disassembly of section .plt:

00000660 <.plt>:
 660:	ff b3 04 00 00 00    	pushl  0x4(%ebx)
 666:	ff a3 08 00 00 00    	jmp    *0x8(%ebx)
 66c:	00 00                	add    %al,(%eax)
	...

00000670 <lua_settop@plt>:
 670:	ff a3 0c 00 00 00    	jmp    *0xc(%ebx)
 676:	68 00 00 00 00       	push   $0x0
 67b:	e9 e0 ff ff ff       	jmp    660 <.plt>

00000680 <lua_close@plt>:
 680:	ff a3 10 00 00 00    	jmp    *0x10(%ebx)
 686:	68 08 00 00 00       	push   $0x8
 68b:	e9 d0 ff ff ff       	jmp    660 <.plt>

00000690 <fgets@plt>:
 690:	ff a3 14 00 00 00    	jmp    *0x14(%ebx)
 696:	68 10 00 00 00       	push   $0x10
 69b:	e9 c0 ff ff ff       	jmp    660 <.plt>

000006a0 <lua_tolstring@plt>:
 6a0:	ff a3 18 00 00 00    	jmp    *0x18(%ebx)
 6a6:	68 18 00 00 00       	push   $0x18
 6ab:	e9 b0 ff ff ff       	jmp    660 <.plt>

000006b0 <__stack_chk_fail@plt>:
 6b0:	ff a3 1c 00 00 00    	jmp    *0x1c(%ebx)
 6b6:	68 20 00 00 00       	push   $0x20
 6bb:	e9 a0 ff ff ff       	jmp    660 <.plt>

000006c0 <luaL_openlibs@plt>:
 6c0:	ff a3 20 00 00 00    	jmp    *0x20(%ebx)
 6c6:	68 28 00 00 00       	push   $0x28
 6cb:	e9 90 ff ff ff       	jmp    660 <.plt>

000006d0 <luaL_newstate@plt>:
 6d0:	ff a3 24 00 00 00    	jmp    *0x24(%ebx)
 6d6:	68 30 00 00 00       	push   $0x30
 6db:	e9 80 ff ff ff       	jmp    660 <.plt>

000006e0 <__libc_start_main@plt>:
 6e0:	ff a3 28 00 00 00    	jmp    *0x28(%ebx)
 6e6:	68 38 00 00 00       	push   $0x38
 6eb:	e9 70 ff ff ff       	jmp    660 <.plt>

000006f0 <fprintf@plt>:
 6f0:	ff a3 2c 00 00 00    	jmp    *0x2c(%ebx)
 6f6:	68 40 00 00 00       	push   $0x40
 6fb:	e9 60 ff ff ff       	jmp    660 <.plt>

00000700 <luaL_loadstring@plt>:
 700:	ff a3 30 00 00 00    	jmp    *0x30(%ebx)
 706:	68 48 00 00 00       	push   $0x48
 70b:	e9 50 ff ff ff       	jmp    660 <.plt>

00000710 <lua_pcallk@plt>:
 710:	ff a3 34 00 00 00    	jmp    *0x34(%ebx)
 716:	68 50 00 00 00       	push   $0x50
 71b:	e9 40 ff ff ff       	jmp    660 <.plt>

Disassembly of section .plt.got:

00000720 <__gmon_start__@plt>:
 720:	ff a3 f0 ff ff ff    	jmp    *-0x10(%ebx)
 726:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

00000730 <_start>:
 730:	31 ed                	xor    %ebp,%ebp
 732:	5e                   	pop    %esi
 733:	89 e1                	mov    %esp,%ecx
 735:	83 e4 f0             	and    $0xfffffff0,%esp
 738:	50                   	push   %eax
 739:	54                   	push   %esp
 73a:	52                   	push   %edx
 73b:	e8 22 00 00 00       	call   762 <_start+0x32>
 740:	81 c3 c0 18 00 00    	add    $0x18c0,%ebx
 746:	8d 83 e0 ea ff ff    	lea    -0x1520(%ebx),%eax
 74c:	50                   	push   %eax
 74d:	8d 83 80 ea ff ff    	lea    -0x1580(%ebx),%eax
 753:	50                   	push   %eax
 754:	51                   	push   %ecx
 755:	56                   	push   %esi
 756:	ff b3 f8 ff ff ff    	pushl  -0x8(%ebx)
 75c:	e8 7f ff ff ff       	call   6e0 <__libc_start_main@plt>
 761:	f4                   	hlt
 762:	8b 1c 24             	mov    (%esp),%ebx
 765:	c3                   	ret
 766:	66 90                	xchg   %ax,%ax
 768:	66 90                	xchg   %ax,%ax
 76a:	66 90                	xchg   %ax,%ax
 76c:	66 90                	xchg   %ax,%ax
 76e:	66 90                	xchg   %ax,%ax

00000770 <__x86.get_pc_thunk.bx>:
 770:	8b 1c 24             	mov    (%esp),%ebx
 773:	c3                   	ret
 774:	66 90                	xchg   %ax,%ax
 776:	66 90                	xchg   %ax,%ax
 778:	66 90                	xchg   %ax,%ax
 77a:	66 90                	xchg   %ax,%ax
 77c:	66 90                	xchg   %ax,%ax
 77e:	66 90                	xchg   %ax,%ax

00000780 <deregister_tm_clones>:
 780:	e8 e4 00 00 00       	call   869 <__x86.get_pc_thunk.dx>
 785:	81 c2 7b 18 00 00    	add    $0x187b,%edx
 78b:	8d 8a 40 00 00 00    	lea    0x40(%edx),%ecx
 791:	8d 82 40 00 00 00    	lea    0x40(%edx),%eax
 797:	39 c8                	cmp    %ecx,%eax
 799:	74 1d                	je     7b8 <deregister_tm_clones+0x38>
 79b:	8b 82 e4 ff ff ff    	mov    -0x1c(%edx),%eax
 7a1:	85 c0                	test   %eax,%eax
 7a3:	74 13                	je     7b8 <deregister_tm_clones+0x38>
 7a5:	55                   	push   %ebp
 7a6:	89 e5                	mov    %esp,%ebp
 7a8:	83 ec 14             	sub    $0x14,%esp
 7ab:	51                   	push   %ecx
 7ac:	ff d0                	call   *%eax
 7ae:	83 c4 10             	add    $0x10,%esp
 7b1:	c9                   	leave
 7b2:	c3                   	ret
 7b3:	90                   	nop
 7b4:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 7b8:	f3 c3                	repz ret
 7ba:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi

000007c0 <register_tm_clones>:
 7c0:	e8 a4 00 00 00       	call   869 <__x86.get_pc_thunk.dx>
 7c5:	81 c2 3b 18 00 00    	add    $0x183b,%edx
 7cb:	55                   	push   %ebp
 7cc:	8d 8a 40 00 00 00    	lea    0x40(%edx),%ecx
 7d2:	8d 82 40 00 00 00    	lea    0x40(%edx),%eax
 7d8:	29 c8                	sub    %ecx,%eax
 7da:	89 e5                	mov    %esp,%ebp
 7dc:	53                   	push   %ebx
 7dd:	c1 f8 02             	sar    $0x2,%eax
 7e0:	89 c3                	mov    %eax,%ebx
 7e2:	83 ec 04             	sub    $0x4,%esp
 7e5:	c1 eb 1f             	shr    $0x1f,%ebx
 7e8:	01 d8                	add    %ebx,%eax
 7ea:	d1 f8                	sar    %eax
 7ec:	74 14                	je     802 <register_tm_clones+0x42>
 7ee:	8b 92 fc ff ff ff    	mov    -0x4(%edx),%edx
 7f4:	85 d2                	test   %edx,%edx
 7f6:	74 0a                	je     802 <register_tm_clones+0x42>
 7f8:	83 ec 08             	sub    $0x8,%esp
 7fb:	50                   	push   %eax
 7fc:	51                   	push   %ecx
 7fd:	ff d2                	call   *%edx
 7ff:	83 c4 10             	add    $0x10,%esp
 802:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 805:	c9                   	leave
 806:	c3                   	ret
 807:	89 f6                	mov    %esi,%esi
 809:	8d bc 27 00 00 00 00 	lea    0x0(%edi,%eiz,1),%edi

00000810 <__do_global_dtors_aux>:
 810:	55                   	push   %ebp
 811:	89 e5                	mov    %esp,%ebp
 813:	53                   	push   %ebx
 814:	e8 57 ff ff ff       	call   770 <__x86.get_pc_thunk.bx>
 819:	81 c3 e7 17 00 00    	add    $0x17e7,%ebx
 81f:	83 ec 04             	sub    $0x4,%esp
 822:	80 bb 40 00 00 00 00 	cmpb   $0x0,0x40(%ebx)
 829:	75 28                	jne    853 <__do_global_dtors_aux+0x43>
 82b:	8b 83 ec ff ff ff    	mov    -0x14(%ebx),%eax
 831:	85 c0                	test   %eax,%eax
 833:	74 12                	je     847 <__do_global_dtors_aux+0x37>
 835:	83 ec 0c             	sub    $0xc,%esp
 838:	ff b3 3c 00 00 00    	pushl  0x3c(%ebx)
 83e:	ff 93 ec ff ff ff    	call   *-0x14(%ebx)
 844:	83 c4 10             	add    $0x10,%esp
 847:	e8 34 ff ff ff       	call   780 <deregister_tm_clones>
 84c:	c6 83 40 00 00 00 01 	movb   $0x1,0x40(%ebx)
 853:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 856:	c9                   	leave
 857:	c3                   	ret
 858:	90                   	nop
 859:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi

00000860 <frame_dummy>:
 860:	55                   	push   %ebp
 861:	89 e5                	mov    %esp,%ebp
 863:	5d                   	pop    %ebp
 864:	e9 57 ff ff ff       	jmp    7c0 <register_tm_clones>

00000869 <__x86.get_pc_thunk.dx>:
 869:	8b 14 24             	mov    (%esp),%edx
 86c:	c3                   	ret
 86d:	66 90                	xchg   %ax,%ax
 86f:	90                   	nop

00000870 <main>:
 870:	55                   	push   %ebp
 871:	89 e5                	mov    %esp,%ebp
 873:	53                   	push   %ebx
 874:	57                   	push   %edi
 875:	56                   	push   %esi
 876:	81 ec 4c 01 00 00    	sub    $0x14c,%esp
 87c:	e8 00 00 00 00       	call   881 <main+0x11>
 881:	58                   	pop    %eax
 882:	81 c0 7f 17 00 00    	add    $0x177f,%eax
 888:	65 8b 0d 14 00 00 00 	mov    %gs:0x14,%ecx
 88f:	89 4d f0             	mov    %ecx,-0x10(%ebp)
 892:	c7 85 ec fe ff ff 00 	movl   $0x0,-0x114(%ebp)
 899:	00 00 00
 89c:	89 c3                	mov    %eax,%ebx
 89e:	89 85 e0 fe ff ff    	mov    %eax,-0x120(%ebp)
 8a4:	e8 27 fe ff ff       	call   6d0 <luaL_newstate@plt>
 8a9:	89 85 e4 fe ff ff    	mov    %eax,-0x11c(%ebp)
 8af:	8b 85 e4 fe ff ff    	mov    -0x11c(%ebp),%eax
 8b5:	89 04 24             	mov    %eax,(%esp)
 8b8:	8b 9d e0 fe ff ff    	mov    -0x120(%ebp),%ebx
 8be:	e8 fd fd ff ff       	call   6c0 <luaL_openlibs@plt>
 8c3:	b8 00 01 00 00       	mov    $0x100,%eax
 8c8:	8b 8d e0 fe ff ff    	mov    -0x120(%ebp),%ecx
 8ce:	8b 91 f4 ff ff ff    	mov    -0xc(%ecx),%edx
 8d4:	8d b5 f0 fe ff ff    	lea    -0x110(%ebp),%esi
 8da:	8b 12                	mov    (%edx),%edx
 8dc:	89 34 24             	mov    %esi,(%esp)
 8df:	c7 44 24 04 00 01 00 	movl   $0x100,0x4(%esp)
 8e6:	00
 8e7:	89 54 24 08          	mov    %edx,0x8(%esp)
 8eb:	89 cb                	mov    %ecx,%ebx
 8ed:	89 85 dc fe ff ff    	mov    %eax,-0x124(%ebp)
 8f3:	e8 98 fd ff ff       	call   690 <fgets@plt>
 8f8:	83 f8 00             	cmp    $0x0,%eax
 8fb:	0f 84 3a 01 00 00    	je     a3b <main+0x1cb>
 901:	8d 85 f0 fe ff ff    	lea    -0x110(%ebp),%eax
 907:	8b 8d e4 fe ff ff    	mov    -0x11c(%ebp),%ecx
 90d:	89 0c 24             	mov    %ecx,(%esp)
 910:	89 44 24 04          	mov    %eax,0x4(%esp)
 914:	8b 9d e0 fe ff ff    	mov    -0x120(%ebp),%ebx
 91a:	e8 e1 fd ff ff       	call   700 <luaL_loadstring@plt>
 91f:	b2 01                	mov    $0x1,%dl
 921:	83 f8 00             	cmp    $0x0,%eax
 924:	88 95 db fe ff ff    	mov    %dl,-0x125(%ebp)
 92a:	0f 85 50 00 00 00    	jne    980 <main+0x110>
 930:	31 c0                	xor    %eax,%eax
 932:	8b 8d e4 fe ff ff    	mov    -0x11c(%ebp),%ecx
 938:	89 0c 24             	mov    %ecx,(%esp)
 93b:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%esp)
 942:	00
 943:	c7 44 24 08 00 00 00 	movl   $0x0,0x8(%esp)
 94a:	00
 94b:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
 952:	00
 953:	c7 44 24 10 00 00 00 	movl   $0x0,0x10(%esp)
 95a:	00
 95b:	c7 44 24 14 00 00 00 	movl   $0x0,0x14(%esp)
 962:	00
 963:	8b 9d e0 fe ff ff    	mov    -0x120(%ebp),%ebx
 969:	89 85 d4 fe ff ff    	mov    %eax,-0x12c(%ebp)
 96f:	e8 9c fd ff ff       	call   710 <lua_pcallk@plt>
 974:	83 f8 00             	cmp    $0x0,%eax
 977:	0f 95 c2             	setne  %dl
 97a:	88 95 db fe ff ff    	mov    %dl,-0x125(%ebp)
 980:	8a 85 db fe ff ff    	mov    -0x125(%ebp),%al
 986:	24 01                	and    $0x1,%al
 988:	0f b6 c8             	movzbl %al,%ecx
 98b:	89 8d e8 fe ff ff    	mov    %ecx,-0x118(%ebp)
 991:	83 bd e8 fe ff ff 00 	cmpl   $0x0,-0x118(%ebp)
 998:	0f 84 98 00 00 00    	je     a36 <main+0x1c6>
 99e:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 9a3:	31 c9                	xor    %ecx,%ecx
 9a5:	8b 95 e0 fe ff ff    	mov    -0x120(%ebp),%edx
 9ab:	8b b2 e8 ff ff ff    	mov    -0x18(%edx),%esi
 9b1:	8b 36                	mov    (%esi),%esi
 9b3:	8b bd e4 fe ff ff    	mov    -0x11c(%ebp),%edi
 9b9:	89 3c 24             	mov    %edi,(%esp)
 9bc:	c7 44 24 04 ff ff ff 	movl   $0xffffffff,0x4(%esp)
 9c3:	ff
 9c4:	c7 44 24 08 00 00 00 	movl   $0x0,0x8(%esp)
 9cb:	00
 9cc:	89 d3                	mov    %edx,%ebx
 9ce:	89 85 d0 fe ff ff    	mov    %eax,-0x130(%ebp)
 9d4:	89 8d cc fe ff ff    	mov    %ecx,-0x134(%ebp)
 9da:	89 b5 c8 fe ff ff    	mov    %esi,-0x138(%ebp)
 9e0:	e8 bb fc ff ff       	call   6a0 <lua_tolstring@plt>
 9e5:	8b 8d e0 fe ff ff    	mov    -0x120(%ebp),%ecx
 9eb:	8d 91 00 eb ff ff    	lea    -0x1500(%ecx),%edx
 9f1:	8b b5 c8 fe ff ff    	mov    -0x138(%ebp),%esi
 9f7:	89 34 24             	mov    %esi,(%esp)
 9fa:	89 54 24 04          	mov    %edx,0x4(%esp)
 9fe:	89 44 24 08          	mov    %eax,0x8(%esp)
 a02:	89 cb                	mov    %ecx,%ebx
 a04:	e8 e7 fc ff ff       	call   6f0 <fprintf@plt>
 a09:	b9 fe ff ff ff       	mov    $0xfffffffe,%ecx
 a0e:	8b 95 e4 fe ff ff    	mov    -0x11c(%ebp),%edx
 a14:	89 14 24             	mov    %edx,(%esp)
 a17:	c7 44 24 04 fe ff ff 	movl   $0xfffffffe,0x4(%esp)
 a1e:	ff
 a1f:	8b 9d e0 fe ff ff    	mov    -0x120(%ebp),%ebx
 a25:	89 85 c4 fe ff ff    	mov    %eax,-0x13c(%ebp)
 a2b:	89 8d c0 fe ff ff    	mov    %ecx,-0x140(%ebp)
 a31:	e8 3a fc ff ff       	call   670 <lua_settop@plt>
 a36:	e9 88 fe ff ff       	jmp    8c3 <main+0x53>
 a3b:	8b 85 e4 fe ff ff    	mov    -0x11c(%ebp),%eax
 a41:	89 e1                	mov    %esp,%ecx
 a43:	89 01                	mov    %eax,(%ecx)
 a45:	8b 9d e0 fe ff ff    	mov    -0x120(%ebp),%ebx
 a4b:	e8 30 fc ff ff       	call   680 <lua_close@plt>
 a50:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 a56:	8b 4d f0             	mov    -0x10(%ebp),%ecx
 a59:	39 c8                	cmp    %ecx,%eax
 a5b:	0f 85 0d 00 00 00    	jne    a6e <main+0x1fe>
 a61:	31 c0                	xor    %eax,%eax
 a63:	81 c4 4c 01 00 00    	add    $0x14c,%esp
 a69:	5e                   	pop    %esi
 a6a:	5f                   	pop    %edi
 a6b:	5b                   	pop    %ebx
 a6c:	5d                   	pop    %ebp
 a6d:	c3                   	ret
 a6e:	8b 9d e0 fe ff ff    	mov    -0x120(%ebp),%ebx
 a74:	e8 37 fc ff ff       	call   6b0 <__stack_chk_fail@plt>
 a79:	66 90                	xchg   %ax,%ax
 a7b:	66 90                	xchg   %ax,%ax
 a7d:	66 90                	xchg   %ax,%ax
 a7f:	90                   	nop

00000a80 <__libc_csu_init>:
 a80:	55                   	push   %ebp
 a81:	57                   	push   %edi
 a82:	56                   	push   %esi
 a83:	53                   	push   %ebx
 a84:	e8 e7 fc ff ff       	call   770 <__x86.get_pc_thunk.bx>
 a89:	81 c3 77 15 00 00    	add    $0x1577,%ebx
 a8f:	83 ec 0c             	sub    $0xc,%esp
 a92:	8b 6c 24 28          	mov    0x28(%esp),%ebp
 a96:	8d b3 e0 fe ff ff    	lea    -0x120(%ebx),%esi
 a9c:	e8 8f fb ff ff       	call   630 <_init>
 aa1:	8d 83 dc fe ff ff    	lea    -0x124(%ebx),%eax
 aa7:	29 c6                	sub    %eax,%esi
 aa9:	c1 fe 02             	sar    $0x2,%esi
 aac:	85 f6                	test   %esi,%esi
 aae:	74 25                	je     ad5 <__libc_csu_init+0x55>
 ab0:	31 ff                	xor    %edi,%edi
 ab2:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi
 ab8:	83 ec 04             	sub    $0x4,%esp
 abb:	55                   	push   %ebp
 abc:	ff 74 24 2c          	pushl  0x2c(%esp)
 ac0:	ff 74 24 2c          	pushl  0x2c(%esp)
 ac4:	ff 94 bb dc fe ff ff 	call   *-0x124(%ebx,%edi,4)
 acb:	83 c7 01             	add    $0x1,%edi
 ace:	83 c4 10             	add    $0x10,%esp
 ad1:	39 fe                	cmp    %edi,%esi
 ad3:	75 e3                	jne    ab8 <__libc_csu_init+0x38>
 ad5:	83 c4 0c             	add    $0xc,%esp
 ad8:	5b                   	pop    %ebx
 ad9:	5e                   	pop    %esi
 ada:	5f                   	pop    %edi
 adb:	5d                   	pop    %ebp
 adc:	c3                   	ret
 add:	8d 76 00             	lea    0x0(%esi),%esi

00000ae0 <__libc_csu_fini>:
 ae0:	f3 c3                	repz ret

Disassembly of section .fini:

00000ae4 <_fini>:
 ae4:	53                   	push   %ebx
 ae5:	83 ec 08             	sub    $0x8,%esp
 ae8:	e8 83 fc ff ff       	call   770 <__x86.get_pc_thunk.bx>
 aed:	81 c3 13 15 00 00    	add    $0x1513,%ebx
 af3:	83 c4 08             	add    $0x8,%esp
 af6:	5b                   	pop    %ebx
 af7:	c3                   	ret
```

# build/inject.so

## readelf
```plain
ELF Header:
  Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF32
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Intel 80386
  Version:                           0x1
  Entry point address:               0x3e0
  Start of program headers:          52 (bytes into file)
  Start of section headers:          9616 (bytes into file)
  Flags:                             0x0
  Size of this header:               52 (bytes)
  Size of program headers:           32 (bytes)
  Number of program headers:         7
  Size of section headers:           40 (bytes)
  Number of section headers:         33
  Section header string table index: 32

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] .note.gnu.build-i NOTE            00000114 000114 000024 00   A  0   0  4
  [ 2] .gnu.hash         GNU_HASH        00000138 000138 00003c 04   A  3   0  4
  [ 3] .dynsym           DYNSYM          00000174 000174 0000c0 10   A  4   1  4
  [ 4] .dynstr           STRTAB          00000234 000234 0000cb 00   A  0   0  1
  [ 5] .gnu.version      VERSYM          00000300 000300 000018 02   A  3   0  2
  [ 6] .gnu.version_r    VERNEED         00000318 000318 000030 00   A  4   1  4
  [ 7] .rel.dyn          REL             00000348 000348 000038 08   A  3   0  4
  [ 8] .rel.plt          REL             00000380 000380 000008 08  AI  3  21  4
  [ 9] .init             PROGBITS        00000388 000388 000023 00  AX  0   0  4
  [10] .plt              PROGBITS        000003b0 0003b0 000020 04  AX  0   0 16
  [11] .plt.got          PROGBITS        000003d0 0003d0 000008 08  AX  0   0  8
  [12] .text             PROGBITS        000003e0 0003e0 00013f 00  AX  0   0 16
  [13] .fini             PROGBITS        00000520 000520 000014 00  AX  0   0  4
  [14] .rodata           PROGBITS        00000534 000534 000007 00   A  0   0  1
  [15] .eh_frame_hdr     PROGBITS        0000053c 00053c 000024 00   A  0   0  4
  [16] .eh_frame         PROGBITS        00000560 000560 000078 00   A  0   0  4
  [17] .init_array       INIT_ARRAY      00001ef0 000ef0 000004 04  WA  0   0  4
  [18] .fini_array       FINI_ARRAY      00001ef4 000ef4 000004 04  WA  0   0  4
  [19] .dynamic          DYNAMIC         00001ef8 000ef8 0000f8 08  WA  4   0  4
  [20] .got              PROGBITS        00001ff0 000ff0 000010 04  WA  0   0  4
  [21] .got.plt          PROGBITS        00002000 001000 000010 04  WA  0   0  4
  [22] .data             PROGBITS        00002010 001010 000004 00  WA  0   0  4
  [23] .bss              NOBITS          00002014 001014 000004 00  WA  0   0  1
  [24] .comment          PROGBITS        00000000 001014 00001a 01  MS  0   0  1
  [25] .debug_aranges    PROGBITS        00000000 00102e 000020 00      0   0  1
  [26] .debug_info       PROGBITS        00000000 00104e 000768 00      0   0  1
  [27] .debug_abbrev     PROGBITS        00000000 0017b6 0001e1 00      0   0  1
  [28] .debug_line       PROGBITS        00000000 001997 000196 00      0   0  1
  [29] .debug_str        PROGBITS        00000000 001b2d 0003af 01  MS  0   0  1
  [30] .symtab           SYMTAB          00000000 001edc 0003c0 10     31  49  4
  [31] .strtab           STRTAB          00000000 00229c 0001c3 00      0   0  1
  [32] .shstrtab         STRTAB          00000000 00245f 00012f 00      0   0  1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset   VirtAddr   PhysAddr   FileSiz MemSiz  Flg Align
  LOAD           0x000000 0x00000000 0x00000000 0x005d8 0x005d8 R E 0x1000
  LOAD           0x000ef0 0x00001ef0 0x00001ef0 0x00124 0x00128 RW  0x1000
  DYNAMIC        0x000ef8 0x00001ef8 0x00001ef8 0x000f8 0x000f8 RW  0x4
  NOTE           0x000114 0x00000114 0x00000114 0x00024 0x00024 R   0x4
  GNU_EH_FRAME   0x00053c 0x0000053c 0x0000053c 0x00024 0x00024 R   0x4
  GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RW  0x10
  GNU_RELRO      0x000ef0 0x00001ef0 0x00001ef0 0x00110 0x00110 R   0x1

 Section to Segment mapping:
  Segment Sections...
   00     .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rel.dyn .rel.plt .init .plt .plt.got .text .fini .rodata .eh_frame_hdr .eh_frame
   01     .init_array .fini_array .dynamic .got .got.plt .data .bss
   02     .dynamic
   03     .note.gnu.build-id
   04     .eh_frame_hdr
   05
   06     .init_array .fini_array .dynamic .got

Dynamic section at offset 0xef8 contains 27 entries:
  Tag        Type                         Name/Value
 0x00000001 (NEEDED)                     Shared library: [libstdc++.so.6]
 0x00000001 (NEEDED)                     Shared library: [libm.so.6]
 0x00000001 (NEEDED)                     Shared library: [libgcc_s.so.1]
 0x00000001 (NEEDED)                     Shared library: [libc.so.6]
 0x0000000c (INIT)                       0x388
 0x0000000d (FINI)                       0x520
 0x00000019 (INIT_ARRAY)                 0x1ef0
 0x0000001b (INIT_ARRAYSZ)               4 (bytes)
 0x0000001a (FINI_ARRAY)                 0x1ef4
 0x0000001c (FINI_ARRAYSZ)               4 (bytes)
 0x6ffffef5 (GNU_HASH)                   0x138
 0x00000005 (STRTAB)                     0x234
 0x00000006 (SYMTAB)                     0x174
 0x0000000a (STRSZ)                      203 (bytes)
 0x0000000b (SYMENT)                     16 (bytes)
 0x00000003 (PLTGOT)                     0x2000
 0x00000002 (PLTRELSZ)                   8 (bytes)
 0x00000014 (PLTREL)                     REL
 0x00000017 (JMPREL)                     0x380
 0x00000011 (REL)                        0x348
 0x00000012 (RELSZ)                      56 (bytes)
 0x00000013 (RELENT)                     8 (bytes)
 0x6ffffffe (VERNEED)                    0x318
 0x6fffffff (VERNEEDNUM)                 1
 0x6ffffff0 (VERSYM)                     0x300
 0x6ffffffa (RELCOUNT)                   3
 0x00000000 (NULL)                       0x0

Relocation section '.rel.dyn' at offset 0x348 contains 7 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
00001ef0  00000008 R_386_RELATIVE
00001ef4  00000008 R_386_RELATIVE
00002010  00000008 R_386_RELATIVE
00001ff0  00000106 R_386_GLOB_DAT    00000000   __cxa_finalize@GLIBC_2.1.3
00001ff4  00000306 R_386_GLOB_DAT    00000000   _ITM_deregisterTMClone
00001ff8  00000406 R_386_GLOB_DAT    00000000   __gmon_start__
00001ffc  00000506 R_386_GLOB_DAT    00000000   _ITM_registerTMCloneTa

Relocation section '.rel.plt' at offset 0x380 contains 1 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
0000200c  00000207 R_386_JUMP_SLOT   00000000   printf@GLIBC_2.0

The decoding of unwind sections for machine type Intel 80386 is not currently supported.

Symbol table '.dynsym' contains 12 entries:
   Num:    Value  Size Type    Bind   Vis      Ndx Name
     0: 00000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 00000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@GLIBC_2.1.3 (2)
     2: 00000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.0 (3)
     3: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
     4: 00000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     5: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
     6: 00002014     0 NOTYPE  GLOBAL DEFAULT   22 _edata
     7: 00002018     0 NOTYPE  GLOBAL DEFAULT   23 _end
     8: 000004dd    66 FUNC    GLOBAL DEFAULT   12 abc
     9: 00000388     0 FUNC    GLOBAL DEFAULT    9 _init
    10: 00002014     0 NOTYPE  GLOBAL DEFAULT   23 __bss_start
    11: 00000520     0 FUNC    GLOBAL DEFAULT   13 _fini

Symbol table '.symtab' contains 60 entries:
   Num:    Value  Size Type    Bind   Vis      Ndx Name
     0: 00000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 00000114     0 SECTION LOCAL  DEFAULT    1
     2: 00000138     0 SECTION LOCAL  DEFAULT    2
     3: 00000174     0 SECTION LOCAL  DEFAULT    3
     4: 00000234     0 SECTION LOCAL  DEFAULT    4
     5: 00000300     0 SECTION LOCAL  DEFAULT    5
     6: 00000318     0 SECTION LOCAL  DEFAULT    6
     7: 00000348     0 SECTION LOCAL  DEFAULT    7
     8: 00000380     0 SECTION LOCAL  DEFAULT    8
     9: 00000388     0 SECTION LOCAL  DEFAULT    9
    10: 000003b0     0 SECTION LOCAL  DEFAULT   10
    11: 000003d0     0 SECTION LOCAL  DEFAULT   11
    12: 000003e0     0 SECTION LOCAL  DEFAULT   12
    13: 00000520     0 SECTION LOCAL  DEFAULT   13
    14: 00000534     0 SECTION LOCAL  DEFAULT   14
    15: 0000053c     0 SECTION LOCAL  DEFAULT   15
    16: 00000560     0 SECTION LOCAL  DEFAULT   16
    17: 00001ef0     0 SECTION LOCAL  DEFAULT   17
    18: 00001ef4     0 SECTION LOCAL  DEFAULT   18
    19: 00001ef8     0 SECTION LOCAL  DEFAULT   19
    20: 00001ff0     0 SECTION LOCAL  DEFAULT   20
    21: 00002000     0 SECTION LOCAL  DEFAULT   21
    22: 00002010     0 SECTION LOCAL  DEFAULT   22
    23: 00002014     0 SECTION LOCAL  DEFAULT   23
    24: 00000000     0 SECTION LOCAL  DEFAULT   24
    25: 00000000     0 SECTION LOCAL  DEFAULT   25
    26: 00000000     0 SECTION LOCAL  DEFAULT   26
    27: 00000000     0 SECTION LOCAL  DEFAULT   27
    28: 00000000     0 SECTION LOCAL  DEFAULT   28
    29: 00000000     0 SECTION LOCAL  DEFAULT   29
    30: 00000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    31: 000003f0     0 FUNC    LOCAL  DEFAULT   12 deregister_tm_clones
    32: 00000430     0 FUNC    LOCAL  DEFAULT   12 register_tm_clones
    33: 00000480     0 FUNC    LOCAL  DEFAULT   12 __do_global_dtors_aux
    34: 00002014     1 OBJECT  LOCAL  DEFAULT   23 completed.6880
    35: 00001ef4     0 OBJECT  LOCAL  DEFAULT   18 __do_global_dtors_aux_fin
    36: 000004d0     0 FUNC    LOCAL  DEFAULT   12 frame_dummy
    37: 00001ef0     0 OBJECT  LOCAL  DEFAULT   17 __frame_dummy_init_array_
    38: 00000000     0 FILE    LOCAL  DEFAULT  ABS inject.cpp
    39: 00000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    40: 000005d4     0 OBJECT  LOCAL  DEFAULT   16 __FRAME_END__
    41: 00000000     0 FILE    LOCAL  DEFAULT  ABS
    42: 0000053c     0 NOTYPE  LOCAL  DEFAULT   15 __GNU_EH_FRAME_HDR
    43: 00002010     0 OBJECT  LOCAL  DEFAULT   22 __dso_handle
    44: 000003e0     4 FUNC    LOCAL  DEFAULT   12 __x86.get_pc_thunk.bx
    45: 00001ef8     0 OBJECT  LOCAL  DEFAULT   19 _DYNAMIC
    46: 00002014     0 OBJECT  LOCAL  DEFAULT   22 __TMC_END__
    47: 000004d9     0 FUNC    LOCAL  DEFAULT   12 __x86.get_pc_thunk.dx
    48: 00002000     0 OBJECT  LOCAL  DEFAULT   21 _GLOBAL_OFFSET_TABLE_
    49: 00000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.1
    50: 00002014     0 NOTYPE  GLOBAL DEFAULT   22 _edata
    51: 00000520     0 FUNC    GLOBAL DEFAULT   13 _fini
    52: 00000388     0 FUNC    GLOBAL DEFAULT    9 _init
    53: 00002018     0 NOTYPE  GLOBAL DEFAULT   23 _end
    54: 00000000     0 FUNC    GLOBAL DEFAULT  UND printf@@GLIBC_2.0
    55: 00002014     0 NOTYPE  GLOBAL DEFAULT   23 __bss_start
    56: 000004dd    66 FUNC    GLOBAL DEFAULT   12 abc
    57: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    58: 00000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    59: 00000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable

Histogram for `.gnu.hash' bucket list length (total of 3 buckets):
 Length  Number     % of total  Coverage
      0  0          (  0.0%)
      1  1          ( 33.3%)     16.7%
      2  1          ( 33.3%)     50.0%
      3  1          ( 33.3%)    100.0%

Version symbols section '.gnu.version' contains 12 entries:
 Addr: 0000000000000300  Offset: 0x000300  Link: 3 (.dynsym)
  000:   0 (*local*)       2 (GLIBC_2.1.3)   3 (GLIBC_2.0)     0 (*local*)
  004:   0 (*local*)       0 (*local*)       1 (*global*)      1 (*global*)
  008:   1 (*global*)      1 (*global*)      1 (*global*)      1 (*global*)

Version needs section '.gnu.version_r' contains 1 entries:
 Addr: 0x0000000000000318  Offset: 0x000318  Link: 4 (.dynstr)
  000000: Version: 1  File: libc.so.6  Cnt: 2
  0x0010:   Name: GLIBC_2.0  Flags: none  Version: 3
  0x0020:   Name: GLIBC_2.1.3  Flags: none  Version: 2

Displaying notes found in: .note.gnu.build-id
  Owner                 Data size	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 305339e2cde038e3c5d4482fc4639116d57217cd
```

## objdump

```plain
build/inject.so:     file format elf32-i386


Disassembly of section .init:

00000388 <_init>:
 388:	53                   	push   %ebx
 389:	83 ec 08             	sub    $0x8,%esp
 38c:	e8 4f 00 00 00       	call   3e0 <__x86.get_pc_thunk.bx>
 391:	81 c3 6f 1c 00 00    	add    $0x1c6f,%ebx
 397:	8b 83 f8 ff ff ff    	mov    -0x8(%ebx),%eax
 39d:	85 c0                	test   %eax,%eax
 39f:	74 05                	je     3a6 <_init+0x1e>
 3a1:	e8 2a 00 00 00       	call   3d0 <__gmon_start__@plt>
 3a6:	83 c4 08             	add    $0x8,%esp
 3a9:	5b                   	pop    %ebx
 3aa:	c3                   	ret

Disassembly of section .plt:

000003b0 <.plt>:
 3b0:	ff b3 04 00 00 00    	pushl  0x4(%ebx)
 3b6:	ff a3 08 00 00 00    	jmp    *0x8(%ebx)
 3bc:	00 00                	add    %al,(%eax)
	...

000003c0 <printf@plt>:
 3c0:	ff a3 0c 00 00 00    	jmp    *0xc(%ebx)
 3c6:	68 00 00 00 00       	push   $0x0
 3cb:	e9 e0 ff ff ff       	jmp    3b0 <.plt>

Disassembly of section .plt.got:

000003d0 <__gmon_start__@plt>:
 3d0:	ff a3 f8 ff ff ff    	jmp    *-0x8(%ebx)
 3d6:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

000003e0 <__x86.get_pc_thunk.bx>:
 3e0:	8b 1c 24             	mov    (%esp),%ebx
 3e3:	c3                   	ret
 3e4:	66 90                	xchg   %ax,%ax
 3e6:	66 90                	xchg   %ax,%ax
 3e8:	66 90                	xchg   %ax,%ax
 3ea:	66 90                	xchg   %ax,%ax
 3ec:	66 90                	xchg   %ax,%ax
 3ee:	66 90                	xchg   %ax,%ax

000003f0 <deregister_tm_clones>:
 3f0:	e8 e4 00 00 00       	call   4d9 <__x86.get_pc_thunk.dx>
 3f5:	81 c2 0b 1c 00 00    	add    $0x1c0b,%edx
 3fb:	8d 8a 14 00 00 00    	lea    0x14(%edx),%ecx
 401:	8d 82 14 00 00 00    	lea    0x14(%edx),%eax
 407:	39 c8                	cmp    %ecx,%eax
 409:	74 1d                	je     428 <deregister_tm_clones+0x38>
 40b:	8b 82 f4 ff ff ff    	mov    -0xc(%edx),%eax
 411:	85 c0                	test   %eax,%eax
 413:	74 13                	je     428 <deregister_tm_clones+0x38>
 415:	55                   	push   %ebp
 416:	89 e5                	mov    %esp,%ebp
 418:	83 ec 14             	sub    $0x14,%esp
 41b:	51                   	push   %ecx
 41c:	ff d0                	call   *%eax
 41e:	83 c4 10             	add    $0x10,%esp
 421:	c9                   	leave
 422:	c3                   	ret
 423:	90                   	nop
 424:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 428:	f3 c3                	repz ret
 42a:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi

00000430 <register_tm_clones>:
 430:	e8 a4 00 00 00       	call   4d9 <__x86.get_pc_thunk.dx>
 435:	81 c2 cb 1b 00 00    	add    $0x1bcb,%edx
 43b:	55                   	push   %ebp
 43c:	8d 8a 14 00 00 00    	lea    0x14(%edx),%ecx
 442:	8d 82 14 00 00 00    	lea    0x14(%edx),%eax
 448:	29 c8                	sub    %ecx,%eax
 44a:	89 e5                	mov    %esp,%ebp
 44c:	53                   	push   %ebx
 44d:	c1 f8 02             	sar    $0x2,%eax
 450:	89 c3                	mov    %eax,%ebx
 452:	83 ec 04             	sub    $0x4,%esp
 455:	c1 eb 1f             	shr    $0x1f,%ebx
 458:	01 d8                	add    %ebx,%eax
 45a:	d1 f8                	sar    %eax
 45c:	74 14                	je     472 <register_tm_clones+0x42>
 45e:	8b 92 fc ff ff ff    	mov    -0x4(%edx),%edx
 464:	85 d2                	test   %edx,%edx
 466:	74 0a                	je     472 <register_tm_clones+0x42>
 468:	83 ec 08             	sub    $0x8,%esp
 46b:	50                   	push   %eax
 46c:	51                   	push   %ecx
 46d:	ff d2                	call   *%edx
 46f:	83 c4 10             	add    $0x10,%esp
 472:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 475:	c9                   	leave
 476:	c3                   	ret
 477:	89 f6                	mov    %esi,%esi
 479:	8d bc 27 00 00 00 00 	lea    0x0(%edi,%eiz,1),%edi

00000480 <__do_global_dtors_aux>:
 480:	55                   	push   %ebp
 481:	89 e5                	mov    %esp,%ebp
 483:	53                   	push   %ebx
 484:	e8 57 ff ff ff       	call   3e0 <__x86.get_pc_thunk.bx>
 489:	81 c3 77 1b 00 00    	add    $0x1b77,%ebx
 48f:	83 ec 04             	sub    $0x4,%esp
 492:	80 bb 14 00 00 00 00 	cmpb   $0x0,0x14(%ebx)
 499:	75 28                	jne    4c3 <__do_global_dtors_aux+0x43>
 49b:	8b 83 f0 ff ff ff    	mov    -0x10(%ebx),%eax
 4a1:	85 c0                	test   %eax,%eax
 4a3:	74 12                	je     4b7 <__do_global_dtors_aux+0x37>
 4a5:	83 ec 0c             	sub    $0xc,%esp
 4a8:	ff b3 10 00 00 00    	pushl  0x10(%ebx)
 4ae:	ff 93 f0 ff ff ff    	call   *-0x10(%ebx)
 4b4:	83 c4 10             	add    $0x10,%esp
 4b7:	e8 34 ff ff ff       	call   3f0 <deregister_tm_clones>
 4bc:	c6 83 14 00 00 00 01 	movb   $0x1,0x14(%ebx)
 4c3:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 4c6:	c9                   	leave
 4c7:	c3                   	ret
 4c8:	90                   	nop
 4c9:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi

000004d0 <frame_dummy>:
 4d0:	55                   	push   %ebp
 4d1:	89 e5                	mov    %esp,%ebp
 4d3:	5d                   	pop    %ebp
 4d4:	e9 57 ff ff ff       	jmp    430 <register_tm_clones>

000004d9 <__x86.get_pc_thunk.dx>:
 4d9:	8b 14 24             	mov    (%esp),%edx
 4dc:	c3                   	ret

000004dd <abc>:
 4dd:	55                   	push   %ebp
 4de:	89 e5                	mov    %esp,%ebp
 4e0:	53                   	push   %ebx
 4e1:	83 ec 14             	sub    $0x14,%esp
 4e4:	e8 f7 fe ff ff       	call   3e0 <__x86.get_pc_thunk.bx>
 4e9:	81 c3 17 1b 00 00    	add    $0x1b17,%ebx
 4ef:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%ebp)
 4f6:	8b 45 f4             	mov    -0xc(%ebp),%eax
 4f9:	3b 45 0c             	cmp    0xc(%ebp),%eax
 4fc:	7d 1b                	jge    519 <abc+0x3c>
 4fe:	83 ec 08             	sub    $0x8,%esp
 501:	ff 75 08             	pushl  0x8(%ebp)
 504:	8d 83 34 e5 ff ff    	lea    -0x1acc(%ebx),%eax
 50a:	50                   	push   %eax
 50b:	e8 b0 fe ff ff       	call   3c0 <printf@plt>
 510:	83 c4 10             	add    $0x10,%esp
 513:	83 45 f4 01          	addl   $0x1,-0xc(%ebp)
 517:	eb dd                	jmp    4f6 <abc+0x19>
 519:	90                   	nop
 51a:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 51d:	c9                   	leave
 51e:	c3                   	ret

Disassembly of section .fini:

00000520 <_fini>:
 520:	53                   	push   %ebx
 521:	83 ec 08             	sub    $0x8,%esp
 524:	e8 b7 fe ff ff       	call   3e0 <__x86.get_pc_thunk.bx>
 529:	81 c3 d7 1a 00 00    	add    $0x1ad7,%ebx
 52f:	83 c4 08             	add    $0x8,%esp
 532:	5b                   	pop    %ebx
 5
```

## External links
- [Redirecting functions in shared ELF libraries](https://www.codeproject.com/Articles/70302/Redirecting-functions-in-shared-ELF-libraries)
