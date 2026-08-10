# Ω-Lab — Реестр гипотез

Этот файл является живым реестром. Гипотезы не удаляются. При новых данных меняется статус, а история проверки сохраняется в экспериментах.

| ID | Гипотеза | Статус | Основание / следующий контроль |
|---|---|---|---|
| H-0.1 | Фундаментальные отношения как исходная исследовательская постановка | OPEN | Требует формальной минимизации |
| H-0.2 | Порядок / минимальное время может быть реконструирован из акта и обновляемого следа | PARTIALLY_CONFIRMED | Ω-0; результат относится к внутреннему порядку модели, не к физическому времени |
| H-0.3 | Функциональная память возникает из обновляемой структуры и влияет на будущее | PARTIALLY_CONFIRMED | Ω-0 + Ω-MEM-1a–1d; требуется количественная проверка prediction/information advantage |
| H-0.4 | Два состояния являются минимально достаточными для причинного влияния памяти в данной архитектуре | NEEDS_RETEST | S=1 не имеет альтернативного состояния, S=2 может иметь causal effect; универсальность не доказана |
| H-0.5 | Structured memory всегда превосходит random memory | REJECTED | Ω-MEM-1c показал trade-off: random может срабатывать чаще при больших S, structured может давать более сильный эффект |
| H-0.6 | Воля является источником актов | OPEN | Не использовать как предпосылку до минимальных тестов |
| H-0.7 | Память может быть не хранилищем состояния, а хранилищем связи между состояниями | OPEN | Проверяется через Ω-MEM-2 и последующие relation-memory эксперименты |
| H-MEM-2 | Prediction advantage связан со структурой памяти | PARTIALLY_CONFIRMED | Ω-MEM-3/4R; преимущество наблюдается не универсально |
| H-MEM-2.1 | Prediction value зависит от структурного соответствия обновления памяти структуре процесса | REFINED | Ω-MEM-3/4R: поддержка на части процессов и контрпример Thue-Morse |
| H-MEM-2.2 | Prediction value зависит от structural match при условии достаточной expressive capacity | REFINED | Ω-MEM-4R: Matched > Random at equal S для 3/4 структурированных процессов; Thue-Morse — критический контрпример. Не считать универсально подтверждённой |
| H-MEM-2.3 | Prediction advantage depends on sufficient expressive capacity, informational content of state, and robustness to implementation loss | PARTIALLY_CONFIRMED | Ω-MEM-4R: expressiveness threshold, process-specific minimal sufficient statistic, implementation loss и iid control поддержаны; Thue-Morse и random-feature advantage требуют дальнейшей проверки |

## Правило статусов

OPEN → TESTING → CONFIRMED / PARTIALLY_CONFIRMED / REFINED / REJECTED / NEEDS_RETEST.

Переход статуса не удаляет предыдущую версию. Любое опровержение является результатом и должно быть связано с экспериментом, который его вызвал.

## Правило интерпретации

**OBSERVATION ≠ INTERPRETATION ≠ HYPOTHESIS.**

Если эксперимент ломает конкретную архитектуру, сначала меняется статус архитектуры/гипотезы в пределах проверенной модели. Более сильный универсальный вывод требует дополнительных независимых контролей.

## Ω-MEM-4 / Ω-MEM-4R rule

Ω-MEM-4 сохраняется как exploratory experiment с известными ошибками. Ω-MEM-4R является отдельной corrected replication и не стирает исходный результат.

Ω-MEM-4R показал:

- Periodic-4: expressive threshold at S=4;
- Markov-2: in the tested generator, Context-1 was already sufficient;
- Thue-Morse: chosen matched position-counter was insufficient at every tested S;
- HMM: discretization can create implementation loss;
- Random-iid: negative control works.

Следующий контроль для H-MEM-2.3: независимая репликация или теоретический анализ, затем — при сохранении гипотезы — Ω-MEM-5 on autonomous predictive-state discovery.
