function validateTransaction(transaction) {
    if (!transaction) return false;
    if (!transaction.amount) return false;
    if (!transaction.currency) return false;

    return true;
}

module.exports = {
    validateTransaction
};
// Validation revision 5
// Validation revision 11
// Validation revision 17
// Validation revision 23
