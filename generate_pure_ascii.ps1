Add-Type -AssemblyName System.Drawing

$ImagePath = "C:\Users\Wali\Downloads\QuickShare\20260617_125532_1(1).jpg"

# Resolve output path dynamically relative to the script location
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$OutputPath = Join-Path $ScriptDir "ascii_avatar.txt"

$Img = [System.Drawing.Image]::FromFile($ImagePath)
$Bmp = New-Object System.Drawing.Bitmap($Img)

# Width needs to be smaller for raw text to fit on most screens without wrapping badly in markdown
$NewWidth = 150
$AspectRatio = $Bmp.Height / $Bmp.Width
$NewHeight = [math]::Floor($NewWidth * $AspectRatio * 0.5)

$ResizedBmp = New-Object System.Drawing.Bitmap($Bmp, $NewWidth, $NewHeight)

$Chars = @("@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " ")
$AsciiContent = ""

for ($y = 0; $y -lt $NewHeight; $y++) {
    $Line = ""
    for ($x = 0; $x -lt $NewWidth; $x++) {
        $Pixel = $ResizedBmp.GetPixel($x, $y)
        $Brightness = ($Pixel.R * 0.299) + ($Pixel.G * 0.587) + ($Pixel.B * 0.114)
        
        $Index = [math]::Floor(($Brightness / 255.0) * ($Chars.Length - 1))
        $Index = [math]::Max(0, [math]::Min($Chars.Length - 1, $Index))
        
        # Invert index for dark background
        $InvertedIndex = ($Chars.Length - 1) - $Index
        $Line += $Chars[$InvertedIndex]
    }
    $AsciiContent += $Line + "`r`n"
}

[System.IO.File]::WriteAllText($OutputPath, $AsciiContent, [System.Text.Encoding]::UTF8)

$Img.Dispose()
$Bmp.Dispose()
$ResizedBmp.Dispose()

Write-Host "Successfully generated raw ascii text at $OutputPath"
