One Status, Three Systems, Different Meanings

A return can be “completed” while the customer is still waiting for a refund.

Consider an illustrative retailer with three systems. The store completes the accepted-return workflow after registering a refund instruction. The warehouse completes an inspection. The payment provider completes its own refund processing.

All three can send COMPLETED. They describe different objects and different conditions for completion. The store also needs a separate outcome for a rejected return closed without a refund.

If an integration translates every COMPLETED into “Money refunded,” a store or warehouse event can imply that the customer has their money before the provider has confirmed anything.

The mapping needs the source, the object, and the evidence behind the status. A completed warehouse inspection also needs inspection_result: ACCEPTED or REJECTED. Finishing the inspection can mean rejecting the item.

I’d keep return_state, inspection_state, and refund_state separate. inspection_state includes both an unfinished inspection and its final result. The customer label is calculated from these facts.

For an accepted item, a matching provider completion can establish REFUND_ISSUED. The UI says “Refund issued by provider,” with a note that the bank may not show the credit yet. A later provider failure updates this result. Provider completion is necessary; warehouse acceptance is also required in this case. An early provider result is retained while the missing warehouse evidence is checked.

Ordering matters too. With complete snapshots and a revision number per source object, a delayed PENDING cannot overwrite a newer COMPLETED. A later provider failure is a valid new outcome. Correcting a terminal warehouse result requires reconciliation that replaces the saved fact and revision.

Case 02 includes one source-status dictionary, a decision table, an event contract, UI labels, and 100 acceptance scenarios. The scenarios specify expected behavior, not executed integration tests. A separate model check covers all 64 state combinations and reconciliation overrides.

A useful review question: which system owns the evidence required for the status we show the customer?

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.
Case 02 · Cross-System Status Mapping

Full specification: https://github.com/YuliaMelekhova/inside-the-spec/blob/case-02-cross-system-status-mapping/cases/02-cross-system-status-mapping/README.md

#SystemsAnalysis #RequirementsEngineering #SystemIntegration
