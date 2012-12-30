'Rot47
'http://rot47.net

Function Rot47(str)
	Dim i, j, k, r
	j = Len(str)
	r = ""
	For i = 1 to j
		k = Asc(Mid(str, i, 1))
		If k >= 33 And k <= 126 Then
			r = r & Chr(33 + ((k + 14) Mod 94))
		Else
			r = r & Chr(k)
		End If
	Next
	Rot47 = r
End Function
