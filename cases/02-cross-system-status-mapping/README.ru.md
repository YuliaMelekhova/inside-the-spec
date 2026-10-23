# Case 02 · Cross-System Status Mapping

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.

[English](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/README.md) · [Русский](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/README.ru.md)

One Status, Three Systems, Different Meanings

Опубликовано на GitHub · спецификация v0.5. Пост еще не опубликован в LinkedIn.

Учебный возврат товара между OMS, WMS и PSP. Общие технические артефакты на английском; русские пояснения помогают их читать.

Редакционная версия 0.5.2: в русских посте, PDF и пояснениях сохранены английские идентификаторы статусов. Финал остается утверждением. Техническая спецификация v0.5 не менялась.

## Материалы публикации

- [Post EN](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/post.en.md) · [Пост RU](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/post.ru.md)

[PDF EN](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/carousel.en.pdf) · [PDF RU](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/carousel.ru.pdf)

[Comment EN](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/comment.en.md) · [Комментарий RU](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/comment.ru.md)

## Рабочие артефакты

- [Полные переходы источников, дедупликация и ревизии](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/transition-and-deduplication.md)
- [Спецификация и таблица решений](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/specification.md)
- [Контракт события](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/event-contract.md)
- [Словарь исходных статусов](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/status-mapping.csv)
- [Правила использования словаря](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/status-mapping.notes.md)
- [Тексты интерфейса EN/RU](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/display-mapping.md)
- [Отправка, дедлайны и финансовые исключения](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/operational-contract.md)
- [112 приемочных сценариев](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/acceptance-scenarios.md)
- [64 комбинации состояний](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/decision-combinations.csv)
- [Границы проверки модели](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/combination-check.notes.md)
- [Воспроизводимая проверка модели](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/verify.py)
- [Отчет проверки модели](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/validation-report.md)
- [Русские пояснения](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/notes.ru.md)
- [Внешние источники](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/source-notes.md)

Проверка модели охватывает 128 входов: 64 сочетания состояний и 64 варианта с флагом сверки. Приемочные сценарии являются ожидаемым поведением, не выполненными интеграционными тестами.

[All cases](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/README.md) · [Yulia Melekhova on LinkedIn](https://www.linkedin.com/in/yuliamelekhova)

[PDF export validation](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/artifacts/pdf-validation.md)

## Русские обозначения статусов

В русских материалах системные статусы сохраняют точные английские идентификаторы рядом с переводом. Для одинаковых enum у разных фактов указано поле. Таблицы показывают идентификатор и пояснение в одной строке; UI-тексты и документирующие их enum разделены. Редакционная правка не меняет контракт и ожидаемые результаты сценариев.
