'Rot5 + Rot13
'http://rot47.net

Function Rot5(str)
	Dim i, j, k, r
	j = Len(str)
	r = ""
	For i = 1 to j
		k = Asc(Mid(str, i, 1))
		If k >= 48 And k <= 57 Then
			If (k <= 52) Then
				r = r & Chr(k + 5)
			Else
				r = r & Chr(k - 5)
			End If
		Else
			r = r & Chr(k)
		End If
	Next
	Rot5 = r
End Function

Function Rot13(str)
	Dim i, j, k, r
	j = Len(str)
	r = ""
	For i = 1 to j
		k = Asc(Mid(str, i, 1))
		If k >= 97 And k <= 109 Then 
			k = k + 13 
		ElseIf k >= 110 And k <= 122 Then 
			k = k - 13 
    ElseIf k >= 65 And k <= 77 Then 
			k = k + 13 
		ElseIf k >= 78 And k <= 90 Then 
			k = k - 13 
		Else
			'out of range, do nothing
		End If
		r = r & Chr(k)
	Next
	Rot13 = r
End Function
