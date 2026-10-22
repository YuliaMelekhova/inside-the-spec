One Status, Three Systems, Different Meanings

A return can be “completed” while the customer is still waiting for a refund.

Consider an illustrative retailer. The store completes an accepted-return workflow after registering a refund instruction. The warehouse completes an inspection. The payment provider completes its refund processing.

All three can send COMPLETED. They describe different objects and conditions. Translating each into “Money refunded” lets a store or warehouse event imply that the customer has their money before the provider has confirmed anything.

The mapping needs the source, the object, and the evidence behind the status. A completed inspection also needs a result: ACCEPTED or REJECTED. Finishing the inspection can mean rejecting the item.

I’d keep the return request, inspection, and refund as separate facts: return_state, inspection_state, and refund_state. inspection_state covers both in-progress and final results. The customer status depends on those facts and an unresolved reconciliation flag retained from earlier conflicts.

For an accepted item, provider completion matching the linked refund ID, amount, and currency can establish “Refund issued by provider” (REFUND_ISSUED), provided no conflict remains. The bank may not show the credit yet. A later valid provider failure updates this result.

In this case, warehouse acceptance authorizes dispatch. An early PSP event means warehouse evidence reached the projection late; it does not authorize paying before inspection. With complete snapshots and revisions per source object, delayed PENDING cannot overwrite newer COMPLETED.

Case 02 contains the source-status dictionary, nine decision rules yielding eight statuses, an event contract, UI labels, and 112 acceptance scenarios. Operational notes cover dispatch, financial handoff, and deadlines because these determine what happens when evidence is missing or contradictory.

The scenarios specify expected behavior, not executed integration tests. The model check evaluates 64 state combinations plus 64 reconciliation-flag cases: 128 inputs. This is a worked specification, not a report of a production incident.

A customer-facing status needs evidence from the system that owns the fact behind it.

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.
Case 02 · Cross-System Status Mapping

Full specification: https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/02-cross-system-status-mapping/README.md

#SystemsAnalysis #RequirementsEngineering #SystemIntegration
