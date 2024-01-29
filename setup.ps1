
# Print current date and time
Get-Date -Format "dddd, MMMM dd, yyyy"
Write-Host "Time: $(Get-Date -Format 'HH:mm:ss')"
Write-Host

Write-Host "Installing dependencies..."
cd '.\!@#$%'
# Install Python dependencies
pip install -r requirements.txt
pyarmor gen lib.py main.py setup.py
Move-Item '!#%' ./dist

# Remove original scripts
# Remove-Item lib.py, main.py, setup.py

# Run setup script
cd dist
python .\setup.py

# Move-Item '.\main.ps1' '..\..\Eagle-Encryptor.ps1'
# ps2exe ".\main.ps1" "..\..\Eagle-Encryptor.exe"
$sourceFile = Join-Path -Path $PWD -ChildPath "main.ps1"
$parentDirectory = Split-Path -Path $PSScriptRoot -Parent
$shortcutPath = Join-Path -Path $parentDirectory -ChildPath "Eagle-Encryptor.lnk"
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $sourceFile
$shortcut.Save()


Write-Host "Shortcut created at: $shortcutPath"


# Wait for input berfor exiting
Write-Host
Read-Host -Prompt "Press Enter to continue... "
cd ..
Write-Host
