Import-Module .\Modules\ImportExcel

#$header = "humidity", "temp", "gas", "pressure", "timestamp"
$header = "temp", "pressure", "humidity", "gas","altitude", "timestamp"

$xlfileName = 'data.xlsx'
Remove-Item $xlfileName -ErrorAction SilentlyContinue

$humidity = New-ExcelChartDefinition -Title humidity -YRange humidity -NoLegend -ChartType Line
$temp = New-ExcelChartDefinition -Title temp -YRange temp -NoLegend -ChartType Line -Row 21
$gas = New-ExcelChartDefinition -Title gas -YRange gas -NoLegend -ChartType Line -Row 42


$excel = Import-Csv data_cap/interior_bme688.csv -header $header | Export-Excel $xlfileName -PassThru -AutoNameRange -AutoFilter -TableName Data -ExcelChartDefinition $temp, $humidity , $gas

Set-ExcelRange -Worksheet $excel.Sheet1 -Range 'A:C' -Width 10
Set-ExcelRange -Worksheet $excel.Sheet1 -Range 'D:D' -Width 24
Set-ExcelRange -Worksheet $excel.Sheet1 -Range 'E:E' -Width 54

Close-ExcelPackage $excel
