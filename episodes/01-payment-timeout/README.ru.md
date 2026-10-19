# Case 01 · Платёж после timeout: состояния, идемпотентность и восстановление

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.

[English](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/README.md) · [Русский](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/README.ru.md)

Пользователь пополняет баланс на €50. Запрос завершается timeout, но провайдер мог принять платёж. Кейс задаёт поведение при повторном запросе, позднем подтверждении и зачислении на баланс.

Это условный кейс. Версия спецификации: 0.3. Статус: Draft. 40 сценариев описывают ожидаемое поведение; тесты реализации не выполнялись.

## Материалы

| Материал | Назначение |
|---|---|
| [Полная спецификация](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/specification.ru.md) | Четыре основных артефакта, шесть приложений и 40 проверочных сценариев |
| [PDF-карусель](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/carousel.ru.pdf) | Согласованная компактная версия, 13 страниц |
| [Редактируемые таблицы и схемы](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/README.ru.md) | CSV и Mermaid с пояснениями и границами использования |

## Как читать кейс

Начните с рабочей ситуации и предпосылок провайдера в спецификации. Затем рассмотрите модель состояний, таблицу переходов, контракт идемпотентности и матрицу. Приложения задают разбор, классификацию ошибок, webhook, outbox, попытки и сверку. Проверочные сценарии связывают ожидаемое поведение с правилами.

`OUTCOME_UNKNOWN` не становится `FAILED` по таймеру или `NOT_FOUND`. Guard действует до доказанного разрешения исходного платежа. Уникальность проводки обеспечивает сервис баланса. Закрытие по `NOT_EXECUTED` требует гарантии PA-08, включая запрет будущего исполнения.

## Подготовка публикации

Комплект находится в ветке для проверки. Тексты постов LinkedIn ещё не добавлены. Адрес страницы кейса в PDF подключим после проверки окончательного адреса; текущая подпись Full specification не подтверждает наличие активной ссылки.

---

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
