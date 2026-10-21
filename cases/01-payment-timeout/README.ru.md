# Case 01 · Платёж после timeout: состояния, идемпотентность и восстановление

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.

[English](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/README.md) · [Русский](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/README.ru.md)

Пользователь пополняет баланс на €50. Запрос завершается timeout, но провайдер мог принять платёж. Кейс задаёт поведение при повторном запросе, позднем подтверждении и зачислении на баланс.

Это условный кейс. Версия спецификации: 0.4. Статус: опубликовано на GitHub. 58 сценариев описывают ожидаемое поведение; тесты реализации не выполнялись.

## Материалы

| Материал | Назначение |
|---|---|
| [Полная спецификация](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/artifacts/specification.ru.md) | Четыре основных артефакта, шесть приложений и 58 проверочных сценариев |
| [Текст поста LinkedIn](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/post.ru.md) | Полный русский текст публикации |
| [Комментарии EN](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/comment.en.md) · [RU](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/comment.ru.md) | Готовые комментарии со ссылками на материалы |
| [PDF-карусель](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/carousel.ru.pdf) | Согласованная компактная версия, 15 страниц |
| [Редактируемые таблицы и схемы](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/artifacts/README.ru.md) | CSV и Mermaid с пояснениями и границами использования |

## Как читать кейс

Начните с рабочей ситуации и предпосылок провайдера в спецификации. Затем рассмотрите модель состояний, таблицу переходов, контракт идемпотентности и матрицу. Приложения задают разбор, классификацию ошибок, webhook, outbox, попытки и сверку. Проверочные сценарии связывают ожидаемое поведение с правилами.

`OUTCOME_UNKNOWN` не становится `FAILED` по таймеру или `NOT_FOUND`. Guard действует до доказанного разрешения; WR-01 безопасно закрывает доказанно неотправленный CREATED. Неизвестное зачисление отделено от hold; lookup баланса чтением продолжается во время разбора. Уникальность проводки обеспечивает сервис баланса. Закрытие по `NOT_EXECUTED` требует гарантии PA-08, включая запрет будущего исполнения.

[Изменения v0.4](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/changes-v0.4.ru.md)

## Статус публикации

Материалы v0.4 опубликованы в основной ветке GitHub. Посты и комментарии подготовлены на двух языках; публикация в LinkedIn ожидается. Ссылки в обоих PDF и комментариях ведут на страницы кейса в main. Для публикации используйте post.en.md с carousel.en.pdf и добавьте подготовленные комментарии EN/RU; русская пара доступна отдельно.

---

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
