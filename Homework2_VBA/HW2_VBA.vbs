Sub Stock2()


Dim CurrentRow, SummaryRow As Long
Dim OpenPrice, EndPrice, TotalVol As Double
Dim StockName As String
Dim MaxRow, BeginRow, EndRow As Long



For Each ws In Worksheets

ws.Range("I1").Value = "Ticker"
ws.Range("J1").Value = "Yearly Change"
ws.Range("K1").Value = "Percent Change"
ws.Range("L1").Value = "Total Stock Volume"

SummaryRow = 2
CurrentRow = 2               'initial for each sheet
BeginRow = 2
EndRow = 2
TotalVol = ws.Cells(BeginRow, 7).Value

 
MaxRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

For CurrentRow = 3 To MaxRow + 1
    If ws.Cells(CurrentRow, 1).Value = ws.Cells(BeginRow, 1).Value Then                       'if name match
        TotalVol = TotalVol + ws.Cells(CurrentRow, 7).Value
        
' if name not match, using Begin and End Row number of that Stock to get open/end stock price
    Else
        EndRow = CurrentRow - 1
        Name = ws.Cells(BeginRow, 1).Value
        OpenPrice = ws.Cells(BeginRow, 3).Value
        EndPrice = ws.Cells(EndRow, 6).Value
        ws.Cells(SummaryRow, 9).Value = Name
        ws.Cells(SummaryRow, 10).Value = EndPrice - OpenPrice
            If OpenPrice <> 0 Then                                                            ' there is a condition of open price is 0, which will lead to calculation error
                ws.Cells(SummaryRow, 11).Value = (EndPrice - OpenPrice) / OpenPrice
            ElseIf EndPrice <> 0 Then
                ws.Cells(SummaryRow, 11).Value = 1
            Else
                ws.Cells(SummaryRow, 11).Value = 0
            End If
        ws.Cells(SummaryRow, 12).Value = TotalVol
        SummaryRow = SummaryRow + 1
        TotalVol = ws.Cells(CurrentRow, 7).Value
        BeginRow = CurrentRow                                    'set a new begin row number for a new stock
    End If

Next CurrentRow


'start to formattging summary table
ws.Range("N2").Value = "Greatest % Increase"
ws.Range("N3").Value = "Greatest % Decrease"
ws.Range("N4").Value = "Greatest Total Volume"
ws.Range("O1").Value = "Ticker"
ws.Range("P1").Value = "Value"

Dim TotalRow As Long
Dim Increase, Decrease, GrtTotal As Double
Dim InName, DeName, TotName As String

TotalRow = ws.Range("I1").End(xlDown).Row
Increase = 0
Decrease = 0
GrtTotal = 0

For i = 2 To TotalRow
    If ws.Cells(i, 11).Value > Increase Then
        Increase = ws.Cells(i, 11).Value
        InName = ws.Cells(i, 9).Value
    End If
    
    If ws.Cells(i, 11).Value < Decrease Then
        Decrease = ws.Cells(i, 11).Value
        DeName = ws.Cells(i, 9).Value
    End If

    If ws.Cells(i, 12).Value > GrtTotal Then
        GrtTotal = ws.Cells(i, 12).Value
        TotName = ws.Cells(i, 9).Value
    End If
    
    If ws.Cells(i, 10).Value > 0 Then
        ws.Cells(i, 10).Interior.ColorIndex = 4
    ElseIf ws.Cells(i, 10).Value < 0 Then
        ws.Cells(i, 10).Interior.ColorIndex = 3
    End If
Next i

ws.Range("O2").Value = InName
ws.Range("P2").Value = Increase
ws.Range("O3").Value = DeName
ws.Range("P3").Value = Decrease
ws.Range("O4").Value = TotName
ws.Range("P4").Value = GrtTotal

ws.Columns("A:P").AutoFit

ws.Range("K2:K" & TotalRow).NumberFormat = "0.00%"
ws.Range("P2:P3").NumberFormat = "0.00%"

Next ws

End Sub



