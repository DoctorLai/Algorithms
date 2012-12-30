'convert.vbs
'http://rot47.net
'http://www.zhihua-lai.com/acm
'Arbitrary Base Number Converter

Const BASE2  = "01"
Const BASE8  = "01234567"
Const BASE10 = "0123456789"
Const BASE16 = "0123456789abcdef"
Const BASE32 = "0123456789abcdefghijklmnopqrstuvwxyz"
Const BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Const BASE75 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,!=-*(){}[]"

Function Convert(src, srctable, desttable)
	Dim srclen
	srclen = Len(srctable)
	Dim destlen
	destlen = Len(desttable)
	Dim val, numlen
	val = 0
	numlen = Len(src)
	Dim i
	For i = 0 To numlen - 1
		val = val * srclen + InStr(srctable, Mid(src, i + 1, 1)) - 1
	Next
	If val < 0 Then
		Convert = 0
		Exit Function
	End If
	Dim r, res, q
	r = val Mod destlen
	res = Mid(desttable, r + 1, 1)
	q = Int(val / destlen)
	While q > 0 
		r = q Mod destlen
		q = Int(q / destlen)
		res = Mid(desttable, r + 1, 1) & res
	WEnd
	convert = res
End Function
