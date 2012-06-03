program TestASM;
(*
  http://acm.zhihua-lai.com
  TestASM.dpr
  Example Usage of Inline-Assembly in Delphi
  Compares Performance of Three Implementation of Fib Numbers
*)

{$APPTYPE CONSOLE}

uses
  Windows,
  SysUtils;

function Fib1(n: LongWord): LongWord; assembler; register;
asm
  PUSH EBX
  TEST EAX, EAX
  JZ @M
  MOV ECX, EAX
  XOR EAX, EAX
  MOV EDX, 1
@L:
  MOV EBX, EDX
  ADD EDX, EAX
  MOV EAX, EBX
  LOOP @L
@M:
  POP EBX
end;

function Fib2(n: LongWord): LongWord; assembler; register;
asm
  PUSH EBX
  XOR ECX, ECX
  TEST EAX, EAX
  JZ @L
  MOV EDX, 1
@M:
  MOV EBX, EDX
  ADD EDX, ECX
  MOV ECX, EBX
  DEC EAX
  JNZ @M
@L:
  MOV EAX, ECX
  POP EBX
end;

function Fib3(n: LongWord): LongWord;
var
  i, a, b, c: LongWord;
begin
  a := 0;
  b := 1;
  for i := 1 to n do
  begin
    c := b;
    b := a + b;
    a := c;
  end;
  Result := a;
end;

var
  i: integer;
  k: array [0..150000] of LongWord;
  start : cardinal;

begin
  for i := 0 to 20 do
  begin
    Writeln(Fib1(i), ' ', Fib2(i), ' ', Fib3(i));
  end;
  start := GetTickCount;
  for i := 0 to 150000 do
  begin
    k[i] := Fib1(i);
  end;
  Writeln(GetTickCount - start);
  start := GetTickCount;
  for i := 0 to 150000 do
  begin
    k[i] := Fib2(i);
  end;
  Writeln(GetTickCount - start);
  start := GetTickCount;
  for i := 0 to 150000 do
  begin
    k[i] := Fib3(i);
  end;
  Writeln(GetTickCount - start);
  Readln;
end.