# Display Mapping

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.5  
Language: en  
Status: Draft

## Purpose
Map internal projection enums to customer copy. Never expose raw enum names, conflict details, or technical source payloads in the customer UI.

| Internal enum | EN label | RU label | EN supporting text | RU supporting text |
|---|---|---|---|---|
| RETURN_IN_PROGRESS | Return in progress | Возврат товара в обработке | We are processing your return request. | Мы обрабатываем вашу заявку на возврат товара. |
| RETURN_REJECTED | Return not accepted | Возврат товара не принят | Contact support for the reason and available next steps. | Обратитесь в поддержку, чтобы узнать причину и дальнейшие действия. |
| AWAITING_CONFIRMATION | Return status being checked | Проверяем статус возврата | We are confirming the latest information. | Мы уточняем последние сведения о возврате. |
| REFUND_NOT_CONFIRMED | Return status being checked | Проверяем статус возврата | We are confirming the latest information. | Мы уточняем последние сведения о возврате. |
| NEEDS_RECONCILIATION | Return status being checked | Проверяем статус возврата | We are confirming the latest information. | Мы уточняем последние сведения о возврате. |
| REFUND_PROCESSING | Refund processing | Возврат денег обрабатывается | The payment provider is processing the refund. | Платежный провайдер обрабатывает возврат денег. |
| REFUND_FAILED | Refund needs attention | Требуется уточнить возврат денег | We need to resolve an issue with your refund. Contact support with your return reference. | Нужно разобраться с возвратом денег. Обратитесь в поддержку с номером возврата. |
| REFUND_ISSUED | Refund issued by provider | Возврат денег отправлен провайдером | Your bank may not show the credit yet. | Банк может еще не отображать зачисление. |

The supporting text is shown with the label, especially for REFUND_ISSUED. Unknown internal enums use the same neutral status-check label and create an internal rendering-contract incident. All status views offer a support action with the return reference. UI rendering never initiates reconciliation or payment actions.


---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
