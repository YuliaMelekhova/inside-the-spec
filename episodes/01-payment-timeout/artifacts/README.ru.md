# Редактируемые артефакты · Case 01

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.

[К странице кейса](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/README.ru.md)

Полная спецификация является основным источником правил. CSV и Mermaid точно извлечены из неё для редактирования и сравнения. Их нельзя использовать без предпосылок, условий и пояснений спецификации.

[Полная спецификация](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/specification.ru.md)

| Файл | Содержание |
|---|---|
| [payment-state-machine.ru.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/payment-state-machine.ru.mmd) | Состояния платежа |
| [payment-review-credit.ru.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/payment-review-credit.ru.mmd) | Связь платежа, разбора и зачисления |
| [review-lifecycle.ru.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/review-lifecycle.ru.mmd) | Жизненный цикл разбора |
| [credit-state-machine.ru.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/credit-state-machine.ru.mmd) | Состояния зачисления |
| [status-combinations.ru.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/status-combinations.ru.csv) | M-01: допустимые сочетания |
| [state-transitions.ru.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/state-transitions.ru.csv) | ST-01–ST-18 |
| [idempotency-matrix.ru.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/idempotency-matrix.ru.csv) | IM-01–IM-25 |
| [acceptance-scenarios.ru.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/episodes/01-payment-timeout/artifacts/acceptance-scenarios.ru.csv) | AC-01–AC-58 |

## Метаданные и использование

Version: 0.4  
Language: ru  
Status: Published on GitHub  
Author: Yulia Melekhova

CSV содержит только таблицы, в UTF-8, с запятой как разделителем. Текст сохраняет Markdown-оформление идентификаторов. Каждый CSV имеет английскую и русскую версии с одинаковыми ID и порядком строк. Mermaid использует комментарии `%%` для метаданных.

Проверено соответствие извлечённых строк и диаграмм исходной спецификации. Это проверка документов, а не выполнение 58 сценариев на реализации. При изменении правил синхронно обновляйте обе спецификации и производные файлы.

---

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
