$files = Get-ChildItem -Path "ТЭО*.md", "Манифест*.md", "FAQ.md"

foreach ($file in $files) {
    if (-not $file.Name.StartsWith("ТЭО") -and -not $file.Name.StartsWith("Манифест") -and -not $file.Name.StartsWith("FAQ")) { continue }

    $content = Get-Content $file.FullName -Raw
    
    # 1. Замена "скоринга" и контроля людей
    $content = $content -replace '(?i)превентивный ручной скоринг \(интервью \+ скоринг-модель\)', 'взаимное знакомство и совпадение по ценностям'
    $content = $content -replace '(?i)Скоринг-модель резидентов \(интервью \+ анализ\)а', 'глубинного интервью по ценностям'
    $content = $content -replace '(?i)Скоринг-модель резидентов \(интервью \+ анализ\)', 'глубинное интервью по ценностям'
    $content = $content -replace '(?i)Ценностно-компетентностный скоринг', 'Взаимное знакомство и ценностный отбор'
    $content = $content -replace '(?i)DAO-скоринг', 'рекомендация от действующих участников'
    $content = $content -replace '(?i)скоринг AI-ассистентом', 'первичное анкетирование'
    $content = $content -replace '(?i)AI HR-Scoring', 'Платформа поиска единомышленников'
    $content = $content -replace '(?i)NLP-анализ профилей и скоринг хард-скиллов резидентов', 'анализ профессионального опыта и компетенций'
    $content = $content -replace '(?i)скоринг внутри DAO', 'одобрение кооперативом единомышленников'
    $content = $content -replace '(?i)Многоуровневый скоринг', 'Многоуровневое знакомство'
    $content = $content -replace '(?i)внутренний скоринг', 'внутреннее согласование'
    $content = $content -replace '(?i)\(скоринг/онбординг\)', '(адаптация/онбординг)'
    $content = $content -replace '(?i)ручной скоринг', 'базовое анкетирование'
    $content = $content -replace '(?i)внутренний скоринг Синдикат \(Цифровой Кооператив\)а', 'внутреннее согласование Кооператива'
    
    # 2. Убираем ESG/Schwab нарративы
    $content = $content -replace '(?i)ESG-комплаенсу', 'гармоничному развитию'
    $content = $content -replace '(?i)ESG-трекинг', 'экологический мониторинг'
    $content = $content -replace '(?i)осознанное потребление', 'созидательное отношение к ресурсам'
    $content = $content -replace '(?i)Carbon Hub интеграция', 'интеграция решений для чистой среды'
    $content = $content -replace '(?i)Избыточный контроль', 'чрезмерное администрирование'

    # 3. Убираем "Тотальный контроль" 
    $content = $content -replace '(?i)контроль этапов сборки \(Camera Vision\)', 'открытая трансляция этапов сборки'

    # 4. HaaS по отношению к человеку/жилью 
    $content = $content -replace '(?i)до подписания HaaS-договора', 'до подписания договора участия'
    $content = $content -replace '(?i)HaaS-контракт', 'договор инфраструктурной подписки'

    # Сохраняем файл обратно
    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}
