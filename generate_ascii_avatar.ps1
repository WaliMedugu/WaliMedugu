Add-Type -AssemblyName System.Drawing

$ImagePath = "C:\Users\Wali\Downloads\QuickShare\20260617_125532_1(1).jpg"
$OutputPath = "C:\Users\Wali\.gemini\antigravity\scratch\github-profile-readme\ascii_avatar.svg"

$Img = [System.Drawing.Image]::FromFile($ImagePath)
$Bmp = New-Object System.Drawing.Bitmap($Img)

$NewWidth = 120
$AspectRatio = $Bmp.Height / $Bmp.Width
$NewHeight = [math]::Floor($NewWidth * $AspectRatio * 0.5)

$ResizedBmp = New-Object System.Drawing.Bitmap($Bmp, $NewWidth, $NewHeight)

$Chars = @("@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " ")
$AsciiLines = @()

for ($y = 0; $y -lt $NewHeight; $y++) {
    $Line = ""
    for ($x = 0; $x -lt $NewWidth; $x++) {
        $Pixel = $ResizedBmp.GetPixel($x, $y)
        # Calculate brightness (0 to 255)
        $Brightness = ($Pixel.R * 0.299) + ($Pixel.G * 0.587) + ($Pixel.B * 0.114)
        
        $Index = [math]::Floor(($Brightness / 255.0) * ($Chars.Length - 1))
        $Index = [math]::Max(0, [math]::Min($Chars.Length - 1, $Index))
        
        $InvertedIndex = ($Chars.Length - 1) - $Index
        $Line += $Chars[$InvertedIndex]
    }
    $AsciiLines += $Line
}

$FontSize = 12
$CharWidth = $FontSize * 0.6
$LineHeight = $FontSize * 1.2

$SvgWidth = [math]::Floor($NewWidth * $CharWidth) + 20
$SvgHeight = [math]::Floor($NewHeight * $LineHeight) + 20

$SvgContent = @"
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 $SvgWidth $SvgHeight" width="100%" height="100%">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a0a" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bgGradient)" rx="15" />
  <rect width="100%" height="100%" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" rx="15" />
  <g font-family="monospace" font-size="${FontSize}px" fill="#00ff41" font-weight="bold" filter="url(#glow)">
"@

$YPos = $LineHeight
foreach ($Line in $AsciiLines) {
    $EscapedLine = $Line.Replace("&", "&amp;").Replace("<", "&lt;").Replace(">", "&gt;")
    $SvgContent += "`n    <text x=`"10`" y=`"$YPos`" xml:space=`"preserve`">$EscapedLine</text>"
    $YPos += $LineHeight
}

$SvgContent += "`n  </g>`n</svg>"

[System.IO.File]::WriteAllText($OutputPath, $SvgContent, [System.Text.Encoding]::UTF8)

$Img.Dispose()
$Bmp.Dispose()
$ResizedBmp.Dispose()

Write-Host "Successfully generated $OutputPath"
