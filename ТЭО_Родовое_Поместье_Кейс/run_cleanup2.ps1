$files = Get-ChildItem -Path "ТЭО*.md", "Манифест*.md"

foreach ($file in $files) {
    if (-not $file.Name.StartsWith("ТЭО") -and -not $file.Name.StartsWith("Манифест")) { continue }
    $content = Get-Content $file.FullName -Raw

    $content = $content -replace '(?i)Этап 0: Скоринг и Аккредитация', 'Этап 0: Взаимное знакомство и Аккредитация'
    $content = $content -replace '(?i)Резидентский скоринг', 'Отбор по ценностям'
    $content = $content -replace '(?i)до момента подписания HaaS-договора', 'до момента подписания договора участия'
    $content = $content -replace '(?i)HaaS-договор', 'договор аренды инфраструктуры'
    $content = $content -replace '(?i)ESG / Carbon Hub', 'Экологический мониторинг ресурсов'
    $content = $content -replace '(?i)ESG-учёт и Carbon Hub', 'Экологический мониторинг'

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}
